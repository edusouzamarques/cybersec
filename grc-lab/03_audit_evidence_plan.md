# 🔍 Audit Evidence Collection & Testing Plan
### Standard Operating Procedure for Internal & External Compliance Audits

**Author:** Eduardo de Souza Marques · GRC & Compliance Specialist  
**Standard Compliance:** SOC 2 Type II · ISO/IEC 27001:2022 Stage 2 Audit · NIST CSF 2.0 Evaluation

---

## 📑 Evidence Collection Matrix

| Evidence ID | Control Objective | Target Frameworks | Source System | Required Artifact & Format | Frequency | Verification Method |
|:---|:---|:---|:---|:---|:---|:---|
| **EVD-01** | Mandatory Multi-Factor Authentication | NIST PR.AA-01<br>ISO A.8.5<br>SOC 2 CC6.1 | **Okta Identity Cloud** | Active User Policy Export (`.csv` / API JSON) | Monthly | Verify 100% of active accounts have WebAuthn/FIDO2 enrolled. Zero SMS/voice bypass allowed. |
| **EVD-02** | Cloud Access Least Privilege & Key Rotation | NIST PR.AA-05<br>ISO A.5.15<br>SOC 2 CC6.3 | **AWS IAM** | AWS IAM Credential Report (`credential_report.csv`) | Quarterly | Verify zero static IAM access keys older than 90 days. Root account access keys must not exist. |
| **EVD-03** | Continuous Logging & Tamper-Proof Storage | NIST DE.CM-01<br>ISO A.8.15<br>SOC 2 CC7.2 | **AWS CloudTrail & S3** | CloudTrail Configuration JSON + S3 Bucket Policy | Continuous / Sample | Verify multi-region trails are enabled with S3 Object Lock (WORM) and log file validation enabled. |
| **EVD-04** | Vulnerability Remediation SLA Adherence | NIST PR.PS-02<br>ISO A.8.8<br>SOC 2 CC7.1 | **Qualys VMDR / AWS Inspector** | Executive Remediation Report (`.pdf` / `.csv`) | Bi-weekly | Sample 25 random vulnerability tickets. Verify Criticals remediated in <7 days and Highs in <30 days. |
| **EVD-05** | Secure Code Review & Peer Approval | NIST PR.PS-06<br>ISO A.8.28<br>SOC 2 CC8.1 | **GitHub Enterprise** | Branch Protection Settings JSON + PR Audit Log | Monthly (Sample 30 PRs) | Confirm `main` branch requires 2 code reviews, passing CI/CD tests (Semgrep/Snyk), and signed commits. |
| **EVD-06** | Data Encryption at Rest Across Databases | NIST PR.DS-01<br>ISO A.8.24<br>SOC 2 CC6.6 | **AWS RDS & KMS** | RDS Aurora Cluster Describe API Output | Quarterly | Inspect `StorageEncrypted: true` and verify KMS Key Policy restricts decryption to authorized roles. |
| **EVD-07** | Disaster Recovery & Backup Integrity | NIST RC.RP-01<br>ISO A.8.13<br>SOC 2 A1.2 | **AWS Backup** | Backup Job Report + Restoration Test Attestation | Biannual | Review documented test restoring an encrypted snapshot to an isolated VPC within 4-hour RTO SLA. |
| **EVD-08** | Third-Party Security Review (TPRM) | NIST GV.SC-04<br>ISO A.5.19<br>SOC 2 CC9.2 | **Vendor Risk Portal** | Vendor SOC 2 Report + Signed DPA/BAA | Annual (Tier 1 Vendors) | Inspect current SOC 2 Type II report for non-qualified opinion and review Complementary User Entity Controls (CUECs). |

---

## 💻 Technical CLI Audit Inspection Scripts

To eliminate human error and ensure audit reproducibility, the GRC team uses automated CLI validation queries:

### 1. Verification of AWS Root Account Access Keys & MFA (EVD-02)
```bash
# Generate and inspect IAM credential report
aws iam generate-credential-report
aws iam get-credential-report --output text --query 'Content' | base64 -d | cut -d, -f1,4,8,9,11,16 | column -t -s,

# Expected Audit Output:
# <root_account>  false  true  N/A  N/A  true (MFA active, zero static access keys)
```

### 2. Verification of CloudTrail Multi-Region & Log Integrity (EVD-03)
```bash
# Query active trails for multi-region logging and log validation
aws cloudtrail describe-trails --query "trailList[*].{Name:Name,IsMultiRegionTrail:IsMultiRegionTrail,LogFileValidationEnabled:LogFileValidationEnabled,KmsKeyId:KmsKeyId}" --output table

# Expected Audit Output:
# --------------------------------------------------------------------------
# |                             DescribeTrails                             |
# +-----------------------+-----------------------------+------------------+
# |  IsMultiRegionTrail   | LogFileValidationEnabled    | Name             |
# +-----------------------+-----------------------------+------------------+
# |  True                 | True                        | org-audit-trail  |
# +-----------------------+-----------------------------+------------------+
```

### 3. Verification of GitHub Branch Protection Rules (EVD-05)
```bash
# Inspect branch protection via GitHub CLI
gh api repos/cloudpay/core-payment-service/branches/main/protection \
  --jq '{
    required_approvals: .required_pull_request_reviews.required_approving_review_count,
    dismiss_stale: .required_pull_request_reviews.dismiss_stale_reviews,
    enforce_admins: .enforce_admins.enabled,
    required_status_checks: .required_status_checks.contexts
  }'

# Expected Audit Output:
# {
#   "required_approvals": 2,
#   "dismiss_stale": true,
#   "enforce_admins": true,
#   "required_status_checks": ["ci/semgrep-sast", "ci/secretlint", "ci/unit-tests"]
# }
```

---

## 🛡️ Auditor Chain of Custody & Evidence Preservation

Following strict investigative procedures:
1. **Timestamping & Hashing:** All exported audit logs (`.csv`, `.json`, `.pdf`) are SHA-256 hashed immediately upon extraction.
2. **Read-Only Storage:** Evidence is stored in a dedicated AWS S3 bucket with **Object Lock in Compliance Mode** (retention period: 7 years) to guarantee that logs cannot be altered or deleted by any user, including root administrators.
3. **Traceability:** Every piece of evidence is tagged with the Auditor ID, Timestamp, Source Endpoint, and Framework Control ID.
