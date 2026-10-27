# Shared PUI89 AI Core — Multimodal Screening adapter

**Status:** human-reviewed screening-workflow contract, not a validated narcotics detector or chemical-identification system.

## Shared contract

Use the existing standard-library autonomy lab, world-state tracker, uncertainty-aware interfaces, and reproducible report builder as Phase 1. Every modality must remain distinguishable in the evidence record; do not merge missing data into a confident fused result.

Each observation should include modality/sensor ID, timestamp, calibration/version where applicable, quality/confidence, provenance reference, missing/stale status, and data integrity status. Each decision record should capture input completeness, disagreement, uncertainty/abstention reason, review state, model/code version, configuration hash, and an audit-minimised evidence reference.

## Required tests

- One modality missing, all modalities missing, stale or malformed inputs.
- Conflicting modality outputs or different timestamps/calibration versions.
- Duplicate evidence, hash mismatch, out-of-range values, corrupted payload, or unknown modality.
- Confidence below threshold, out-of-distribution signal, or uncalibrated confidence.
- Missing reviewer reference or review timestamp.
- Reviewer rejects or overrides a proposal; audit trail records the disposition.
- Sensor/communications fault during simulated movement → safe hold/stop.
- Synthetic or unlabelled data supplied to a performance evaluator → refuse to report real-world accuracy.

## Expected behavior

Incomplete, stale, conflicting, or uncertain evidence must produce UNKNOWN, ABSTAIN, or REQUEST_HUMAN_REVIEW; it must not be silently imputed as a positive detection. An alert is a hypothesis, not proof of chemical identity or guilt. It must not automatically trigger search, seizure, detention, or enforcement. Ordinary RGB imagery cannot establish chemical identity or reliably reveal concealed contents.

## Evaluation gate

Use only lawful, authorised, appropriately licensed, expert-reviewed data. Split by source/session/device or other independent acquisition group to reduce leakage. Report per-class precision/recall, false-positive and false-negative rates, calibration, abstention, latency, and uncertainty with sample counts and limitations. Mark missing benchmarks NOT RUN; synthetic tests are workflow checks, not screening accuracy.

## Run order

1. Run python tools/pui89_master_verify.py.
2. Run existing unit and synthetic workflow tests.
3. Run missing/conflicting/stale/corrupted modality and human-review tests.
4. Only then evaluate a model with reviewed data and a frozen held-out test set.

**Cost and privacy:** no paid API, cloud GPU, automatic model download, or external upload is required by this contract. Minimise personal data and keep review records access-controlled.