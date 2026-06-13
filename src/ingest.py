import pandas as pd

def load_logs(path="data/data_access_logs.csv"):
    df = pd.read_csv(path, parse_dates=["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek  # 0=Mon, 6=Sun
    df["date"] = df["timestamp"].dt.date
    df["is_weekend"] = df["day_of_week"] >= 5
    return df

def load_profiles(path="data/user_profiles.csv"):
    df = pd.read_csv(path, parse_dates=["hire_date", "last_login"])
    df["tenure_days"] = (pd.Timestamp.now() - df["hire_date"]).dt.days
    df["tenure_months"] = df["tenure_days"] // 30
    return df

def merge_data(logs, profiles):
    df = logs.merge(profiles, on="user_id", how="left")
    # Fix duplicate columns after merge
    if "username_x" in df.columns:
        df["username"] = df["username_x"]
        df.drop(columns=["username_x", "username_y"], inplace=True)
    return df