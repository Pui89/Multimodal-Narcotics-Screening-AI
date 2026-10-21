# Engineering Assurance and Verification Plan

**Status:** engineering process document for a screening-workflow research prototype.  
**Basis:** project-defined engineering assurance practices for requirements traceability, hazard tracking, verification, validation, and evidence-based release decisions.

## 1. Purpose and system boundary

This plan defines traceable requirements, hazards, verification evidence, and release gates for the screening workflow and proposed robotic screening concept.

**Current scope:** local workflow, API/dashboard, evaluation utilities, provenance/split tools, and synthetic evaluation fixtures. Dashboard values may be manually entered; image preview is not evidence of a trained-model prediction.  
**Not established:** representative real-data accuracy, reliable substance identification, validated sensor fusion, chemical identity, or a validated physical screening robot.

A model score or visual similarity is a screening hypothesis, not proof of a substance. AI must not independently trigger enforcement, search, seizure, or other consequential action.

## 2. Requirements and verification matrix

| ID | Requirement | Verification | Acceptance evidence | Current status |
|---|---|---|---|---|
| MS-REQ-001 | Missing, malformed, non-finite, or out-of-range values are rejected or marked invalid. | Unit/regression tests | Tests cover types, boundaries, missing fields, and invalid confidence/sensor values. | Must be confirmed by CI. |
| MS-REQ-002 | Missing/conflicting modalities are not silently treated as agreeing evidence. | Unit/scenario tests | Availability and quality are tracked; conflicts trigger uncertainty/review. | Intended policy; verify each path. |
| MS-REQ-003 | Insufficient or out-of-scope evidence can produce UNKNOWN/abstain. | Evaluation/workflow tests | Low-quality, conflicting, unsupported inputs are not forced into a class. | Verify current implementation. |
| MS-REQ-004 | Synthetic scores are separated from real screening performance. | Report/README audit | Data type is stated; synthetic fixtures are never presented as real accuracy. | Ongoing control. |
| MS-REQ-005 | Real-data evaluation uses authorised, expert-reviewed labels and independent group-aware splits. | Data audit/benchmark rerun | Provenance, permission/licence, label protocol, group key, split version recorded. | Representative real-data benchmark not established. |
| MS-REQ-006 | Reports include false positives/negatives, calibration, abstention, and limitations where data permits. | Independent report review | Reproducible metrics and explicit limitations. | Real-world benchmark not established. |
| MS-REQ-007 | Consequential outcomes require authorised human decision and auditable review. | Workflow/procedure tests | Reviewer, decision, evidence, and unresolved uncertainty recorded. | Intended policy; verify end-to-end. |

## 3. Initial hazard log

| Hazard | Potential consequence | Required control before operational use |
|---|---|---|
| False positive hypothesis | Unjustified search, delay, stigma, or enforcement | Independent validation, threshold analysis, human review and correction process |
| False negative | Contraband missed or unsafe reliance | Held-out evaluation, failure analysis, explicit scope limits |
| RGB image mistaken for chemical evidence | Unsupported substance identity claim | State sensor limits; use validated authorised analytical instruments where required |
| Missing/conflicting sensor data | Overconfident fusion | Modality-quality checks, uncertainty propagation, abstain to UNKNOWN |
| Biased sample or data leakage | Misleading performance claims | Group-aware split, provenance audit, representative sampling and subgroup analysis |
| Sensitive data exposure | Privacy/security harm | Data minimisation, access controls, retention policy, local-first processing |
| AI score used alone for enforcement | Unjustified consequential action | Prohibit AI-only decisions; require authorised human review and audit trail |

This initial hazard log is not a completed formal safety, legal, or privacy assessment. Obtain qualified domain, legal, privacy, and operational review before a pilot.

## 4. Verification, validation, and release gates

1. **Software:** tests cover invalid inputs, missing modalities, confidence boundaries, abstention, and audit logging.
2. **Data:** intended use is narrow; data is authorised/licensed; labels are expert-reviewed; group-aware splits and provenance are documented.
3. **Baseline:** evaluate each available modality independently before fusion. Compare fusion only when modalities are genuinely aligned and lawful to use.
4. **Performance:** report per-class precision/recall, confusion matrix, false-positive/false-negative rates, calibration, abstention coverage, latency, and failures on independent held-out data.
5. **Robustness:** test missing/stale/conflicting modalities, distribution shift, image quality, sensor failure, and ambiguous cases.
6. **Human review:** test UNKNOWN, escalation, reviewer override, audit trail, privacy, and non-discrimination safeguards.
7. **Operational:** no deployment/enforcement use without independent expert validation, legal authorisation, privacy/security review, and supervised pilot approval.

Verification checks requirements; validation checks suitability for intended use. Synthetic CI passing does not establish narcotics-identification accuracy or chemical identity.

## 5. Evidence and change control

Record commit, environment, command, dataset/model version, seed, metric definitions, raw output, and limitations for each result. Keep sensitive datasets and weights out of Git unless rights and policy explicitly allow them. Safety- or decision-related changes require tests and human review.

## 6. Cost and licensing

Prefer local execution and free/open-source tools. Check dependency and dataset licences. Do not add paid APIs, hosted inference, cloud GPUs, subscriptions, or billing-triggering workflows without explicit approval.

## 7. Review boundary

This project-level plan supports disciplined engineering and evidence tracking. It does not replace independent safety, legal, privacy, domain-expert, or operational review.