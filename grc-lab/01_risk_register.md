# 📋 Enterprise Risk Register (NIST CSF 2.0 & ISO 27001:2022)
### CloudPay Technologies · Information Security & Governance Program

**Scoring Methodology:**
* **Likelihood (L):** 1 (Rare) · 2 (Unlikely) · 3 (Moderate) · 4 (Likely) · 5 (Almost Certain)
* **Impact (I):** 1 (Insignificant) · 2 (Minor) · 3 (Moderate) · 4 (Major) · 5 (Catastrophic)
* **Risk Score:** Likelihood × Impact (1–25)
  * 🔴 **Critical (16–25):** Immediate board escalation; mitigation within 30 days.
  * 🟠 **High (10–15):** Executive priority; remediation within 60 days.
  * 🟡 **Medium (5–9):** Operational tracking; quarterly review.
  * 🟢 **Low (1–4):** Monitored within standard operating procedures.

---

## 📊 Summary Table of Enterprise Risks

| ID | Domain | Risk Description | Inherent (L×I) | Primary Controls | Residual (L×I) | Treatment | Owner | Target Date |
|:---|:---|:---|:---:|:---|:---:|:---:|:---|:---:|
| **RSK-01** | **Identity / IAM** | Compromise of privileged cloud admin credentials via phishing leading to full AWS account takeover. | 4 × 5 = **20 (Crit)** | Hardware MFA (FIDO2) enforcement, Just-In-Time (JIT) AWS IAM Identity Center access, 4-hour max session. | 1 × 4 = **4 (Low)** | Mitigate | Head of SecOps | 30 Days |
| **RSK-02** | **Third-Party / TPRM** | Critical payment gateway API downtime or security breach causing severe customer transaction failure and SLA penalties. | 3 × 5 = **15 (High)** | Annual SOC 2 Type II audit review, multi-gateway failover routing, automated real-time API health probes. | 2 × 3 = **6 (Med)** | Mitigate / Transfer | VP Engineering | 60 Days |
| **RSK-03** | **AI Governance** | Accidental ingestion of plaintext customer PII/cardholder data into third-party LLM training pipelines via AI fraud model. | 4 × 4 = **16 (Crit)** | Presidio/regex automated data sanitization layer, BAA/Zero Data Retention contractual clause with AI vendor. | 1 × 3 = **3 (Low)** | Mitigate | Lead AI Engineer | 45 Days |
| **RSK-04** | **Cloud Security** | Accidental public exposure of AWS S3 storage bucket containing unencrypted database snapshots or financial transaction logs. | 3 × 5 = **15 (High)** | AWS Organizations Service Control Policy (SCP) blocking public S3 access, AWS Config continuous compliance rule. | 1 × 4 = **4 (Low)** | Mitigate | Cloud Architect | Completed |
| **RSK-05** | **Data Privacy (LGPD/GDPR)** | Inability to fulfill customer Data Subject Access Requests (DSAR) or Right to be Forgotten within statutory 15-day limit. | 4 × 3 = **12 (High)** | Centralized data catalog (OpenMetadata), automated DSAR workflow script, database pseudonymization. | 2 × 2 = **4 (Low)** | Mitigate | Data Protection Officer | 90 Days |
| **RSK-06** | **Ransomware / BCP** | Production database encryption and backup corruption via ransomware, causing multi-day platform unavailability. | 3 × 5 = **15 (High)** | AWS Backup Vault Lock (WORM / Immutable backups), cross-region replication to isolated AWS account, biannual restoration drill. | 1 × 4 = **4 (Low)** | Mitigate | Head of Infrastructure | 60 Days |
| **RSK-07** | **Application Security** | Critical SQL Injection or Broken Object Level Authorization (BOLA) vulnerability in payment processing API. | 3 × 4 = **12 (High)** | CI/CD SAST (Semgrep), DAST pipeline integration, annual third-party black-box penetration testing, bug bounty. | 1 × 3 = **3 (Low)** | Mitigate | AppSec Lead | Ongoing |
| **RSK-08** | **Insider Threat** | Unauthorized exfiltration of proprietary database records by a disgruntled departing engineer prior to offboarding. | 3 × 4 = **12 (High)** | Automated offboarding hook via Okta/HRIS, endpoint DLP monitoring, database query audit logging via pgAudit. | 2 × 2 = **4 (Low)** | Mitigate | GRC Analyst | 60 Days |
| **RSK-09** | **Supply Chain / Code** | Introduction of malicious dependency or typo-squatted package into core codebase via automated npm/pip build script. | 3 × 4 = **12 (High)** | Dependabot / Snyk automated SCA scanning, mandatory signed commits, required 2-person pull request approval. | 2 × 2 = **4 (Low)** | Mitigate | DevSecOps Lead | Completed |
| **RSK-10** | **Regulatory Compliance** | Failure to provide complete, timely audit evidence to external ISO 27001 / SOC 2 auditors resulting in qualified audit opinion. | 4 × 3 = **12 (High)** | Automated continuous compliance platform (Drata/Vanta), standardized evidence repository, quarterly mock audits. | 1 × 2 = **2 (Low)** | Mitigate | GRC Analyst | 90 Days |

---

## 🔍 Detailed Deep Dives on Priority Risks

### RSK-01: Compromise of Privileged Cloud Admin Credentials
* **Threat Source:** Advanced phishing, session hijacking, or credential stuffing targeting engineering leadership.
* **Vulnerability:** Static AWS IAM Access Keys stored on developer local workstations without mandatory IP-whitelisting.
* **NIST CSF 2.0 Mapping:** `PR.AA-01` (Credentials and authenticators are issued, managed, verified), `PR.AA-05` (Access permissions are managed).
* **ISO/IEC 27001:2022 Mapping:** Control `A.5.15` (Access control), Control `A.8.5` (Secure authentication).
* **Remediation Action Plan:**
  1. Deprecate and delete all long-lived IAM user access keys in AWS root/production accounts.
  2. Implement Okta SSO with mandatory FIDO2 (YubiKey) WebAuthn hardware tokens for all AWS CLI sessions via `aws-vault`.
  3. Enforce maximum 1-hour session duration with automated session invalidation upon anomaly detection.

### RSK-03: PII Leakage into External LLM Training Pipelines
* **Threat Source:** Internal developers piping raw production customer tickets or dispute logs into external AI APIs.
* **Vulnerability:** Lack of an automated egress data-inspection proxy between internal services and external AI endpoints.
* **NIST CSF 2.0 Mapping:** `GV.PO-01` (Organizational policy established), `PR.DS-01` (Confidentiality, integrity, availability of data-at-rest and in-transit).
* **ISO/IEC 27001:2022 Mapping:** Control `A.8.11` (Data masking), Control `A.5.8` (Information security in project management).
* **Remediation Action Plan:**
  1. Deploy an automated data classification and masking proxy (Microsoft Presidio) intercepting all AI prompt traffic.
  2. Execute formal Enterprise Zero Data Retention (ZDR) agreements and Business Associate Agreements with AI vendors.
  3. Publish employee AI Acceptable Use Policy (AUP) with mandatory acknowledgment.
