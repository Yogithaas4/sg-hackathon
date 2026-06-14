# 07 - Evaluation Metrics

## Objective

Measure detection quality using precision, recall, F1 score, anomaly counts, and severity breakdown.

## Implementation

Code: `src/evaluate.py`

Current metrics are saved to `outputs/metrics.json`.

## Current Results

| Metric | Value |
|---|---:|
| Total events | 1200 |
| Anomalies detected | 185 |
| Anomaly rate | 15.4% |
| Precision | 0.781 |
| Recall | 0.748 |
| F1 score | 0.764 |

## Severity Breakdown

| Severity | Count |
|---|---:|
| CRITICAL | 17 |
| HIGH | 124 |
| MEDIUM | 508 |
| LOW | 551 |

## Baseline Comparison

| Model | Precision | Recall | F1 |
|---|---:|---:|---:|
| Naive off-hours baseline | 0.400 | 0.350 | 0.373 |
| Proposed model | 0.781 | 0.748 | 0.764 |

## Theory

Precision measures how many generated alerts are truly suspicious. Recall measures how many real threats were detected. F1 balances both, which is useful for insider-threat detection because both missed incidents and alert fatigue are costly.

## Evidence

- `outputs/metrics.json`
- `outputs/metrics_dashboard.html`

