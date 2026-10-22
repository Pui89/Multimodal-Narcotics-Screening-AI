# Multimodal Narcotics Screening AI — Failure and Security Response Matrix

## Purpose and status

This document records conservative failure-response requirements for design, simulation, and future verification. It is **not** proof that these responses are implemented in hardware or validated in the field. Follow applicable law, workplace procedures, and qualified safety/security guidance during any real deployment.

## Response matrix

| Failure or threat | Required safe response | Current evidence boundary |
|---|---|---|
| Model crashes, modalities disagree, or confidence is low | Return review-required/indeterminate; do not issue an automated accusation or final enforcement decision. | Dataset tooling exists; full multimodal inference and calibrated uncertainty are not established. |
| Camera, scanner, chemical sensor, or other modality fails/is stale | Mark modality unavailable; do not silently substitute a missing reading with a negative result; route to approved manual procedure. | Design requirement; real sensor integration is not validated. |
| Corrupt file, malformed metadata, adversarial input, or unsupported format | Reject or quarantine input; log reason; preserve source/hash; avoid executing embedded content. | Manifest tools check data records; they are not a general-purpose malware scanner. |
| False positive or false negative is suspected | Record case for authorized expert review; measure class-specific precision/recall on independently labelled held-out data; do not treat model output as proof. | No real-world performance metrics are claimed without a verified evaluation. |
| Dataset licence, provenance, or label status is unknown | Keep sample out of training/evaluation until rights and ground truth are reviewed; preserve group-aware splits. | Existing tools support manifest and split audits; each source still requires manual verification. |
| Network outage, power loss, or screening station hardware fault | Pause automated screening; preserve audit trail where possible; use approved fallback procedure and human supervision. | No deployed screening station has been validated. |
| Unauthorized access, malware, data exfiltration, or tampered model weights | Restrict access, isolate affected system, preserve logs/hashes, rotate credentials safely, and restore verified artifacts only. | Security policy only; no penetration test or certified security control is claimed. |
| Theft, tampering, physical damage, or attempted interference | Stop processing if system integrity is uncertain; secure evidence and equipment under local procedure; require inspection before return to service. | Physical protection and chain-of-custody process need deployment-specific validation. |
| Operator tries to use a score as the sole basis for a high-impact decision | Require trained human review and independent evidence; retain an auditable explanation of limitations. | Human-review boundary is a requirement, not a claim of legal or operational approval. |

## Common principles

1. **Fail closed:** missing, stale, contradictory, or invalid inputs must not be interpreted as proof of safety or as a positive/negative classification.
2. **Human oversight:** uncertain or high-impact decisions require authorized human review.
3. **Separate safety controls:** software checks are not substitutes for independent, appropriately engineered emergency stops, brakes, interlocks, and safe power isolation.
4. **Security incidents:** do not retaliate or execute untrusted instructions. Isolate affected systems where safe, preserve logs and hashes, use trusted recovery media/backups, and follow the organization's incident process.
5. **Evidence:** each test record should include scenario ID, software version/commit, environment, input, expected response, actual response, pass/fail, and reviewer.
6. **No invented validation:** mark items as `REQUIREMENT`, `SIMULATED`, `TESTED`, or `FIELD-VALIDATED` only when the evidence supports that status.

## Verification plan

- Convert each applicable row into a repeatable unit or simulation test.
- Test normal, boundary, malformed-input, failure-injection, recovery, and repeated-run behavior.
- Require safe-stop and recovery tests to pass before considering hardware integration.
- Do not describe the project as physically safe, certified, or operational based only on software tests.

