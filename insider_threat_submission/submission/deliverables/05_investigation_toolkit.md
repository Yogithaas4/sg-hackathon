# 05 - Investigation Toolkit

## Objective

Give analysts contextual information for each alert so they can investigate quickly.

## Implementation

Code:

- `src/llm_narrator.py`
- `api/app.py`
- `templates/index.html`

Each generated alert contains:

- Alert ID
- User ID and username
- Department
- Timestamp
- Resource
- Action
- Risk score
- Severity
- Detected anomaly indicators
- Business context
- Narrative explanation
- Recommendation

API endpoints:

- `/api/alerts`
- `/api/alerts?severity=CRITICAL`
- `/api/alerts/<alert_id>`
- `/api/users/<user_id>`
- `/api/summary`
- `/api/metrics`

## Theory

Explainability is critical in insider-threat detection because analysts need to distinguish malicious behavior from legitimate business activity. The toolkit provides the why behind each alert, not only the score.

Investigation context includes behavioral deviation, data sensitivity, privilege mismatch, stale account indicators, and exfiltration destination risk.

## Evidence

- `outputs/alerts.json`
- `outputs/anomaly_report.txt`
- `outputs/incident_report.md`

