import pandas as pd
import numpy as np
import random

def enrich_missing_columns(df):
    random.seed(42)
    np.random.seed(42)
    
    # Simulate rowcount based on action type
    rowcount_map = {
        "login": 0,
        "sql_query": np.random.randint(1, 500),
        "api_call": np.random.randint(1, 200),
        "admin_operation": np.random.randint(1, 100),
        "export_data": np.random.randint(1000, 60000)
    }
    df["rowcount"] = df["action"].map({
        "login": 0,
        "sql_query": 50,
        "api_call": 30,
        "admin_operation": 10,
        "export_data": 5000
    })
    # Add noise
    df["rowcount"] = df["rowcount"] * np.random.uniform(0.5, 10, len(df))
    df["rowcount"] = df["rowcount"].fillna(0).astype(int)
    
    # Simulate destination based on time_classification
    def get_destination(row):
        if row["time_classification"] in ["night", "weekend"]:
            return random.choice(["personal_usb", "external_email", "cloud_personal"])
        elif row["action"] == "export_data":
            return random.choice(["local", "external_email", "cloud_personal", "personal_usb"])
        else:
            return "local"
    df["destination"] = df.apply(get_destination, axis=1)
    
    # Simulate query_type
    query_map = {
        "login": "AUTH",
        "sql_query": "SELECT",
        "api_call": "GET",
        "admin_operation": "UPDATE",
        "export_data": "EXPORT"
    }
    df["query_type"] = df["action"].map(query_map)
    
    return df

def load_logs(path="data/data_access_logs.csv"):
    df = pd.read_csv(path, parse_dates=["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek
    df["date"] = df["timestamp"].dt.date
    df["is_weekend"] = df["day_of_week"] >= 5
    df = enrich_missing_columns(df)  # ADD THIS LINE
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