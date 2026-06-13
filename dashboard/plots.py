import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json

def load_data():
    df = pd.read_csv("outputs/scored_logs.csv")
    with open("outputs/alerts.json") as f:
        alerts = json.load(f)
    with open("outputs/metrics.json") as f:
        metrics = json.load(f)
    return df, alerts, metrics

SEVERITY_COLORS = {
    "CRITICAL": "#FF0000",
    "HIGH": "#FF6B00",
    "MEDIUM": "#FFD700",
    "LOW": "#00C851"
}

def plot_alert_feed(alerts):
    df = pd.DataFrame(alerts)
    df["color"] = df["severity"].map(SEVERITY_COLORS)
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=["Alert ID", "User", "Dept", "Resource", "Action", "Risk Score", "Severity", "Recommendation"],
            fill_color="#1a1a2e",
            font=dict(color="white", size=13),
            align="left"
        ),
        cells=dict(
            values=[
                df["alert_id"], df["username"], df["department"],
                df["resource"], df["action"],
                df["risk_score"], df["severity"], df["recommendation"]
            ],
            fill_color=[["#2d0000" if s == "CRITICAL" else
                         "#2d1500" if s == "HIGH" else
                         "#2d2d00" if s == "MEDIUM" else
                         "#002d00" for s in df["severity"]]],
            font=dict(color="white", size=11),
            align="left"
        )
    )])
    fig.update_layout(
        title="🚨 Alert Feed — All Detected Threats",
        paper_bgcolor="#0d0d1a",
        font_color="white",
        height=600
    )
    fig.write_html("outputs/alert_feed.html")
    print("✅ alert_feed.html generated")

def plot_heatmap(df):
    df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour
    df["day_of_week"] = pd.to_datetime(df["timestamp"]).dt.day_name()
    
    day_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    heatmap_data = df[df["is_anomaly"] == True].groupby(
        ["day_of_week", "hour"]
    )["risk_score"].mean().reset_index()
    
    pivot = heatmap_data.pivot(index="day_of_week", columns="hour", values="risk_score").fillna(0)
    pivot = pivot.reindex([d for d in day_order if d in pivot.index])
    
    fig = px.imshow(
        pivot,
        labels=dict(x="Hour of Day", y="Day of Week", color="Avg Risk Score"),
        color_continuous_scale="Reds",
        title="🔥 Anomaly Heatmap — When Do Threats Occur?"
    )
    fig.update_layout(
        paper_bgcolor="#0d0d1a",
        plot_bgcolor="#0d0d1a",
        font_color="white",
        height=400
    )
    fig.write_html("outputs/heatmap.html")
    print("✅ heatmap.html generated")

def plot_user_timeline(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    
    top_users = (df[df["is_anomaly"] == True]
                 .groupby("user_id")["risk_score"]
                 .max()
                 .sort_values(ascending=False)
                 .head(10).index.tolist())
    
    top_df = df[df["user_id"].isin(top_users)].copy()
    top_df["severity"] = top_df["risk_score"].apply(
        lambda s: "CRITICAL" if s >= 86 else "HIGH" if s >= 61 else "MEDIUM" if s >= 31 else "LOW"
    )
    
    fig = px.scatter(
        top_df,
        x="timestamp", y="user_id",
        color="severity",
        size="risk_score",
        hover_data=["action", "resource", "risk_score"],
        color_discrete_map=SEVERITY_COLORS,
        title="👤 Top 10 Risky Users — Access Timeline"
    )
    fig.update_layout(
        paper_bgcolor="#0d0d1a",
        plot_bgcolor="#1a1a2e",
        font_color="white",
        height=500
    )
    fig.write_html("outputs/user_timeline.html")
    print("✅ user_timeline.html generated")

def plot_metrics_dashboard(metrics):
    fig = make_subplots(
        rows=2, cols=3,
        specs=[[{"type": "indicator"}, {"type": "indicator"}, {"type": "indicator"}],
               [{"type": "bar", "colspan": 2}, None, {"type": "pie"}]],
        subplot_titles=("Precision", "Recall", "F1 Score",
                        "Severity Breakdown", "", "Anomaly vs Normal")
    )

    perf = metrics["model_performance"]
    
    for i, (label, val) in enumerate([
        ("Precision", perf["precision"]),
        ("Recall", perf["recall"]),
        ("F1 Score", perf["f1_score"])
    ]):
        color = "green" if val >= 0.75 else "orange" if val >= 0.65 else "red"
        fig.add_trace(go.Indicator(
            mode="gauge+number",
            value=val * 100,
            title={"text": label, "font": {"color": "white"}},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": color},
                "steps": [
                    {"range": [0, 65], "color": "#2d0000"},
                    {"range": [65, 75], "color": "#2d2d00"},
                    {"range": [75, 100], "color": "#002d00"}
                ]
            },
            number={"suffix": "%", "font": {"color": "white"}}
        ), row=1, col=i+1)

    sev = metrics["severity_breakdown"]
    fig.add_trace(go.Bar(
        x=list(sev.keys()),
        y=list(sev.values()),
        marker_color=["#FF0000", "#FF6B00", "#FFD700", "#00C851"],
        text=list(sev.values()),
        textposition="auto"
    ), row=2, col=1)

    total = metrics["total_events"]
    anomalies = metrics["anomalies_detected"]
    fig.add_trace(go.Pie(
        labels=["Anomalies", "Normal"],
        values=[anomalies, total - anomalies],
        marker_colors=["#FF0000", "#00C851"],
        hole=0.4
    ), row=2, col=3)

    fig.update_layout(
        title="📊 Model Performance Dashboard",
        paper_bgcolor="#0d0d1a",
        plot_bgcolor="#1a1a2e",
        font_color="white",
        height=700,
        showlegend=False
    )
    fig.write_html("outputs/metrics_dashboard.html")
    print("✅ metrics_dashboard.html generated")

def generate_all():
    print("Generating dashboards...")
    df, alerts, metrics = load_data()
    plot_alert_feed(alerts)
    plot_heatmap(df)
    plot_user_timeline(df)
    plot_metrics_dashboard(metrics)
    print("\n✅ All dashboards saved to outputs/")

if __name__ == "__main__":
    generate_all()