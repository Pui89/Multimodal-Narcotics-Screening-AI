# Multimodal Screening AI — Product Readiness and Evidence Gates

## Intended role
A human-reviewed inspection workflow that organises visible-item observations and, only when separately supported, sensor-specific evidence. This repository does not demonstrate a validated narcotics detector.

## Keep sensing claims separate
- **RGB images:** may support visible-object or packaging classification; cannot establish concealed contents or chemical identity.
- **X-ray:** research datasets may depict prohibited objects but do not automatically represent narcotics. Verify licence, intended use and commercial restrictions.
- **Chemical sensors / spectroscopy:** require appropriate calibrated hardware, reference standards, controlled validation and specialist oversight. Do not infer chemical composition from ordinary imagery.
- **Multimodal fusion:** record each modality's availability, timestamp, calibration status, model/version and confidence; missing or contradictory sensors must lower confidence or trigger abstention.

## Data source and licence register
For every dataset/image, record source URL, licence and terms, attribution, commercial-use permission, subject/task fit, collection context, checksum, annotation schema and split group. Verify terms at source before use.
- Open Images can be considered for visible objects only after checking each image's licence and attribution requirements.
- OPIXray and HiXray are X-ray prohibited-object datasets with academic-use limitations; do not use them in a commercial product unless the rights holder's terms explicitly permit the intended use.
- Pill images are not a narcotics dataset. Do not label pills, powders or packages as illicit drugs without verified ground truth and lawful provenance.
- No unverified dataset should be presented as training-ready. Do not download data automatically.

## Evaluation protocol
Use source/session/device-separated test data. Report per-class precision/recall, false-positive rate, calibration, abstention coverage, confusion matrix and latency. For any high-impact alert, prioritise false-positive analysis and human-review workflow; no automatic accusation, enforcement or adverse decision is supported.

## Reliability tests
Test corrupt images, empty inputs, unsupported modality, low-confidence results, out-of-distribution samples, contradictory sensor outputs, stale calibration, missing metadata and unavailable model weights. Fail safely and preserve audit logs without exposing unnecessary personal data.

## Release gates
1. Rights and ground truth approved.
2. Baseline benchmark reproducible with versioned data manifest.
3. Human review and appeal/correction workflow demonstrated.
4. Sensor-specific validation and legal/privacy review completed.
5. Commercial-use rights and operating limitations documented.

## Commercial boundary
A potentially credible initial product is an evidence-management and visible-item inspection assistant. Do not market it as detecting concealed narcotics or identifying chemical substances until the appropriate sensor, dataset, independent validation and legal approvals exist.