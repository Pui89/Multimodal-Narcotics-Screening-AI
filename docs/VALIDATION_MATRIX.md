# Validation Matrix — Multimodal Narcotics Screening AI

Last reviewed: 18 October 2026. The current repository is a screening workflow prototype, not a validated narcotics detector or chemical analyser.

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

## Evaluation and governance rules

- Treat model confidence as a score unless calibration has been measured.
- Missing, conflicting or out-of-distribution input should lead to UNKNOWN/REVIEW, not an automatic positive decision.
- Do not claim substance identity from an ordinary image.
- Use only authorised datasets and record source, licence/permission, ground-truth basis, reviewer, split and hashes.
- Synthetic pipeline accuracy must never be presented as accuracy on real narcotics.
