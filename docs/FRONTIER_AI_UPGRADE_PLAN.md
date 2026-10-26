# Frontier AI Technology and Free-First Upgrade Plan

## Goal

Develop a responsible multimodal screening and robotic-inspection research concept with auditable evidence. Prioritize free/open-source tools, local tests, privacy and human review. Do not present a concept as a validated operational screening system.

## Priority order

### P0 — Data governance and scope
- Record dataset origin, license/permission, permitted use, labeling protocol and exclusions for every data source.
- Avoid sensitive personal data and unlicensed operational imagery.
- Define the intended screening task precisely; do not infer substance identity from weak visual evidence or present model output as a definitive finding.
- Keep test/evaluation data separate from development data.

### P1 — Evidence and safety workflow
- Produce a traceable report for each experiment: data version, model/version, configuration, metrics, errors and limitations.
- Require human review for uncertain, conflicting or high-consequence outputs.
- Do not automatically trigger enforcement, detention, destructive inspection or other consequential action from model predictions.
- Test missing inputs, contradictory modalities, low-quality images and out-of-distribution examples.

### P2 — Multimodal baseline
- Establish a simple, documented baseline before adding advanced vision-language models.
- Compare models only on the same approved dataset split and label protocol.
- Measure false positives and false negatives, class-specific performance, calibration/uncertainty where feasible and runtime.
- Check model licenses, data restrictions, hardware requirements and offline capability before adoption.

### P3 — Controlled agentic assistance
- Build a bounded agent workflow for checking data provenance, running evaluations, summarizing evidence and flagging incomplete records.
- Agents may recommend next steps but cannot turn an uncertain prediction into a confirmed finding.
- Keep the core validation workflow independent of paid APIs and hosted model availability.

### P4 — Robotic inspection concept
- Specify sensor inputs, inspection workflow, operator handoff and safe-stop behavior.
- Use simulation or recorded test data before any physical integration.
- Clearly label conceptual robot imagery and distinguish simulated behavior from tested hardware.

## Acceptance criteria
- Data sources have traceable provenance and license/permission status.
- Evaluation data is held out from training and tuning.
- Reports include error analysis and limitations, not only aggregate scores.
- Uncertain results are routed to human review.
- README distinguishes implemented, in-progress, planned and unverified capabilities.

## Free-first tool policy
Prefer Python, pytest, Ruff, OpenCV and compatible open-source ML tools. Check data and model licenses before adoption. Keep tests runnable without paid APIs or cloud compute. No paid service, subscription or metered API without explicit approval.

## Current status
This document is a plan, not evidence that all listed stages are implemented or passed. Model accuracy, real-world screening utility and physical robot capability remain unverified until supported by reproducible evaluations.
