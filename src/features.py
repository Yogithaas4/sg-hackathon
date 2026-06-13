import pandas as pd
import numpy as np

SENSITIVITY_MAP = {"low": 1, "medium": 2, "high": 3, "critical": 4}
PRIVILEGE_MAP = {"user": 1, "power-user": 2, "admin": 3, "service-account": 2}
ACTION_RISK_MAP = {
    "login": 1, "sql_query": 2, "api_call": 2,
    "admin_operation": 3, "export_data": 4
}
TIME_CLASS_MAP = {
    "business_hours": 0, "unusual_hours": 1,
    "night": 2, "weekend": 2
}

def build_user_baselines(df):
    """Build per-user normal behavior profiles"""
    baselines = df.groupby("user_id").agg(
        avg_hour=("hour", "mean"),
        std_hour=("hour", "std"),
        typical_resources=("resource", lambda x: x.value_counts().to_dict()),
        action_counts=("action", lambda x: x.value_counts().to_dict()),
        total_events=("timestamp", "count"),
        normal_sensitivity=("resource_sensitivity", 
                           lambda x: x.map(SENSITIVITY_MAP).mean()),
        failure_rate=("status", lambda x: (x == "failure").mean())
    ).reset_index()
    baselines["std_hour"] = baselines["std_hour"].fillna(2.0)
    return baselines

def build_features(df, baselines):
    df = df.merge(baselines, on="user_id", suffixes=("", "_base"))
    
    # Sensitivity score
    df["sensitivity_score"] = df["resource_sensitivity"].map(SENSITIVITY_MAP).fillna(2)
    
    # Action risk score
    df["action_risk"] = df["action"].map(ACTION_RISK_MAP).fillna(2)
    
    # Time classification risk
    df["time_risk"] = df["time_classification"].map(TIME_CLASS_MAP).fillna(1)
    
    # Hour deviation from user's normal
    df["hour_deviation"] = abs(df["hour"] - df["avg_hour"]) / (df["std_hour"] + 1)
    
    # Is this a new resource for this user?
    user_resource_history = df.groupby(["user_id", "resource"]).cumcount()
    df["is_new_resource"] = (user_resource_history == 0).astype(int)
    
    # Privilege vs sensitivity mismatch
    df["privilege_score"] = df["privilege_level"].map(PRIVILEGE_MAP).fillna(1)
    df["privilege_sensitivity_gap"] = df["sensitivity_score"] - df["privilege_score"]
    df["privilege_sensitivity_gap"] = df["privilege_sensitivity_gap"].clip(0, 3)
    
    # Failure flag
    df["is_failure"] = (df["status"] == "failure").astype(int)
    
    # Is weekend/night access?
    df["off_hours_flag"] = df["time_classification"].isin(
        ["night", "weekend", "unusual_hours"]
    ).astype(int)
    
    # Days inactive flag (stale account accessing data)
    df["stale_account_flag"] = (df["days_inactive"] > 30).astype(int)
    
    # Short tenure + high sensitivity = risky
    df["new_user_sensitive_access"] = (
        (df["tenure_months"] < 3) & (df["sensitivity_score"] >= 3)
    ).astype(int)
    
    return df

FEATURE_COLS = [
    "sensitivity_score", "action_risk", "time_risk",
    "hour_deviation", "is_new_resource", "privilege_sensitivity_gap",
    "is_failure", "off_hours_flag", "stale_account_flag",
    "new_user_sensitive_access"
]