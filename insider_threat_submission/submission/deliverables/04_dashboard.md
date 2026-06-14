# 04 - Dashboard

## Objective

Provide a dashboard for analysts to review top alerts, user activity, risky data assets, and model metrics.

## Implementation

Code:

- `dashboard/plots.py`
- `templates/index.html`
- `api/app.py`

Dashboard views include:

- Alert feed with severity and recommendation
- Anomaly heatmap by hour/day
- Top risky users timeline
- Model performance dashboard
- API-backed investigation view

## Theory

Security dashboards must reduce alert fatigue. The prototype emphasizes sortable alert summaries, severity badges, investigation context, and high-level metrics so analysts can quickly decide which incidents require blocking, investigation, or monitoring.

## Evidence

- `outputs/alert_feed.html`
- `outputs/heatmap.html`
- `outputs/user_timeline.html`
- `outputs/metrics_dashboard.html`
- Live UI: `http://127.0.0.1:5000/ui` after running `python api/app.py`

