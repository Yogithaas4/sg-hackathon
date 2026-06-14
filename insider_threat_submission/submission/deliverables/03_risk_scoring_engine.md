# 03 - Risk Scoring Engine

## Objective

Convert anomaly scores and behavioral signals into ranked alert severity.

## Implementation

Code:

- `src/model.py`
- `src/llm_narrator.py`

The model's raw anomaly score is normalized to a 0-100 risk score. Severity is assigned using fixed thresholds:

| Risk Score | Severity |
|---:|---|
| 86-100 | CRITICAL |
| 61-85 | HIGH |
| 31-60 | MEDIUM |
| 0-30 | LOW |

## Theory

Risk scoring makes alerts actionable. Instead of giving analysts an unordered anomaly list, the engine combines statistical abnormality with security context such as sensitive data, off-hours activity, stale accounts, privilege mismatch, and suspicious destinations.

This prioritizes events likely to represent data exfiltration or unauthorized access.

## Evidence

- Alert list: `outputs/alerts.json`
- Scored event log: `outputs/scored_logs.csv`
- Severity counts: `outputs/metrics.json`

