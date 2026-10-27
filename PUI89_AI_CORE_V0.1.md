# PUI89 AI Core v0.1

Initial shared, local-first interfaces for PUI89 AI projects.

## Included
- Dependency-free world-state records and confidence validation.
- Simulation-only action proposals; no robot commands execute.
- JSON failure-report writer and standard-library tests.

## Run tests
Python 3.10+: `python -m unittest discover -s tests -v`

No model weights, paid APIs, cloud services, or third-party packages are required for these checks.

## Safety and evidence boundary
This is an interface scaffold, not a validated perception model, robot controller, or end-to-end system. Confidence values are supplied by callers and are not calibrated here. Actions remain proposals for human review or simulation. Hardware execution is out of scope.

## Next steps
Run tests on the target laptop, inspect each project's existing structure before integration, record measured outcomes, and check licences/resources before adding optional models or simulators.
