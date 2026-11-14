# Product brief — Multimodal Narcotics Screening AI

**Product direction:** A local-first screening-evidence review application, with a future mobile inspection-robot concept. The current implementation is a software prototype; it is not a validated narcotics detector, chemical-identification system, or operational screening robot.

## The operational problem

Authorized screening teams may need to review multiple kinds of evidence, sensor quality, conflicting observations and uncertainty. A useful tool must keep provenance visible, avoid overstating what an image can prove, preserve an `UNKNOWN` state when evidence is insufficient, and support accountable human review.

## What exists today

- A local API and dashboard prototype with manually entered example features and heuristic decision rules.
- Software regression tests and an evaluation runner that can check structured predictions and calculate metrics.
- Synthetic examples for checking the evaluation pipeline.
- Documentation for local-first deployment, data provenance, uncertainty, privacy and safety boundaries.

Uploaded images are preview-only; the current dashboard does not run a trained vision model on them. Synthetic scores are not real screening accuracy. No reliable chemical identification, validated multimodal fusion, or physical robot operation is established.

## Intended product workflow

1. Receive authorized observations from configured sensors or approved data sources.
2. Check timestamps, quality, calibration, missing modalities and provenance.
3. Present supported observations and anomalies without inferring chemical identity from appearance alone.
4. Record agreement, conflicts, uncertainty and the reason for an `UNKNOWN` outcome.
5. Present a screening hypothesis to an authorized reviewer.
6. Record the reviewer decision and an audit trail with suitable access controls.

A normal RGB photograph cannot reveal the contents of closed baggage or reliably identify a chemical. Baggage screening requires an appropriate authorized imaging system; chemical identity requires a validated analytical procedure. The AI must not independently accuse a person, initiate enforcement, or command a robot.

## Potential users and collaborators

Potential stakeholders include authorized airport or transport-screening teams, public-sector technology groups, security researchers, and robotics/system integrators. These are audiences for discovery and validation, not confirmed customers or endorsements.

## Product requirements before any operational pilot

- A narrowly defined lawful intended use and documented operating limits.
- Authorized data access, source/licence records, expert-reviewed labels and leakage-safe splits.
- A trained baseline evaluated on a frozen, independent and representative test set.
- Per-class precision/recall, confusion matrix, false-positive and false-negative rates, calibration, abstention coverage, latency, robustness and failure analysis.
- Privacy impact review, access controls, cybersecurity testing, audit-log policy and retention limits.
- Human-factors evaluation and written procedures that prevent an AI score from being treated as proof or an automatic enforcement trigger.
- Independent expert review, formal approvals and a controlled pilot plan before operational use.

## Deployment and cost direction

Prefer free/open-source tooling and local inference where practical. The current application can be run locally; cloud inference, paid subscriptions and hosted GPU services are not required by the documented prototype workflow. Actual local model integration, hardware needs and performance must be tested before they are claimed.

## Product milestones

- **Stage 1 — software reliability:** keep installation, API, dashboard and evaluation tests reproducible.
- **Stage 2 — data readiness:** secure lawful data, document annotation, and freeze group-separated splits.
- **Stage 3 — measured baseline:** train or integrate one bounded baseline and publish independently evaluated results and failure cases.
- **Stage 4 — controlled system validation:** test missing/conflicting modalities, uncertainty, security, privacy and human review.
- **Stage 5 — robotics feasibility:** separately validate sensors, navigation, safety controls and human supervision before any physical pilot.

These are development gates, not promised delivery dates. No product-readiness, detection-accuracy or customer-savings claim is made until supported by evidence.
