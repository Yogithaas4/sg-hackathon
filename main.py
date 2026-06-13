from src.ingest import load_logs, load_profiles, merge_data
from src.features import build_user_baselines, build_features
from src.model import train_model, predict_anomalies, classify_severity
from src.llm_narrator import generate_alerts_json
import json

# 1. Load data
print("Loading data...")
logs = load_logs()
profiles = load_profiles()
df = merge_data(logs, profiles)

# 2. Build features
print("Engineering features...")
baselines = build_user_baselines(df)
df = build_features(df, baselines)

# 3. Train model
print("Training model...")
model, scaler = train_model(df)

# 4. Predict
print("Detecting anomalies...")
df = predict_anomalies(df, model, scaler)
df["severity"] = df["risk_score"].apply(classify_severity)

# 5. Generate alerts with LLM narratives
print("Generating LLM narratives (this takes 2-3 min)...")
alerts = generate_alerts_json(df)
with open("outputs/alerts.json", "w") as f:
    json.dump(alerts, f, indent=2)

print(f"Done! {len(alerts)} alerts generated.")
print(f"CRITICAL: {sum(1 for a in alerts if a['severity']=='CRITICAL')}")
print(f"HIGH: {sum(1 for a in alerts if a['severity']=='HIGH')}")

# Save scored dataframe
df.to_csv("outputs/scored_logs.csv", index=False)