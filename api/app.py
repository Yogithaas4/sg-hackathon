from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import pandas as pd
import os

app = Flask(__name__)
CORS(app)
@app.route("/ui")
def ui():
    template_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
    return send_from_directory(template_path, "index.html")

@app.route("/")
def index():
    return jsonify({
        "status": "✅ Insider Threat Detection API Running",
        "endpoints": {
            "all_alerts": "/api/alerts",
            "filter_by_severity": "/api/alerts?severity=CRITICAL",
            "single_alert": "/api/alerts/<alert_id>",
            "user_profile": "/api/users/<user_id>",
            "summary": "/api/summary",
            "metrics": "/api/metrics"
        }
    })

def load_alerts():
    with open("outputs/alerts.json") as f:
        return json.load(f)

def load_scored():
    return pd.read_csv("outputs/scored_logs.csv")

@app.route("/api/alerts")
def get_alerts():
    alerts = load_alerts()
    severity = request.args.get("severity")
    if severity:
        alerts = [a for a in alerts if a["severity"] == severity.upper()]
    return jsonify(alerts)

@app.route("/api/alerts/<alert_id>")
def get_alert(alert_id):
    alerts = load_alerts()
    alert = next((a for a in alerts if a["alert_id"] == alert_id), None)
    if not alert:
        return jsonify({"error": "Not found"}), 404
    return jsonify(alert)

@app.route("/api/users/<user_id>")
def get_user(user_id):
    df = load_scored()
    user_events = df[df["user_id"] == user_id].to_dict(orient="records")
    alerts = [a for a in load_alerts() if a["user_id"] == user_id]
    return jsonify({"user_id": user_id, "events": user_events, "alerts": alerts})

@app.route("/api/summary")
def get_summary():
    alerts = load_alerts()
    summary = {
        "total": len(alerts),
        "critical": sum(1 for a in alerts if a["severity"] == "CRITICAL"),
        "high": sum(1 for a in alerts if a["severity"] == "HIGH"),
        "medium": sum(1 for a in alerts if a["severity"] == "MEDIUM"),
        "low": sum(1 for a in alerts if a["severity"] == "LOW"),
        "top_users": sorted(
            [{"user": a["username"], "score": a["risk_score"]} for a in alerts[:5]],
            key=lambda x: x["score"], reverse=True
        )
    }
    return jsonify(summary)

@app.route("/api/metrics")
def get_metrics():
    try:
        with open("outputs/metrics.json") as f:
            return jsonify(json.load(f))
    except:
        return jsonify({"error": "Run evaluate.py first"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)