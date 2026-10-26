# 🗺️ Multi-Framework Control Mapping Matrix
### Crosswalk: NIST CSF 2.0 · ISO/IEC 27001:2022 · SOC 2 Type II

This crosswalk provides the unified control baseline for **CloudPay Technologies**, allowing a single operational control implementation to satisfy multiple security and regulatory audits simultaneously.

---

## 🏛️ Comprehensive Framework Crosswalk

| Domain | Control Title | NIST CSF 2.0 Subcategory | ISO/IEC 27001:2022 Control | SOC 2 Type II (TSC 2017) | Operational Implementation Mechanism |
|:---|:---|:---|:---|:---|:---|
| **Governance** | Information Security Policy Management | **GV.PO-01** (Policy established and communicated) | **A.5.1** (Policies for information security) | **CC1.2, CC2.1** (Management tone & communication) | Version-controlled policies in GitHub (`security-policies/`), automated annual employee sign-off via HRIS. |
| **Governance** | Third-Party Risk Management (TPRM) | **GV.SC-04** (Suppliers are assessed prior to engagement) | **A.5.19, A.5.20** (Supplier security & addressing security in agreements) | **CC9.2** (Vendor risk assessment & monitoring) | Annual SOC 2 review, automated vendor security scoring (BitSight), mandatory security addendum (DPA/BAA). |
| **Identity & Access** | Multi-Factor Authentication (MFA) | **PR.AA-01** (Authenticators issued & verified) | **A.8.5** (Secure authentication) | **CC6.1** (Logical access controls) | Mandatory Okta FastPass / WebAuthn FIDO2 keys for all SaaS, VPN, and AWS cloud management consoles. |
| **Identity & Access** | Least Privilege & Role-Based Access | **PR.AA-05** (Access permissions managed & least privilege) | **A.5.15, A.5.18** (Access control & rights) | **CC6.2, CC6.3** (User registration & privileged access) | AWS IAM Identity Center with temporary role assumption, automated quarterly access reviews via Okta API. |
| **Data Protection** | Encryption at Rest & In Transit | **PR.DS-01** (Confidentiality & integrity of data protected) | **A.8.24** (Use of cryptography) | **CC6.6, CC6.7** (Data transmission & boundary protection) | TLS 1.3 enforced on Cloudflare WAF; AWS KMS customer-managed keys (CMK) with AES-256 on EBS, S3, and RDS Aurora. |
| **Data Protection** | Data Masking & Pseudonymization | **PR.DS-02** (Data-in-use protected) | **A.8.11** (Data masking) | **CC6.5** (Disposal and logical isolation) | Automated PII masking proxy for staging/test environments; hash salting for customer identifier storage. |
| **System Operations** | Vulnerability & Patch Management | **PR.PS-02** (Software maintained & patched) | **A.8.8** (Management of technical vulnerabilities) | **CC7.1** (Vulnerability infrastructure management) | Qualys VMDR cloud agent on EC2 instances; AWS Inspector container image scanning; SLA: Critical <7 days, High <30 days. |
| **System Operations** | Secure Software Development (AppSec) | **PR.PS-06** (Secure software development life cycle) | **A.8.25, A.8.28** (Secure development life cycle & secure coding) | **CC8.1** (Change management & code deployment) | Mandatory GitHub branch protection (2 approvals, passing SAST/Semgrep & SecretLint checks); no direct push to `main`. |
| **Detection & Monitoring** | Centralized Logging & Threat Detection | **DE.CM-01** (Networks and environments are monitored) | **A.8.15, A.8.16** (Logging & monitoring activities) | **CC7.2** (System anomalies detection & monitoring) | AWS CloudTrail multi-region logs streamed to immutable S3 bucket; Wazuh SIEM agent correlation and alerting via PagerDuty. |
| **Incident Response** | Incident Handling & Escalation Plan | **RS.MA-01** (Incident response plan executed) | **A.5.24, A.5.25** (Information security incident management planning) | **CC7.3, CC7.4** (Incident identification & communication) | Documented Incident Response Plan (IRP), annual tabletop simulation exercise (Ransomware / Data Breach), post-mortem root-cause analysis. |
| **Resilience & Continuity** | Immutable Backups & Disaster Recovery | **RC.RP-01** (Recovery plan executed) | **A.8.13, A.8.14** (Information backup & redundancy of processing facilities) | **A1.2, A1.3** (Backup procedures & recovery testing) | AWS Backup with Vault Lock (WORM compliance mode); cross-region backup replication; RTO < 4 hours, RPO < 15 minutes tested biannually. |
| **Emerging Tech** | AI Governance & Model Risk Management | **GV.PO-02** (Legal & regulatory requirements integrated) | **A.5.8** (Security in project management) | **CC3.2** (Risk assessment of emerging technologies) | AI Acceptable Use Policy; verification of zero-data retention clauses with third-party LLM providers; manual human-in-the-loop review for high-risk decisions. |

---

## 💡 How this Table Translates into Operational Efficiency

* **Zero Duplication:** Instead of maintaining three separate security checklists for ISO, NIST, and SOC 2, engineers implement one technical control (e.g., `A.8.24` / `PR.DS-01` / `CC6.6` via AWS KMS) and provide a single piece of evidence to all auditors.
* **Continuous Compliance Readiness:** Because each control maps to automated configurations (IAM, SCPs, KMS, GitHub settings), audit evidence collection is automated rather than manual screenshot gathering.
