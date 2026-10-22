# AI Agent Review and Support Plan

## Purpose
Provide repeatable review of the multimodal screening decision-support prototype. The agent checks data quality, software logic, provenance, uncertainty, and human-review escalation. It must not infer that a substance is a narcotic from appearance alone or infer guilt/criminality.

## Automated review stages
1. **Repository health:** run tests and report failing checks with links.
2. **Evidence integrity:** validate file manifests, modality names, timestamps, source/provenance fields, missing inputs, and permission records.
3. **Conflict and uncertainty tests:** test contradictory modality records, low-confidence outputs, missing modalities, out-of-distribution flags, and corrupted inputs.
4. **Decision logic:** verify that missing authorization or conflicting/insufficient evidence routes to human review rather than an automated conclusion.
5. **Evaluation readiness:** require documented labels, lawful data access, dataset version, split manifest, model identity, and evaluation protocol before calculating metrics.
6. **Audit report:** log what was supplied, what checks ran, what was missing, and why the system abstained or escalated.

## Evidence labels
- **PASS:** a defined automated check ran and passed.
- **FAIL:** a defined check ran and failed.
- **NOT RUN:** required code/data/model was unavailable.
- **HUMAN REVIEW REQUIRED:** evidence cannot support an automated conclusion.
- A software test passing does not validate chemical identification or legal conclusions.

## Suggested report
A dated Markdown report should include commit SHA, test summary, input/provenance status, conflict tests, evaluation protocol, limitations, and evidence links. Avoid storing sensitive case or personal data in public logs.

## Cost and permissions
Use existing Python tooling and GitHub Actions where available. No paid API, cloud service, or external upload is required. Use least-privilege workflow permissions and avoid automatically publishing sensitive inputs or outputs.

## First priorities
- Add tests for missing authorization, conflicting modality records, and insufficient evidence.
- Add schema validation and a synthetic test set with clearly documented expected outcomes.
- Generate an audit report that distinguishes rule-engine tests from model validation.
- Ensure all uncertain cases abstain and request authorized human review.

## Limitations
This prototype is not a validated chemical identification instrument, law-enforcement decision system, or substitute for laboratory analysis and authorized professional judgment.