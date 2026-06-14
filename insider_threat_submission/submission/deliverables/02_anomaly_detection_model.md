# 02 - Anomaly Detection Model

## Objective

Detect unusual user data access behavior using behavioral baselines and machine learning.

## Implementation

Code:

- `src/features.py`
- `src/model.py`
- `main.py`

The model uses an Isolation Forest trained on events classified as normal business-hour behavior. Each access event is converted into numeric risk features before scoring.

## Features Used

- Data sensitivity score
- Action risk score
- Time risk score
- Hour deviation from user baseline
- First-time resource access
- Privilege vs sensitivity mismatch
- Failed access flag
- Off-hours flag
- Stale-account flag
- New-user sensitive access flag

## Theory

Isolation Forest is suitable for this problem because insider-threat behavior is rare compared with normal access. The algorithm isolates unusual points faster than normal points by recursively splitting feature space. Events that require fewer splits are treated as more anomalous.

User-level baselines reduce false positives by comparing each person against their own normal behavior, instead of only using global rules.

## Evidence

- Trained model: `outputs/model.pkl`
- Feature scaler: `outputs/scaler.pkl`
- Scored events: `outputs/scored_logs.csv`

