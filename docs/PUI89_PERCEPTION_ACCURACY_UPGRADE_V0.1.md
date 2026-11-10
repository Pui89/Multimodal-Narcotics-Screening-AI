# Sentinel Multimodal Screening — Perception Accuracy Upgrade v0.1

**Status:** Requirements specified; no new screening model, X-ray equipment, chemical sensor or operational capability is validated.

Shared contract: [PUI89 Perception and Accuracy Standard](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/perception/PUI89_PERCEPTION_AND_ACCURACY_STANDARD_V0.1.md).

## Priority perception tasks

1. RGB object detection and instance segmentation with localization and image-quality assessment.
2. X-ray object detection/segmentation only for legally accessible, correctly licensed data and suitable real equipment.
3. Explicit overlapping-object, partial-occlusion and ambiguous-shape labels.
4. Scan quality detection: blur, saturation, clipping, incomplete field of view, low resolution and acquisition anomalies.
5. Preserve modality-specific evidence; do not silently merge RGB and X-ray scores.
6. Cross-modal alignment only when the records refer to the same item, time and acquisition context.
7. Report disagreement between modalities as a conflict requiring review.
8. Chemical-sensor interpretation only when sensor type, calibration, units, limits of detection, sample conditions and reference standards are recorded.
9. Maintain provenance, operator review, model/checkpoint version and audit trail for every result.

## Evaluation

Report per-class precision/recall, detection AP at declared IoU, mask IoU, overlap-stratified recall, image-quality rejection rate, calibration quality, false-alarm rate and human-review overturn rate. Use separate test sets by scanner/device/site where possible. Do not compare incompatible scanner domains as if interchangeable.

## Dataset and governance controls

Separate research-only, academic-only, non-commercial, synthetic and commercially reusable datasets. Record exact licence and version, attribution, source, checksum and intended-use permissions. A public download is not automatic commercial permission. Do not publish sensitive screening images or personal data.

**Safety boundary:** outputs are decision-support flags for trained human review only. No autonomous enforcement, accusation, search, seizure or adverse decision is permitted.
