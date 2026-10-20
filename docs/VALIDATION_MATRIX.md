# Validation Matrix — Multimodal Narcotics Screening AI

Last reviewed: 20 October 2026. The current repository is a screening workflow prototype, not a validated narcotics detector or chemical analyser.

## Latest automated evidence

The latest main-branch CI run [39276822504](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/39276822504) passed regression jobs on Python 3.10, 3.11 and 3.12. The workflow checked API/evaluation tests, dataset provenance and split/path-safety safeguards, and a synthetic evaluation smoke test. Synthetic tests are not evidence of real narcotics-screening accuracy.

| Capability | Repository evidence | Current status | What is still required |
|---|---|---|---|
| Local API/dashboard workflow | `apps/pui89_app/` | Software prototype; API regression tests passed in CI | Test the intended deployment environment and access controls |
| Synthetic evaluation pipeline | `evaluation/` | Reproducible synthetic tests passed in CI; synthetic scores are not real-world performance | Independently labelled, task-appropriate test set and pre-registered evaluation |
| Dataset provenance and image inventory | `tools/`, `data/manifest.template.csv` | Local tools; regression tests passed in CI | Verify source rights, metadata, labels and item-level provenance |
| Group-aware data splitting | `tools/group_split_manifest.py` | Rejects unapproved licences and unverified labels; regression tests passed in CI | Establish groups by physical item/source/capture session; prevent duplicates across splits |
| Prescription-pill image workflow | C3PI source guidance | Possible proxy task only after licence/terms review | Define narrow pill-image task; do not describe it as illicit-drug detection |
| Real narcotics classification | No validated real-narcotics checkpoint or benchmark established | **Not validated** | Authorised dataset, qualified ground truth and independent evaluation |
| Chemical identification | No chemical sensor/confirmatory analysis in this repository | **Not implemented/validated** | Appropriate laboratory or authorised confirmatory method; image appearance is insufficient |
| X-ray/CT/thermal or robotic sensors | Architecture interfaces only unless separately implemented and tested | **Not validated** | Actual supported sensor, calibrated data, validated modality-specific model and integration tests |
| Operational screening decisions | Human-review workflow is the intended boundary | **No autonomous enforcement decision** | Qualified operator review, privacy controls, documented intended-use and error analysis |

## Immediate zero-cost next actions

Work in this order and keep screening hypotheses separate from substance identification or enforcement decisions.

1. **Define the narrow task:** document intended use, authorised operator, prohibited use, permitted data sources and what the system is not allowed to infer.
2. **Verify data provenance:** audit every dataset's licence/permission, source, label meaning, ground-truth basis and hashes. Prescription-pill images are not proof of illicit-narcotics detection; ordinary RGB images cannot establish chemical identity.
3. **Prevent leakage:** group by physical item, source, subject or capture session as appropriate; detect duplicates and near-duplicates before splitting. Keep sensitive or unlicensed data out of Git.
4. **Test safe abstention:** missing, conflicting, low-quality or out-of-distribution inputs must yield `UNKNOWN`/`HUMAN_REVIEW`, not an automatic positive or negative finding.
5. **Evaluate only on appropriate held-out data:** report per-class precision/recall, confusion matrix, false positives/negatives, calibration, abstention rate, latency and failure cases. Mark experiments **NOT RUN** until actually executed.
6. **No-cost boundary:** run existing local tests and tools first. Do not enable paid APIs, cloud GPUs, hosted inference or subscriptions. If a future step may incur a charge, stop and ask first.

**Next milestone:** a lawful, independently reviewed evaluation set and a reproducible baseline report—not a claim of validated narcotics identification.

## Evaluation and governance rules

- Treat model confidence as a score unless calibration has been measured.
- Missing, conflicting or out-of-distribution input should lead to UNKNOWN/REVIEW, not an automatic positive decision.
- Do not claim substance identity from an ordinary image.
- Use only authorised datasets and record source, licence/permission, ground-truth basis, reviewer, split and hashes.
- Synthetic pipeline accuracy must never be presented as accuracy on real narcotics.
