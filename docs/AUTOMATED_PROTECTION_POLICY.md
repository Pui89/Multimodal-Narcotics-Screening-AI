# Document automated protection policy for screening

## Automated protection and fail-safe policy

This is the project's safety, privacy, and decision-control contract for software and future hardware integration. It is **not proof of a validated screening system**.

### Required automated checks
- Validate input format, sensor availability, calibration/health status, timestamps, and model-output schema. Missing, stale, corrupt, or conflicting inputs must trigger an abstention/hold, not a positive finding.
- Keep RGB object detection, segmentation, material/chemical sensing, and human review as distinct evidence sources. Do not infer chemical identity or concealed contents from ordinary RGB images alone.
- Require calibrated thresholds, documented uncertainty, and a validated evaluation set for each modality before operational use.
- On sensor failure, calibration drift, model error, disagreement between modalities, or a security/privacy fault, stop automated classification and request qualified human review.
- Never automatically accuse a person, deny access, initiate enforcement, or make another consequential decision based solely on a model alert.
- Record a minimal audit trail of model/version, sensor health, uncertainty, reason for abstention, and reviewer outcome; protect sensitive data and apply retention/access controls.

### Screening-specific boundaries
- A segmentation mask identifies visible image regions; it does not prove a hidden substance is present.
- Chemical claims require suitable, validated sensing hardware and reference methods, lawful test data, and qualified interpretation.
- Test for false positives/negatives across representative conditions and groups; measure calibration, sensitivity, specificity, latency, and abstention rate on held-out data.
- Physical safeguards and privacy/security controls must be reviewed before deployment. This repository does not establish real-world detection performance.

### Release gate
Automated alerts remain advisory until modality-specific validation and human review procedures are documented. Any critical sensor/model failure must fail closed to **no automated finding / human review**, not a presumed positive or presumed safe result.
