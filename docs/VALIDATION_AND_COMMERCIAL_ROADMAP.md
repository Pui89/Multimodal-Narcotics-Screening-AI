# Multimodal Narcotics Screening AI — validation and commercial roadmap

## Current baseline
The API/dashboard uses manually entered illustrative features and heuristic rules. Uploaded images are preview-only. The repository has metric utilities and a synthetic JSONL example, but the example does not measure a trained model or real screening performance. No chemical identification, validated X-ray/CT system or deployed robot is established by these components.

## Intended-use and data boundary
Choose one narrowly defined task before training. Ordinary RGB photos cannot reveal hidden contents inside closed baggage and cannot reliably establish chemical identity. Baggage screening requires appropriate authorized X-ray/CT equipment and legally usable data; chemical identity requires an authorized validated analytical procedure. AI output must remain a screening hypothesis, with UNKNOWN/abstention for insufficient or out-of-scope evidence. No autonomous enforcement decision is permitted.

## Dataset and annotation plan
- Obtain documented lawful access and confirm commercial/research reuse terms.
- Record source, licence/permission, modality, acquisition conditions, item/session/site grouping, dataset version and annotation protocol.
- Use qualified annotators and adjudication appropriate to the task; never assign chemical identity from visual appearance alone.
- Split by item, session or source to avoid leakage.
- Apply privacy, retention, access-control and evidence-handling requirements to sensitive data.
- Store restricted data and checkpoints outside Git unless redistribution is explicitly permitted.

## Training and evaluation gates
1. Establish a baseline for one modality/task with a compatible, licensed model.
2. Log commit, dataset checksum, split counts, annotation version, seed, configuration, hardware, package versions, training time and checkpoint checksum.
3. Freeze the test set before model selection is complete.
4. Generate actual model predictions on the held-out set and pass them to the existing evaluation runner.
5. Report per-class precision/recall/F1, confusion matrix, false-positive and false-negative counts, calibration, abstention coverage, robustness by acquisition condition, latency and memory.
6. Document out-of-distribution handling and sensor-missing/conflict cases. An anomaly score is not proof of narcotics.
7. Evaluate navigation and physical robot safety independently from screening performance; use simulation and deterministic safety controls before authorized hardware trials.

For genuine held-out predictions, run: python evaluation/run_evaluation.py path/to/real_test_predictions.jsonl --output reports/real-test-v1.json

Each JSONL row needs adjudicated y_true, the evaluated model's y_pred and meaningful confidence from 0 to 1. Keep the checked-in synthetic example labelled synthetic; never cite it as real model performance.

## Minimum benchmark report
Include intended use, dataset provenance/permissions, annotation/adjudication protocol, split strategy and counts, model/checkpoint checksum, code commit, thresholds, hardware/software, per-class metrics, confusion matrix, calibration, abstention, latency, failure analysis, limitations and reproduction commands.

## Product readiness
Potential early offer: research collaboration, evaluation tooling or a feasibility study with an authorized data/instrument partner. Do not market this as a validated narcotics detector or autonomous enforcement robot. Before deployment, require legal/regulatory review, independent validation, privacy/security controls, authorized human review, auditability and customer-agreed acceptance criteria.

## Zero-cost-first rule
Prefer local/open-source tooling and offline evaluation. Confirm model and dataset licences independently. Avoid paid APIs, hosted GPU subscriptions and automatic downloads unless explicitly approved.
