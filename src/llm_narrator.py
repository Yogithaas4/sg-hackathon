import os
import json
from dotenv import load_dotenv
load_dotenv()

SENSITIVITY_MAP = {"low": 1, "medium": 2, "high": 3, "critical": 4}
ACTION_RISK_MAP = {
    "login": 1, "sql_query": 2, "api_call": 2,
    "admin_operation": 3, "export_data": 4
}

def classify_severity(score):
    if score >= 86: return "CRITICAL"
    elif score >= 61: return "HIGH"
    elif score >= 31: return "MEDIUM"
    else: return "LOW"

def build_anomaly_list(row):
    anomalies = []
    if row.get("off_hours_flag"):
        anomalies.append(f"Off-hours access at {row.get('hour',0):02d}:00 (normal 9-17)")
    if row.get("is_new_resource"):
        anomalies.append(f"First-time access to {row.get('resource','unknown')}")
    if row.get("sensitivity_score", 0) >= 3:
        anomalies.append(f"Accessed {row.get('resource_sensitivity','high')} sensitivity data")
    if row.get("action_risk", 0) >= 4:
        anomalies.append("High-risk action: export_data")
    if row.get("privilege_sensitivity_gap", 0) >= 2:
        anomalies.append("Privilege level below data sensitivity")
    if row.get("stale_account_flag"):
        anomalies.append(f"Account inactive for {row.get('days_inactive',0)} days")
    if row.get("new_user_sensitive_access"):
        anomalies.append("New user accessing sensitive data")
    return anomalies

def generate_narrative(row):
    anomalies = build_anomaly_list(row)
    action = row.get("action", "accessed data")
    resource = row.get("resource", "unknown resource")
    dept = row.get("department", "Unknown")
    time_class = row.get("time_classification", "unknown hours")
    risk_score = row.get("risk_score", 0)
    username = row.get("username", "Unknown user")

    if risk_score >= 86:
        narrative = (f"{username} from {dept} performed a high-risk {action} on "
                    f"{resource} during {time_class}. "
                    f"Multiple anomaly indicators: {', '.join(anomalies[:3]) if anomalies else 'unusual pattern'}. "
                    f"Pattern consistent with data exfiltration behavior.")
        recommendation = "BLOCK"
        context = "No legitimate business context identified"
    elif risk_score >= 61:
        narrative = (f"{username} from {dept} accessed {resource} with unusual patterns "
                    f"during {time_class}. Anomalies: {', '.join(anomalies[:2]) if anomalies else 'deviation detected'}. "
                    f"Requires investigation to rule out insider threat.")
        recommendation = "INVESTIGATE"
        context = "Possible legitimate activity — verify with manager"
    else:
        narrative = (f"{username} from {dept} showed minor deviations during {time_class} "
                    f"on {resource}. Pattern warrants monitoring but may be legitimate.")
        recommendation = "MONITOR"
        context = "Likely legitimate business activity"

    return {
        "narrative": narrative,
        "recommendation": recommendation,
        "business_context": context
    }

def generate_alerts_json(df, top_n=50):
    high_risk = df[df["risk_score"] >= 31].sort_values(
        "risk_score", ascending=False
    ).head(top_n)

    alerts = []
    for i, (_, row) in enumerate(high_risk.iterrows()):
        narrative_data = generate_narrative(row)
        date_str = str(row["timestamp"])[:10].replace("-", "")
        alert = {
            "alert_id": f"ALERT-{date_str}-{i+1:03d}",
            "user_id": row.get("user_id", "UNKNOWN"),
            "username": row.get("username", "Unknown"),
            "risk_score": int(row.get("risk_score", 0)),
            "severity": classify_severity(row.get("risk_score", 0)),
            "timestamp": str(row["timestamp"]),
            "resource": row.get("resource", "Unknown"),
            "action": row.get("action", "Unknown"),
            "department": row.get("department", "Unknown"),
            "anomalies_detected": build_anomaly_list(row),
            "business_context": narrative_data["business_context"],
            "narrative": narrative_data["narrative"],
            "recommendation": narrative_data["recommendation"]
        }
        alerts.append(alert)

    return alerts