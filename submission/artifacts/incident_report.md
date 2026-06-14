# INSIDER THREAT INCIDENT REPORT

Total: 50 | CRITICAL: 17 | HIGH: 33

---

## Incident 1: ALERT-20250507-001
- **User:** xiulan.colombo (Compliance)
- **Risk Score:** 100/100 — CRITICAL
- **Resource:** File_Share | **Action:** login
- **Time:** 2025-05-07 19:55:00
- **Anomalies:**   - First-time access to File_Share
  - Account inactive for 34 days
- **Narrative:** xiulan.colombo from Compliance performed a high-risk login on File_Share during business_hours. Multiple anomaly indicators: First-time access to File_Share, Account inactive for 34 days. Pattern consistent with data exfiltration behavior.
- **Recommendation:** 

---

## Incident 2: ALERT-20260110-002
- **User:** michael.sharma (Legal)
- **Risk Score:** 95/100 — CRITICAL
- **Resource:** Customer_Vault | **Action:** login
- **Time:** 2026-01-10 02:53:00
- **Anomalies:**   - Off-hours access at 02:00 (normal 9-17)
  - Accessed high sensitivity data
- **Narrative:** michael.sharma from Legal performed a high-risk login on Customer_Vault during unusual_hours. Multiple anomaly indicators: Off-hours access at 02:00 (normal 9-17), Accessed high sensitivity data. Pattern consistent with data exfiltration behavior.
- **Recommendation:** 

---

## Incident 3: ALERT-20250916-003
- **User:** nikhil.jang (HR)
- **Risk Score:** 95/100 — CRITICAL
- **Resource:** BI_Tool | **Action:** login
- **Time:** 2025-09-16 02:19:00
- **Anomalies:**   - First-time access to BI_Tool
- **Narrative:** nikhil.jang from HR performed a high-risk login on BI_Tool during business_hours. Multiple anomaly indicators: First-time access to BI_Tool. Pattern consistent with data exfiltration behavior.
- **Recommendation:** 

---

## Incident 4: ALERT-20251224-004
- **User:** george.lim (Engineering)
- **Risk Score:** 91/100 — CRITICAL
- **Resource:** HRIS | **Action:** login
- **Time:** 2025-12-24 11:43:00
- **Anomalies:**   - First-time access to HRIS
  - Accessed high sensitivity data
  - Privilege level below data sensitivity
  - Account inactive for 57 days
- **Narrative:** george.lim from Engineering performed a high-risk login on HRIS during business_hours. Multiple anomaly indicators: First-time access to HRIS, Accessed high sensitivity data, Privilege level below data sensitivity. Pattern consistent with data exfiltration behavior.
- **Recommendation:** 

---

## Incident 5: ALERT-20250525-005
- **User:** thomas.iyer (Sales)
- **Risk Score:** 90/100 — CRITICAL
- **Resource:** Customer_Vault | **Action:** login
- **Time:** 2025-05-25 12:53:00
- **Anomalies:**   - Off-hours access at 12:00 (normal 9-17)
  - First-time access to Customer_Vault
  - Accessed high sensitivity data
  - Privilege level below data sensitivity
  - Account inactive for 57 days
- **Narrative:** thomas.iyer from Sales performed a high-risk login on Customer_Vault during night. Multiple anomaly indicators: Off-hours access at 12:00 (normal 9-17), First-time access to Customer_Vault, Accessed high sensitivity data. Pattern consistent with data exfiltration behavior.
- **Recommendation:** 

---

## Incident 6: ALERT-20260213-006
- **User:** anthony.taylor (Finance)
- **Risk Score:** 90/100 — CRITICAL
- **Resource:** HRIS | **Action:** login
- **Time:** 2026-02-13 10:54:06
- **Anomalies:**   - First-time access to HRIS
  - Accessed high sensitivity data
  - Privilege level below data sensitivity
  - Account inactive for 51 days
- **Narrative:** anthony.taylor from Finance performed a high-risk login on HRIS during business_hours. Multiple anomaly indicators: First-time access to HRIS, Accessed high sensitivity data, Privilege level below data sensitivity. Pattern consistent with data exfiltration behavior.
- **Recommendation:** 

---

## Incident 7: ALERT-20251024-007
- **User:** thomas.kang (Engineering)
- **Risk Score:** 90/100 — CRITICAL
- **Resource:** Customer_Vault | **Action:** login
- **Time:** 2025-10-24 08:44:00
- **Anomalies:**   - First-time access to Customer_Vault
  - Accessed high sensitivity data
  - Privilege level below data sensitivity
- **Narrative:** thomas.kang from Engineering performed a high-risk login on Customer_Vault during business_hours. Multiple anomaly indicators: First-time access to Customer_Vault, Accessed high sensitivity data, Privilege level below data sensitivity. Pattern consistent with data exfiltration behavior.
- **Recommendation:** 

---

## Incident 8: ALERT-20260202-008
- **User:** george.clark (Engineering)
- **Risk Score:** 90/100 — CRITICAL
- **Resource:** PROD_DB | **Action:** export_data
- **Time:** 2026-02-02 10:54:06
- **Anomalies:**   - First-time access to PROD_DB
  - Accessed high sensitivity data
  - High-risk action: export_data
  - Account inactive for 55 days
- **Narrative:** george.clark from Engineering performed a high-risk export_data on PROD_DB during business_hours. Multiple anomaly indicators: First-time access to PROD_DB, Accessed high sensitivity data, High-risk action: export_data. Pattern consistent with data exfiltration behavior.
- **Recommendation:** 

---

## Incident 9: ALERT-20251214-009
- **User:** xiulan.colombo (Compliance)
- **Risk Score:** 90/100 — CRITICAL
- **Resource:** GL_System | **Action:** export_data
- **Time:** 2025-12-14 21:05:00
- **Anomalies:**   - Off-hours access at 21:00 (normal 9-17)
  - Accessed high sensitivity data
  - High-risk action: export_data
  - Privilege level below data sensitivity
  - Account inactive for 34 days
- **Narrative:** xiulan.colombo from Compliance performed a high-risk export_data on GL_System during unusual_hours. Multiple anomaly indicators: Off-hours access at 21:00 (normal 9-17), Accessed high sensitivity data, High-risk action: export_data. Pattern consistent with data exfiltration behavior.
- **Recommendation:** 

---

## Incident 10: ALERT-20251130-010
- **User:** stephen.bhat (Engineering)
- **Risk Score:** 89/100 — CRITICAL
- **Resource:** File_Share | **Action:** api_call
- **Time:** 2025-11-30 23:28:00
- **Anomalies:**   - First-time access to File_Share
- **Narrative:** stephen.bhat from Engineering performed a high-risk api_call on File_Share during business_hours. Multiple anomaly indicators: First-time access to File_Share. Pattern consistent with data exfiltration behavior.
- **Recommendation:** 

---

