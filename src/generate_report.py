import json

with open('outputs/alerts.json') as f:
    alerts = json.load(f)

report = '''# INSIDER THREAT INCIDENT REPORT
**Generated:** 2026-06-13
**System:** Data Access Audit & Insider Threat Detection
**Total Alerts:** {total} | CRITICAL: {crit} | HIGH: {high}

---

'''.format(
    total=len(alerts),
    crit=sum(1 for a in alerts if a['severity'] == 'CRITICAL'),
    high=sum(1 for a in alerts if a['severity'] == 'HIGH')
)

for i, alert in enumerate(alerts[:10], 1):
    report += f'''## Incident {i}: {alert['alert_id']}

| Field | Value |
|---|---|
| **User** | {alert['username']} ({alert['department']}) |
| **Risk Score** | {alert['risk_score']}/100 |
| **Severity** | {alert['severity']} |
| **Time** | {alert['timestamp']} |
| **Resource** | {alert['resource']} |
| **Action** | {alert['action']} |

**Anomalies Detected:**
{chr(10).join(f'- {a}' for a in alert['anomalies_detected'])}

**Investigation Narrative:**
{alert['narrative']}

**Recommendation:** `{alert['recommendation']}`

---

'''

with open('outputs/incident_report.md', 'w') as f:
    f.write(report)

print('Incident report saved!')