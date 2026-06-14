# Solution Video Script

Recommended length: 3 to 5 minutes.

## 1. Opening - 20 seconds

Hello, my project is "Data Access Audit and Insider Threat Detection". The goal is to detect suspicious enterprise data access behavior before sensitive information is leaked.

The system ingests access logs, builds user behavior features, detects anomalies, ranks alerts by risk, and provides a dashboard plus investigation narratives.

## 2. Problem Summary - 30 seconds

Enterprises process thousands or millions of database, API, BI, and file-access events every day. Manual review is impossible, and simple rules create too many false positives.

This solution focuses on identifying risky patterns such as off-hours access, stale account activity, first-time access to sensitive resources, privilege mismatch, bulk exports, and suspicious destinations.

## 3. Architecture - 45 seconds

The project has five main layers:

1. Ingestion: `src/ingest.py` loads access logs and user profiles.
2. Feature engineering: `src/features.py` creates behavioral and risk features.
3. Model: `src/model.py` trains an Isolation Forest anomaly detector.
4. Scoring and narratives: alerts are ranked with 0-100 risk scores and severity levels.
5. Dashboard and API: Flask APIs and dashboard views show alerts, users, metrics, and investigation context.

For production scale, the design can move to Kafka, Spark Streaming, a feature store, Redis cache, and SIEM/DLP integrations.

## 4. Code Walkthrough - 45 seconds

Show these files briefly:

- `main.py`: full pipeline entry point.
- `src/ingest.py`: loads and enriches logs.
- `src/features.py`: creates anomaly features.
- `src/model.py`: trains and applies the Isolation Forest model.
- `api/app.py`: exposes alert, user, summary, and metrics APIs.
- `dashboard/plots.py`: generates dashboard HTML files.

## 5. Demo - 90 seconds

Run or show the generated outputs:

```bash
python main.py
python dashboard/plots.py
python api/app.py
```

Open:

```text
http://127.0.0.1:5000/ui
```

Show:

- Alert summary cards.
- Critical/high alerts.
- One alert investigation panel.
- Risk score, anomaly reasons, narrative, and recommendation.
- Metrics dashboard.
- Incident report from `outputs/incident_report.md`.

## 6. Results - 40 seconds

The current run processed 1200 events and detected 185 anomalies.

Model results:

- Precision: 0.781
- Recall: 0.748
- F1 score: 0.764

Severity breakdown:

- Critical: 17
- High: 124
- Medium: 508
- Low: 551

These results meet the target of precision and recall above 70 percent.

## 7. Closing - 20 seconds

This submission includes detailed documentation, source code, generated dashboards, incident reports, evaluation metrics, and a production scalability design.

The solution helps analysts prioritize insider-threat investigations with explainable alerts instead of manually reviewing raw access logs.

