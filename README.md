# 🛡️ Insider Threat Detection System

> AI-powered behavioral anomaly detection for enterprise data access monitoring.

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python main.py              # Run full ML pipeline
python api/app.py           # Start REST API + UI
open http://127.0.0.1:5000/ui  # Open dashboard
```

## 📊 Results
| Metric | Naive Baseline | Our Model | Improvement |
|---|---|---|---|
| Precision | 40% | **78.1%** | +38% |
| Recall | 35% | **74.8%** | +40% |
| F1 Score | 37% | **76.4%** | +39% |

## 🏗️ Architecture

## 📁 Outputs
- `alerts.json` — 50 prioritized alerts
- `metrics.json` — Precision/Recall/F1
- `incident_report.md` — 10 detailed threat narratives
- 4 interactive Plotly dashboards

## ⚡ Production Scale (1M+ events/day)
Apache Kafka → Spark Streaming → Feature Store → ML Pipeline → Redis → FastAPI

## 📋 Compliance
- ✅ GDPR Article 32
- ✅ NIST IR-4  
- ✅ SOX 302
