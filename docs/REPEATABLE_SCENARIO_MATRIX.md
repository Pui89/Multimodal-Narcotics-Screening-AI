# Repeatable Scenario Matrix — Multimodal Narcotics Screening AI

This is a test-design document, not evidence that any chemical sensor or screening model is validated. Ordinary RGB imagery alone cannot establish chemical identity.

| Scenario ID | Input condition | Fault or ambiguity | Required behavior | Record |
|---|---|---|---|---|
| NS-01 | Baseline licensed sample | None | Report only what the configured sensor actually measures | Per-class counts, calibration |
| NS-02 | Benign lookalike | Visual ambiguity | Preserve uncertainty; do not label as confirmed substance | False-positive outcome |
| NS-03 | Missing modality | One sensor unavailable | Mark partial evidence and request review | Missing-modality handling |
| NS-04 | Conflicting modalities | Sensors disagree | Abstain/escalate; never silently choose the most alarming output | Conflict flags, review outcome |
| NS-05 | Calibration drift | Reference check out of tolerance | Block or qualify result until recalibrated | Drift magnitude, block behavior |
| NS-06 | Out-of-distribution sample | Unseen material or packaging | Flag out-of-distribution or uncertain | OOD status, errors |
| NS-07 | Low signal quality | Occlusion/noise/poor scan | Request rescan or human review | Quality score and response |
| NS-08 | Threshold boundary | Near decision threshold | Report threshold and uncertainty; avoid binary certainty language | Scores, threshold, calibration |
| NS-09 | Benign environmental interferent | Sensor cross-sensitivity | Flag limitations and route to review | Interferent-specific error |
| NS-10 | Human-review disagreement | Reviewer rejects model suggestion | Preserve audit trail and allow correction | Model output, reviewer decision |

## Required report fields
Scenario ID, sensor model and physical quantity, calibration status, sample provenance/licence, software commit, model/checkpoint hash, threshold, confusion matrix, per-class false-positive/false-negative rates, uncertainty/calibration method, reviewer outcome, raw-log location and limitations.

Use lawful, appropriately governed samples and datasets. Do not infer the presence of a substance in a person or item from appearance alone. Any consequential result requires trained human review and a validated sensing method.
