# 06 - Sample Incident Report

## Objective

Provide 10-15 detected threat narratives in a format suitable for security review.

## Implementation

Code:

- `src/generate_report.py`
- `src/llm_narrator.py`

The report selects top-ranked alerts and writes analyst-friendly incident summaries.

## Included Fields

Each incident includes:

- Alert ID
- User and department
- Risk score
- Severity
- Event timestamp
- Accessed resource
- Action performed
- Detected anomaly indicators
- Investigation narrative
- Recommended action

## Theory

Incident narratives translate model output into decision-ready language. This helps security teams communicate suspected insider-threat events to managers, compliance teams, and incident responders.

## Evidence

Full report: `outputs/incident_report.md`

Summary from current run:

- Total alerts: 50
- Critical alerts: 17
- High alerts: 33
- Report includes the top 10 detailed incidents

