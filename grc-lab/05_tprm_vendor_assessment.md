# 🏢 Third-Party Risk Management (TPRM) Vendor Assessment
### Vendor Security Due Diligence Report: "CognitiveAI Inc." (External LLM API Provider)

**Assessor:** Eduardo de Souza Marques · GRC & Third-Party Risk Specialist  
**Assessment Date:** October 20, 2026  
**Vendor Tier:** **Tier 1 (High Criticality / Confidential Data Processing)**  
**Target Engagement:** Real-time AI fraud detection and customer dispute processing API.

---

## 1. Vendor Profile & Engagement Scope

* **Vendor Name:** CognitiveAI Inc. (Delaware, USA).
* **Service Provided:** Hosted Large Language Model (LLM) API endpoints for automated transaction anomaly scoring.
* **Data Transmitted:** Anonymized transaction metadata, merchant category codes, user dispute text summaries.
* **Inherent Risk Classification:** **HIGH** (Vendor processes core transaction decision data and interfaces with customer-facing dispute flows).

---

## 2. Security Due Diligence Findings (Evidence Review)

| Assessment Area | Evidence Reviewed | Verification Procedure | Finding / Status |
|:---|:---|:---|:---:|
| **SOC 2 Type II Report** | Report dated August 2026 (Auditor: Ernst & Young) | Inspected scope (Security & Confidentiality). Reviewed testing of controls over customer data isolation and KMS encryption. | ✅ **Satisfactory** (Zero exceptions reported in testing period). |
| **Data Retention & AI Training** | Master Services Agreement (MSA) & Data Processing Addendum (DPA) | Verified presence of **Zero Data Retention (ZDR)** clause. Confirmed vendor does NOT retain customer prompts to train foundation models. | ✅ **Satisfactory** (Explicit contractual guarantee of zero model training). |
| **Data Encryption** | Architectural Whitepaper + TLS Certificate Audit | Inspected cryptographic standards for API ingress (TLS 1.3 enforced) and database storage (AES-256 with tenant-isolated KMS keys). | ✅ **Satisfactory** (A+ rating on SSL Labs; TLS 1.3 only). |
| **Business Continuity & SLA** | Business Continuity Plan (BCP) & Disaster Recovery Attestation | Verified Multi-AZ failover and 99.95% uptime SLA with financial service credit penalties for unexcused downtime. | ⚠️ **Medium Risk** (Vendor relies on single primary cloud region for inference). |
| **Vulnerability & Pentest** | Annual Third-Party Pentest Executive Summary | Reviewed summary report from Bishop Fox (conducted May 2026). All high/critical findings resolved. | ✅ **Satisfactory** (Zero outstanding critical vulnerabilities). |

---

## 3. Complementary User Entity Controls (CUEC) Review

Under SOC 2 Type II guidelines, vendor controls are only effective if the customer implements corresponding CUECs:

1. **Client-Side Pre-Filtering (CloudPay Responsibility):** CloudPay must filter and tokenize all direct cardholder data (PAN) and tax IDs prior to making API calls to CognitiveAI.
   * *Status at CloudPay:* **Implemented** via automated regex / Presidio tokenization middleware.
2. **API Key Security & Rotation:** CloudPay must securely store CognitiveAI API keys in AWS Secrets Manager and rotate every 90 days.
   * *Status at CloudPay:* **Implemented** with automated AWS Lambda rotation hook.

---

## 4. Final Risk Rating & Recommendation

```
========================================================================
FINAL TPRM ASSESSMENT VERDICT: [ APPROVED WITH CONDITIONS ]
Overall Vendor Risk Score: LOW-RESIDUAL (Inherent: HIGH)
Next Periodic Re-Assessment: October 2027 (Annual)
========================================================================
```

### Mandatory Conditions for Production Rollout:
1. **Network Egress Restriction:** Direct production API calls must be whitelisted only through CloudPay's designated NAT Gateway static IP addresses.
2. **Automated Health Fallback:** If CognitiveAI response latency exceeds 800ms or HTTP 5xx errors exceed 1%, CloudPay's payment engine must automatically failover to internal rules-based heuristics without interrupting checkout.
