# Security Policy

## Scope
This policy covers the Multimodal Narcotics Screening AI source code, evidence-processing pipeline, model files, and any future screening-device integration.

## Reporting a vulnerability
Please do not publish exploit details, credentials, personal data, or a working attack in a public issue. Use GitHub's private vulnerability reporting feature if enabled. Otherwise, contact the maintainer through the GitHub profile and share only the minimum information needed to reproduce the issue safely. Do not include real secrets or sensitive case records in reports.

## Safety, privacy, and security boundaries
- Treat images, documents, metadata, model files, and external evidence as untrusted inputs; validate file types, sizes, and parsing boundaries.
- Never commit passwords, API keys, tokens, private keys, identifiable personal data, or non-public case evidence.
- Appearance-based AI output is not chemical confirmation, proof of a crime, or a determination of guilt. Keep human review, uncertainty reporting, conflict detection, and an abstain/escalate path.
- Do not connect AI output directly to enforcement action or a physical actuator.
- Use least privilege, MFA, reviewed changes, dependency updates, and tested offline backups.
- Restrict access to any sensitive data and retain only what is necessary and authorised.

## Incident response
1. Suspend affected processing and prevent further disclosure of sensitive records.
2. Isolate affected devices, revoke compromised tokens/sessions, and rotate credentials from a clean device.
3. Preserve relevant logs and commit/run identifiers while protecting personal data.
4. Restore from a known-good version; inspect dependencies, model provenance, and workflow changes.
5. Require human review of integrity, privacy, and safety controls before resuming use.

## Disclosure
Please allow the maintainer reasonable time to investigate and prepare a fix before sharing technical details publicly.


## Automated security verification

Security checks are run through the repository's GitHub Actions security workflow when relevant source, dependency, workflow, or security-policy files change. Depending on the workflow configuration, checks may include secret-pattern detection, dependency vulnerability auditing, static analysis, and CodeQL. A configured check is not evidence of a clean result: verify the latest workflow run and retain its logs before marking a control as passed. No AI model or robot/vehicle command is authorized by a successful software scan. Verify current GitHub Actions billing terms and usage limits before enabling additional workflows or services.


Automated dependency audit: the security workflow includes pip-audit on the ephemeral public-repository runner; results must be reviewed from the exact workflow run before claiming dependencies are clear.
