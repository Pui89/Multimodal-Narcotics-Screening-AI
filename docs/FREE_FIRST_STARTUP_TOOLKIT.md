# Free-First Product and Engineering Toolkit

This project is built free-first and evidence-first. Use local checks and synthetic test fixtures before considering larger models, sensor stacks, hosted APIs or paid services.

## Recommended workflow

1. **Specify each modality:** document sensor type, calibration, timestamp, data quality, permitted use, provenance and known failure modes.
2. **Run the local preflight:** `python tools/pui89_master_verify.py`. It performs lightweight checks and inventories available project gates; it does not prove detection capability.
3. **Test data handling:** include missing modalities, corrupt inputs, time misalignment, low quality, out-of-distribution samples and uncertain outputs.
4. **Evaluate only with lawful, suitable data:** maintain separated train/validation/test sources and document ground-truth quality. Synthetic scenarios validate workflow behaviour only.
5. **Plan customer discovery:** ask prospective users about throughput, false-alarm tolerance, auditability, privacy, operator review and integration constraints before claiming product fit.

## Free-first tool choices

| Need | First choice | Guardrail |
|---|---|---|
| Versioning and reviews | GitHub issues and pull requests | Keep changes auditable |
| Continuous checks | Existing GitHub Actions workflows | Keep permissions read-only unless a job needs more |
| Local preflight | Python standard library and existing tests | Avoid silent package/model downloads |
| Data quality | Existing inventory and benchmark-validation tools | Track provenance, missing data and uncertainty |
| Reporting | Versioned JSON/Markdown benchmark reports | State dataset size, limitations and failure cases |
| Product page | GitHub Pages or existing site | Do not publish sensitive operational details |

## Cost, privacy and evidence rules

- No paid API, cloud GPU, subscription, or automatic model download is required by this guide.
- Do not upload sensitive screening data to third-party services without authorisation and a data-protection review.
- An RGB image or AI confidence score alone is not chemical identification or proof that a substance is narcotics.
- Distinguish synthetic workflow tests, benchmark results, controlled sensor experiments and real-world validation.
- Require human review and documented escalation for uncertain or high-impact decisions.

## Definition of done for each upgrade

Record the intended use, data source and permission, test protocol, metrics, failures, uncertainty and limits. A green CI run is evidence of software checks only, not proof of screening accuracy or operational suitability.
