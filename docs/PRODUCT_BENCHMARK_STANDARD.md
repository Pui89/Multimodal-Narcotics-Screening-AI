# Multimodal Narcotics Screening AI — Product Benchmark Standard

Company-wide benchmark rules: [PUI89 Product Quality and Benchmark Standard](https://github.com/Pui89/Pui89.github.io/blob/main/PRODUCT_QUALITY_AND_BENCHMARK_STANDARD.md).

## Scope and comparison discipline

Define a lawful, narrow screening-support task before choosing metrics. Compare only alternatives performing the same task on authorized, representative data with expert-reviewed ground truth. Candidate groups may include human review alone, a transparent simple baseline, and licence-compatible multimodal models or research systems where permitted data and reproducible tests exist. Record source, model version, licence, modality, runtime, tested/not tested and comparability limits.

**Appearance alone cannot establish chemical identity.** Do not claim that images prove a substance is a narcotic. If the project cannot obtain valid, lawful ground truth for its stated task, mark model performance “not yet measured”.

## Core metrics where an appropriate labeled task exists

- Sensitivity/recall, specificity, false-positive rate and false-negative rate.
- Precision/positive predictive value with the dataset prevalence disclosed.
- Confusion matrix and class-level/subgroup results where appropriate.
- Calibration only when a valid calibration protocol is run.
- Abstention coverage and error rate among accepted predictions.
- Human review time, disagreement, correction burden and escalation rate.
- Latency and resource use on named hardware.

## Fair protocol

Use authorized data, predefine labels and evaluation splits, prevent train/test leakage, fix thresholds on validation data, and evaluate once on held-out test data. Include negative and ambiguous cases. Document expert-review process, provenance, exclusions, sample count, and domain limitations. Report uncertainty and failures rather than a single unsupported accuracy number.

## Safety, legal and human-control boundary

This is not validated chemical identification and must not be marketed as such. Model outputs must not trigger autonomous enforcement, detention, accusation, or other consequential action. Qualified domain, legal, privacy and safety review is required before any operational use.

## Zero-spend constraint

Use only existing, authorized data and local/free tools. Do not acquire paid datasets, APIs, cloud compute, or hardware without explicit approval. Do not bypass data-access restrictions to obtain ground truth.
