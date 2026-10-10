# End-to-End Multimodal Screening Workflow

## Status and scope

This is a simulation-first research application for authorized screening support. Outputs are evidence summaries and hypotheses for trained human review—not proof of chemical identity, a medical diagnosis, or grounds for automatic enforcement. The software workflow does not authorize robot movement or actuator commands.

## Run locally

From the repository root:

```bash
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python demo_end_to_end.py
pytest -q
```

If the optional dependencies or hardware are unavailable, continue with the documented synthetic/recorded-data workflow. Do not connect physical hardware until the relevant interfaces and safety controls have been independently tested.

## Workflow

```text
Recorded / simulated observations
            |
            v
Schema + provenance validation
            |
            v
Sensor quality + timestamp alignment
            |
            v
Perception hypotheses (not ground truth)
            |
            v
Multimodal evidence fusion
            |
            v
Open-set / OOD + uncertainty checks
            |
            v
UNKNOWN / ABSTAIN when evidence is insufficient
            |
            v
Human review and recorded disposition
            |
            v
Audit record + reproducibility metadata

Navigation (separate boundary):
LiDAR / depth / IMU -> map -> planner -> deterministic safety gate
                                               |
                                               v
                                      ROS 2 (optional)
```

## Expected safety behavior

- Reject malformed, stale, poorly synchronized, or low-quality observations.
- Record missing modalities as missing evidence; do not treat them as negative evidence.
- Preserve UNKNOWN/ABSTAIN when evidence is contradictory, outside the validated envelope, or insufficient.
- Keep screening hypotheses separate from chemical identification and consequential decisions.
- Require authorized human review and preserve an auditable record of reviewer disposition.
- Keep foundation-model output isolated from direct motor, cutter, manipulator, or other actuator control.

## Example development sequence

1. Run the synthetic demo and automated tests.
2. Inspect the emitted decision, uncertainty, missing-modality handling, and audit record.
3. Add versioned, lawfully collected and appropriately governed evaluation data.
4. Establish fixed train/validation/test splits and prevent subject, scene, or event leakage.
5. Evaluate calibration, unknown detection, modality ablations, sensor failures, and latency.
6. Only then consider optional simulator or ROS 2 integration, with independent safety review.

## Current limitations

A passing unit test confirms only the tested software invariant. It does not demonstrate chemical identification, detection accuracy, field reliability, fairness, or robot safety. Visual and multimodal observations alone cannot establish the chemical composition of a substance. Do not present synthetic examples or concept animations as measured benchmark results.
