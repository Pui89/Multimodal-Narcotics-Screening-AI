# Step-by-Step Testing Guide

This guide supports repeatable software, evidence-integrity and human-review checks. Use synthetic test cases unless data is lawfully authorized and safe to handle.

## 1. Check the current commit
- Open the repository's **Actions** tab.
- Open the latest run for the commit being reviewed.
- Record the commit SHA and status. A queued or in-progress run is not a pass.

## 2. Run software checks
From a local clone, open a terminal at the repository root and use the test command documented in the repository workflow. If the Python test workflow uses pytest and dependencies are installed:
```powershell
python -m pytest
```
Save full errors and resolve the first underlying failure before rerunning.

## 3. Validate evidence records
- Check required fields, modality names, timestamps, provenance and authorization flags.
- Test missing files, corrupt inputs, duplicate records and conflicting modality entries.
- Keep sensitive case details out of public test logs and repository fixtures.

## 4. Test abstention and human review
Use synthetic cases to test missing authorization, missing modalities, contradictory records, low confidence and insufficient evidence. Expected result: the system flags uncertainty and routes to authorized human review rather than making a definitive identification or legal conclusion.

## 5. Evaluate model readiness
Do not calculate or publish model metrics until lawful data access, approved labels, dataset version, split manifest, model identity and evaluation protocol are documented. Visual appearance alone cannot establish chemical identity.

## 6. Record the result
Create a dated report with commit SHA, commands, synthetic scenarios, pass/fail/not-run status, evidence links and limitations. A passing rule-engine test is not validation of chemical identification or law-enforcement decisions.
