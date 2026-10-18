# Commercial and award-readiness roadmap — Multimodal Narcotics Screening AI

**Updated:** 18 October 2026  
**Stage:** local screening-workflow prototype and synthetic evaluation tests; not a validated narcotics detector or chemical analyser.

## Product goal
Build an auditable, human-supervised research application that checks authorized sensor inputs, records uncertainty and routes insufficient or conflicting evidence to UNKNOWN and qualified human review. A visual score is not proof of chemical identity and must never independently trigger enforcement action.

## Evidence already recorded
- Python CI passed on Python 3.10, 3.11 and 3.12: https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/39096448541
- Local API/dashboard, evaluation utilities, synthetic fixtures, provenance/manifest tools, group-aware splitting and uncertainty/human-review documentation are present.
- The documented dashboard uses manually entered sample values; image preview is not a trained image detector.

## Not yet proven
- A lawful, representative, expert-labelled dataset for a narrowly defined intended use.
- Independent held-out performance, calibration, false-positive/negative rates or multimodal benefit.
- Chemical identification from ordinary images, deployment-ready sensor fusion or a validated physical screening robot.
- Commercial demand, certification or competitive superiority.

## Product ladder
1. **Workflow demo:** synthetic examples clearly marked as synthetic; data-quality checks, audit trail, abstention and reviewer workflow.
2. **Evaluation package:** documented intended use, authorized data, independent ground truth, source-separated splits, baseline metrics and error analysis.
3. **Multimodal research prototype:** compare modalities only when lawful, aligned, representative measurements exist; document missing sensors and contradictions.
4. **Independent expert review:** privacy, bias, security, legal basis, human factors and confirmatory testing reviewed before a pilot.
5. **Controlled pilot:** only with formal authorization, secure data handling, expert oversight and validated procedures.

## Immediate priorities
- [ ] Define a narrow lawful task and what the system is and is not allowed to infer.
- [ ] Check licences, permissions, provenance, consent where applicable, class definitions and expert ground truth.
- [ ] Do not treat pharmaceutical pill-image datasets as illicit-narcotics evidence.
- [ ] Test malformed, missing, noisy, conflicting and out-of-distribution inputs; insufficient evidence must return UNKNOWN.
- [ ] Build source-separated and item/group-separated splits to prevent leakage.
- [ ] Compare unimodal baselines with fusion only when aligned real data exist.
- [ ] Report per-class precision/recall, confusion matrix, false-positive/negative rates, calibration, abstention and failure examples.
- [ ] Prevent AI outputs from independently triggering accusation, search, detention or other consequential enforcement action.

## Minimum acceptance gates
| Gate | Required evidence |
|---|---|
| Intended use | Written scope, permissions, prohibited uses and qualified ground-truth process |
| Data | Source/licence, provenance, privacy, labels and leakage audit |
| Evaluation | Frozen held-out results, confusion matrix, calibration and error analysis |
| Uncertainty | Tests show insufficient/conflicting inputs abstain and request review |
| Security/privacy | Access control, retention, audit trail and risk review |
| Pilot readiness | Independent expert/legal review, operator procedures and confirmatory testing |

## Commercial positioning
**Value proposition to test:** an auditable research workflow for authorized screening teams to evaluate multimodal evidence and manage uncertainty—not a standalone narcotics detector.

Potential audiences include research laboratories, authorized screening-technology integrators and academic safety/evaluation groups. These are possible audiences, not confirmed customers.

Do not claim chemical identification, illicit-substance accuracy, detection superiority or enforcement readiness without validated evidence and authorization. Ordinary RGB imagery cannot establish a chemical substance's identity. Pricing must wait until intended use, data governance and sensor requirements are clear.

## Award application evidence pack
- Narrow problem statement and lawful intended use.
- Reproducible demo using clearly marked synthetic or authorized data.
- Data governance, privacy and expert-labeling plan.
- Evaluation protocol, held-out metrics and error analysis.
- UNKNOWN/abstention, conflicting-input and auditability tests.
- Human-review and confirmatory-testing workflow.
- Realistic milestones, budget and partner letters only when obtained.

## Cost, safety and integrity
- Free/local-first; no paid inference, cloud GPUs or subscriptions without explicit approval.
- Do not commit sensitive case or personal data without authorization.
- Synthetic metrics are not real screening performance.
- Never present an AI score as proof of substance identity or enable independent enforcement action.
- This is a plan, not proof checklist items are complete. Record commit, dataset version, environment, results and unresolved failures after each verified run.
