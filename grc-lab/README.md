# 🛡️ Enterprise GRC & Security Assurance Lab
### Multi-Framework Governance, Risk & Compliance Implementation (NIST CSF 2.0 · ISO/IEC 27001:2022 · SOC 2 Type II)

**Author:** Eduardo de Souza Marques  
**Focus:** Cybersecurity Governance, Risk, and Compliance (GRC) · Third-Party Risk (TPRM) · Security Assurance  
**Interactive Web Dashboard:** [Live GRC Lab Dashboard](https://edusouzamarques.github.io/cybersec/grc-lab.html)

---

## 📌 1. Executive Overview & Scenario

This laboratory models a complete, enterprise-grade Governance, Risk, and Compliance (GRC) program for **CloudPay Technologies**, a fast-growing B2B financial SaaS platform processing credit card transactions, storing customer Personally Identifiable Information (PII), and utilizing cloud-hosted Machine Learning (LLM) models for real-time fraud scoring.

### Regulatory & Threat Context:
* **Infrastructure:** 100% AWS Cloud-Native (EKS, Aurora PostgreSQL, S3, IAM, KMS) with multi-region replication.
* **Identity Architecture:** Okta Workforce Identity + Google Workspace + Hardware Security Keys (FIDO2/WebAuthn).
* **Compliance Targets:** 
  1. **NIST Cybersecurity Framework 2.0** (Govern, Identify, Protect, Detect, Respond, Recover).
  2. **ISO/IEC 27001:2022** (Information Security Management System - Annex A Controls).
  3. **AICPA SOC 2 Type II** (Security, Availability, and Confidentiality Trust Services Criteria).
  4. **Data Privacy:** LGPD (Brazil) and GDPR (EU) cross-border data protection principles.

---

## 📂 2. Laboratory Structure & Artifacts

| Artifact | File | Description |
|---|---|---|
| **01. Enterprise Risk Register** | [`01_risk_register.md`](01_risk_register.md) | 10 quantified enterprise risks (Inherent vs. Residual scoring, treatment strategy, and owner assignments). |
| **02. Multi-Framework Mapping** | [`02_control_mapping_matrix.md`](02_control_mapping_matrix.md) | Crosswalk connecting NIST CSF 2.0 functions to ISO 27001:2022 Annex A and SOC 2 Type II criteria. |
| **03. Audit Evidence & Testing Plan** | [`03_audit_evidence_plan.md`](03_audit_evidence_plan.md) | Practical auditor verification procedures, CLI query commands (AWS/Okta), and sampling criteria. |
| **04. Executive Security Memo** | [`04_executive_security_memo.md`](04_executive_security_memo.md) | C-Level briefing memo detailing Top 5 Priority Risks and the 90-day board-approved remediation budget. |
| **05. Third-Party Risk Assessment** | [`05_tprm_vendor_assessment.md`](05_tprm_vendor_assessment.md) | Complete vendor due diligence scorecard and security review for an external AI LLM API provider. |

---

## 🎯 3. Methodological Highlights: "Technical GRC"

Unlike superficial "paper compliance" that merely checks boxes without understanding systems, this lab demonstrates **Technical GRC**:
* **Evidence Tracing to Real Logs:** Controls are mapped directly to measurable telemetry (e.g., AWS CloudTrail multi-region trails, IAM Credential Reports, GitHub branch protection rules, Okta System Log queries).
* **AI Security Governance (ISO 42001 / NIST AI RMF):** Addresses emerging threat vectors, including sensitive data leakage into LLM training pipelines, prompt injection, and model hallucination risks in automated fraud decisions.
* **Investigative Evidence Discipline:** Applies 13+ years of formal investigation, rigorous chain-of-custody protocols, and procedural auditing to prevent non-conformities and audit sampling failures.

---

## 🚀 4. How to Explore

1. **Interactive UI:** Open [`grc-lab.html`](https://edusouzamarques.github.io/cybersec/grc-lab.html) to interact with the 5x5 dynamic Risk Heatmap, filter controls by domain, and inspect testing evidence live.
2. **Repository Source:** Review the detailed Markdown documents in this folder for formal audit documentation ready for regulatory examination.
