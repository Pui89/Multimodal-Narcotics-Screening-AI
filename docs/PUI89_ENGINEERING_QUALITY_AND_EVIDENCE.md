# PUI89 Engineering Quality and Evidence System — Multimodal Screening AI

**Reviewed:** 25 October 2026  
**Purpose:** a lightweight, free-first release gate shared across PUI89 projects. This is a process standard, not a claim of validated screening or chemical identification.

## Non-negotiable evidence rules

1. **No evidence, no claim.** Use *verified*, *failed*, *not measured*, or *blocked* with a named artifact, test, dataset/scenario, and date.
2. **Separate software, synthetic, model, sensor, and operational evidence.** Passing CI or segmenting visible pixels does not establish narcotics detection or chemical identity.
3. **Reproducibility before performance claims.** Record code revision, environment, command, authorised data provenance, label protocol, split method, sample count, metrics, failures, and report path.
4. **No fabricated numbers.** Synthetic fixture scores are workflow tests, not real screening performance.
5. **Free-first.** Prefer local tools and standard-library checks. Do not require paid APIs, hosted GPUs, subscriptions, or model downloads for basic checks. Warn before resource-heavy downloads.
6. **Safe, reversible workflow.** Work on a branch and open a reviewable pull request. Do not auto-merge or silently modify the default branch.
7. **Human review and due process.** An AI alert is not proof of narcotics or wrongdoing. No autonomous accusation, detention, search, seizure, or enforcement action.

## Project release gates

| Gate | Required evidence | Current status |
|---|---|---|
| Input integrity | Missing, malformed, stale, low-quality and non-finite inputs are rejected or explicitly marked invalid | **Verify coverage with named tests** |
| Modality availability/conflict | Each modality has independent quality/status; missing or conflicting inputs are not silently treated as agreement | **Verify end-to-end behavior** |
| Uncertainty and abstention | Insufficient or out-of-scope evidence can produce UNKNOWN and human review | **Must be demonstrated per path** |
| Data governance | Lawful provenance, license/permission, expert labels, privacy controls and traceable exclusions | **Required before real-data evaluation** |
| Valid evaluation | Frozen representative holdout with group-aware splits; false positives/negatives, abstention, calibration and uncertainty where appropriate | **No validated real-world narcotics benchmark established** |
| Chemical identity | Independent validated chemical-sensor/analytical evidence; image segmentation alone is insufficient | **Not established** |
| Consequential workflow | Authorised human review, recorded rationale, audit trail and no automatic enforcement | Policy requirement; verify software and procedure separately |
| Physical capability | Instrumented inspection-robot trials and independent safety review | **Not validated** |

## Standard evidence record

For each meaningful test or experiment, record:

- **ID / requirement:** stable identifier and expected behavior.
- **Revision and environment:** commit SHA, OS, dependencies and hardware if relevant.
- **Command and inputs:** exact command, authorised data source/permission, label protocol, split version and modality availability.
- **Result:** pass/fail/blocked/not measured; actual counts and metrics only when observed.
- **Failures and uncertainty:** false positives/negatives, abstentions, conflicts, missing modalities and out-of-scope cases.
- **Artifact:** durable report path or CI run URL.
- **Limitations and next action:** what the result does not establish.

## Operating loop

1. Select a requirement from [the engineering assurance plan](ENGINEERING_ASSURANCE_PLAN.md) and [reproducible benchmark plan](REPRODUCIBLE_BENCHMARKS.md).
2. Make the smallest safe change on a dedicated branch.
3. Run targeted tests for missing/stale/conflicting inputs and UNKNOWN handling first; then the regression suite when feasible.
4. Inspect logs and reports. A passing synthetic test does not establish real-world detection.
5. Update the evidence matrix with observed results and limitations.
6. Open a pull request with scope, commands run, results, and unrun checks; review before merging.

## Immediate priority

Add or strengthen deterministic tests for missing, stale, malformed and conflicting modality inputs; ensure insufficient evidence can remain UNKNOWN; verify that a human review is required before consequential action. Use only lawfully obtained, privacy-appropriate, expert-labelled data for any real-data evaluation.

## Completion criteria

This system is operational only when a reviewer can trace **requirement → implementation → test → observed result → artifact → limitation**. This document does not validate a narcotics detector, prove chemical identity, or certify a physical robot.
