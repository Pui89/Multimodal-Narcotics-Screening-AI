# Product Quality and Safety Roadmap — Multimodal-Narcotics-Screening-AI

**Status:** development roadmap, not a safety certification, compliance claim or proof of validated real-world performance.

## Project-specific safety focus

mobile screening assistant, sensor/modality quality and calibration, privacy, human review and safe movement around people; no validated chemical identification.

**Required conservative behavior:** No automated search, detention, seizure or enforcement; incomplete, stale, conflicting, corrupted or uncertain modalities must yield UNKNOWN / ABSTAIN / REQUEST REVIEW.


## Cross-project quality gates

1. **Requirements and hazard analysis:** define intended use, prohibited use, users, operating environment, measurable acceptance criteria, foreseeable misuse, hazards, emergency procedures and stop-work authority with qualified domain experts.
2. **Fail-safe software:** test missing, stale, conflicting, malformed, out-of-range and low-confidence inputs; communications loss; emergency stop requests; restart/power loss; safe hold; manual override; bounded logging; and recovery from faults. Never silently guess missing safety data.
3. **Reproducible evidence:** record exact commit, environment, configuration hash, test/scenario ID, expected and observed outcome, failure codes, latency where measured, reviewer and NOT RUN items. Keep synthetic, simulation, lab and field evidence separate.
4. **Independent evaluation:** freeze a lawful, licensed, human-reviewed, leakage-safe held-out dataset or scenario set before testing. Publish sample counts, class-wise performance, false positives/negatives, uncertainty and limitations. Never copy literature metrics as project results or infer results from tool presence.
5. **Physical validation:** before people-at-risk testing, require a documented risk assessment, qualified engineering review, staged tests, emergency/recovery plan, incident log, and signed acceptance criteria for the exact hardware/software configuration.
6. **Cybersecurity and privacy:** least privilege, no secrets in Git, dependency/vulnerability review, controlled updates and rollback, data minimisation, access controls, retention/deletion rules and incident response.
7. **Maintainability:** document calibration/pre-use checks, operating limits, wear parts, maintenance intervals, fault codes, operator training, spares, warranty/support assumptions and safe decommissioning.
8. **Commercial release gate:** no buyer-facing safety, accuracy, autonomy, lives-saved, reach, chemical-identification or rescue-capability claim without independent evidence for the released configuration. Include limitations and known failure modes.

## Standards and external review

Use [ISO 12100](https://www.iso.org/standard/51528.html) as a general machinery risk-assessment starting point where applicable and the [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) for AI risk-lifecycle practices. [ISO 10218-1:2025](https://www.iso.org/standard/73933.html) and [ISO 10218-2:2025](https://www.iso.org/standard/73934.html) address industrial robots and industrial robot applications; applicability to each PUI89 mobile, agricultural, rescue or public-facing concept must be determined by qualified specialists. Referencing a standard is not compliance or certification. Check relevant Thai and target-market laws and standards before any pilot or sale.

## Customer/buyer evidence pack

Before a pilot, prepare: intended-use statement; operating envelope; risk register and residual risks; test plan/results including failures; dataset/model/sensor provenance; hardware/software bill of materials; cybersecurity/privacy notes; installation/site requirements; operator training; maintenance/support plan; incident and rollback procedure; and clear exclusions. A polished README or simulation pass alone is not product readiness.

## Free-first policy

Prefer offline, standard-library checks and synthetic tests first. No paid API, recurring service, automatic model download, external data upload or hardware actuation is required by this roadmap. Review licences, privacy, hardware fit, maintenance cost and safety impact before adding any tool or dependency.

## Screening evidence integrity and operational safeguards

**Current status:** requirements below are design gates. Unless a specific implementation and test are linked, treat each control as **NOT VERIFIED**. This section does not establish sensor performance, legal compliance or operational readiness.

1. **Keep evidence streams separate.** Record each configured modality independently with sensor/device identity, physical quantity measured, acquisition time and timezone, calibration status/version, quality flags, units/range, provenance reference and integrity result. Do not combine incompatible units, acquisition sessions, calibration states or evidence types.
2. **Protect the evidence chain.** Preserve the original authorised input as read-only where lawful; record cryptographic hashes, transformations, software/model/configuration versions and operator actions. A hash proves file consistency after hashing, not that the source is authentic or the contents are true. Missing provenance, failed integrity checks or unexplained edits must block a screening conclusion and request review.
3. **Validate sensor health before interpretation.** Define modality-specific pre-use checks, calibration intervals, reference materials, drift limits, known interferents, saturation/range checks and fault codes with qualified instrument specialists. Out-of-calibration, expired, damaged or self-test-failed sensors must be marked INVALID/UNAVAILABLE; never compensate by increasing another modality's confidence.
4. **Test spoofing and environmental interference.** Include documented synthetic or controlled tests for replayed/duplicated inputs, substituted device IDs, timestamp manipulation, corrupted files, glare/occlusion, packaging and benign lookalikes, environmental interference and deliberate sensor obstruction. Clearly separate simulated threat tests from tests on real instruments.
5. **Prevent automation bias.** Present neutral evidence summaries, uncertainty, missing data and known limitations before any recommendation. Keep the human reviewer responsible for the decision; record reviewer identity/reference, time, rationale and any override. Provide a way to correct or contest an erroneous record. Do not make a model score the default or sole basis for escalation.
6. **Evaluate errors by class and operating condition.** Before any performance claim, freeze a lawful, licensed, independently acquired held-out dataset with documented ground truth and leakage controls. Report per-class sample counts, false-positive and false-negative counts/rates, precision, recall, calibration, abstention and confidence intervals where statistically appropriate. Analyse relevant device, site, packaging and environmental variation; do not infer fairness or generalisation from an underpowered subgroup.
7. **Control thresholds and updates.** Version and justify decision thresholds; log changes and evaluate them against the same frozen protocol. Model, firmware, sensor, calibration or preprocessing changes require impact assessment and regression testing before use. No silent online learning or automatic threshold adaptation in an operational workflow.
8. **Minimise and govern personal data.** Collect item/equipment evidence only where lawful and necessary. Do not identify, track, profile or score people. Define purpose limitation, access roles, encryption, retention/deletion, export controls, audit access and breach response before any real-data pilot. Keep sensitive images and case details out of public issues, logs and test fixtures.
9. **Separate alert from action.** The only permitted software outcome is a neutral review prompt or an explicit no-alert/unknown state within the approved workflow. No automated accusation, search, detention, seizure, denial of access or enforcement. An authorised human must follow applicable law and independent procedures; an AI result is not proof.
10. **Record evidence gaps honestly.** Each evaluation report must list NOT RUN, NOT AVAILABLE, NOT CALIBRATED and NOT VALIDATED items, failed cases, exclusions, dataset limitations and reviewer sign-off. Synthetic workflow tests must never be counted as substance-detection accuracy.

**Release stop condition:** if provenance, sensor health, calibration, authorisation, audit integrity or required human review cannot be established, the system must abstain and the affected screening workflow must not issue a positive/negative substance conclusion.

