# Insider Threat Detection System - Submission Pack

This submission contains a complete prototype for Problem 04: Data Access Audit and Insider Threat Detection.

## How to Run

```bash
pip install -r requirements.txt
python main.py
python -c "from src.evaluate import evaluate; import pandas as pd; evaluate(pd.read_csv('outputs/scored_logs.csv'))"
python dashboard/plots.py
python api/app.py
```

Then open:

```text
http://127.0.0.1:5000/ui
```

## Deliverable Files

1. `deliverables/01_access_log_ingestion.md`
2. `deliverables/02_anomaly_detection_model.md`
3. `deliverables/03_risk_scoring_engine.md`
4. `deliverables/04_dashboard.md`
5. `deliverables/05_investigation_toolkit.md`
6. `deliverables/06_sample_incident_report.md`
7. `deliverables/07_evaluation_metrics.md`

## Main Evidence Artifacts

- `artifacts/alerts.json`
- `artifacts/scored_logs.csv`
- `artifacts/metrics.json`
- `artifacts/incident_report.md`
- `artifacts/alert_feed.html`
- `artifacts/heatmap.html`
- `artifacts/user_timeline.html`
- `artifacts/metrics_dashboard.html`
- `artifacts/scalability.md`

## Source Code Map

- Ingestion: `src/ingest.py`
- Feature engineering: `src/features.py`
- ML model: `src/model.py`
- Narratives and alert payloads: `src/llm_narrator.py`
- Evaluation: `src/evaluate.py`
- Report generation: `src/generate_report.py`
- Dashboard plots: `dashboard/plots.py`
- API and UI serving: `api/app.py`
- Pipeline entry point: `main.py`

