from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib
import pandas as pd
from src.features import FEATURE_COLS

def train_model(df):
    # Train only on "normal" labeled data if labels available,
    # else train on business_hours data as proxy for normal
    normal_df = df[df["time_classification"] == "business_hours"]
    
    X_train = normal_df[FEATURE_COLS].fillna(0)
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_train)
    
    model = IsolationForest(
        contamination=0.15,  # expect ~15% anomalies
        n_estimators=200,
        random_state=42
    )
    model.fit(X_scaled)
    
    joblib.dump(model, "outputs/model.pkl")
    joblib.dump(scaler, "outputs/scaler.pkl")
    return model, scaler

def predict_anomalies(df, model, scaler):
    X = df[FEATURE_COLS].fillna(0)
    X_scaled = scaler.transform(X)
    
    # Raw scores: more negative = more anomalous
    raw_scores = model.decision_function(X_scaled)
    
    # Convert to 0-100 risk score (higher = riskier)
    min_s, max_s = raw_scores.min(), raw_scores.max()
    risk_scores = 100 * (1 - (raw_scores - min_s) / (max_s - min_s))
    
    df["anomaly_score"] = model.predict(X_scaled)  # -1 = anomaly, 1 = normal
    df["risk_score"] = risk_scores.round(1)
    df["is_anomaly"] = df["anomaly_score"] == -1
    
    return df

def classify_severity(score):
    if score >= 86: return "CRITICAL"
    elif score >= 61: return "HIGH"
    elif score >= 31: return "MEDIUM"
    else: return "LOW"