# PUI89 Shared Engineering Standard — Multimodal Screening AI

**Purpose:** make development repeatable, low-cost, reviewable, and evidence-led. This document records a working standard; it does not claim new tests or real screening results have been run.

## Operating rules

1. **Free-first:** prefer open-source tools and GitHub Actions within available free quotas. Do not add paid APIs, hosted GPUs, subscriptions, or services that can incur charges without explicit approval.
2. **Inspect before changing:** reuse existing evaluation tools, input validation, manifests, and tests rather than creating duplicates.
3. **Small, reviewable changes:** isolate changes, add regression tests, and use a pull request when practical.
4. **Evidence over claims:** synthetic fixtures validate pipeline behavior only. They do not establish chemical identity, real screening accuracy, or wrongdoing.
5. **Reproducibility:** record dataset/version, modality availability, ground-truth basis, configuration, model identity, metrics, sample count, and failure cases.

## Project-specific priority: trustworthy modality evaluation

1. Define a narrow, lawful screening-assistance task with authorized data and qualified ground truth before collecting or evaluating real samples.
2. Audit permission, license, provenance, privacy, retention, and access controls for every data source.
3. Evaluate each modality separately before evaluating fusion; document missing, noisy, conflicting, or out-of-distribution inputs.
4. Test malformed inputs, missing sensors, sensor disagreement, uncertainty calibration, and safe fallback to human review.
5. Freeze source/item-aware evaluation splits before tuning and prevent different views of the same physical item from leaking across splits.
6. Report precision, recall, F1, calibration and error patterns only for the exact validated task and dataset. Clearly separate synthetic metrics from real-data results.
7. Treat an alert as a reason for an authorized human to follow an approved procedure—not proof that a person possesses a substance. Do not build automatic accusation, detention, or enforcement decisions from model scores.

## Shared quality gates

- Run the existing lightweight unit tests and CI workflow.
- Do not infer chemical detection capability from ordinary RGB, depth, or lidar sensors.
- Keep any optional chemical sensor interface separate until hardware, calibration, and validation are established.
- Minimize personal data and use privacy-preserving defaults.
- Record failures and limitations alongside successful results.

## Definition of done

A change is complete only when its code/docs are reviewed, relevant automated checks have actually run, the result is reported accurately, and any remaining limitation is explicit. If a check has not run, mark it **not verified**.

## Immediate next action

Use the existing validation matrix to establish the data and evaluation prerequisites, then strengthen modality-specific and missing-input regression tests. Do not present synthetic pipeline results as real screening performance.
