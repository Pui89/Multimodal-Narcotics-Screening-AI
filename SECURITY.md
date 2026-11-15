# Security Policy

## Scope

This policy covers the PUI89 Sentinel All-Terrain Inspection Robot Dog repository, its software, documentation, simulation assets, evidence-processing workflows and any future hardware integration. Sentinel is a quadruped inspection concept; no physical prototype, sensor integration or field performance is claimed.

Historical screening-related code, workflows and documentation may remain in repository history or in clearly identified legacy areas. They are not part of Sentinel's current product scope. See [Sentinel scope migration and legacy artifact register](docs/SENTINEL_SCOPE_MIGRATION.md).

## Reporting a vulnerability

Please do not publish exploit details, credentials, personal data, or a working attack in a public issue. Use GitHub's private vulnerability reporting feature if enabled. Otherwise, contact the maintainer through the GitHub profile and share only the minimum information needed to reproduce the issue safely. Do not include real secrets or sensitive case records in reports.

## Safety, privacy, and security boundaries

- Treat images, documents, metadata, model files, robot telemetry and external evidence as untrusted inputs; validate file types, sizes and parsing boundaries.
- Never commit passwords, API keys, tokens, private keys, identifiable personal data or non-public inspection records.
- Preserve provenance, timestamps, uncertainty and missing-data states. Do not present a model estimate as a verified physical condition.
- Do not connect an AI proposal directly to an actuator or safety-critical action. Keep independent interlocks, emergency stop and human approval.
- Do not claim RGB, depth or LiDAR can certify breathable air or detect every hazardous gas. Use suitable calibrated instruments and site procedures where required by the risk assessment.
- Use least privilege, reviewed changes, dependency updates and tested offline backups.
- Restrict access to sensitive data and retain only what is necessary and authorised.

## Incident response

1. Suspend affected processing and prevent further disclosure of sensitive records.
2. Isolate affected devices, revoke compromised tokens/sessions, and rotate credentials from a clean device.
3. Preserve relevant logs and commit/run identifiers while protecting personal data.
4. Restore from a known-good version; inspect dependencies, model provenance and workflow changes.
5. Require human review of integrity, privacy and safety controls before resuming use.

## Disclosure

Please allow the maintainer reasonable time to investigate and prepare a fix before sharing technical details publicly.

## Automated security verification

Security checks may run through the repository's GitHub Actions workflows when relevant source, dependency, workflow or security-policy files change. Depending on workflow configuration, checks may include secret-pattern detection, dependency vulnerability auditing, static analysis and CodeQL. A configured check is not evidence of a clean result: verify the latest workflow run and retain its logs before marking a control as passed. No AI model or robot command is authorised by a successful software scan. Review current GitHub Actions usage limits before enabling additional workflows or services.
