# PUI89 Shared AI Core — Sentinel Quadruped Inspection Adapter

**Status:** Integration plan; documentation only.  
**Product identity:** PUI89 Sentinel — All-Terrain Exploration & Inspection Robot, a four-legged quadruped.  
**Platform contract:** [PUI89 Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core)

## Purpose

Apply the shared PUI89 evidence, provenance, multimodal-quality, uncertainty, abstention, safety and human-review contracts to supervised inspection missions. Sentinel uses **General Multimodal Intelligence** to combine observations from permitted modalities; it is not a narcotics-screening system.

## Observation modalities

Each modality remains a separately traceable observation with source, timestamp, device/system identifier, quality, calibration state when relevant, provenance, permission context and explicit missing/failed status.

- **Vision:** RGB, depth and optional thermal imagery for visible scene, asset, surface and condition observations.
- **Spatial:** LiDAR, map, localisation and geometry observations, with coordinate frame and freshness.
- **Audio:** authorised speech and acoustic-event observations; no speaker identity inference.
- **Text:** operator instructions, checklists, labels and inspection notes with source attribution.
- **Robot and environment telemetry:** IMU, joint state, foot contact, battery, compute health and mission-specific sensor time series.

Candidate modalities are not proof of installed hardware. A sensor is treated as available only when the actual device, interface, calibration and health state are evidenced.

## World-state requirements

Track modality availability, timestamp alignment, coordinate frames, sensor health, image/signal quality, calibration state, evidence age, conflicts, model/software version and human-review status. Preserve each source observation; do not merge incompatible scores or treat an absent modality as a negative result.

## Inspection tasks

- Scene and asset observation, object/condition detection, segmentation and tracking where supported by evidence.
- Terrain, obstacle, free-space and traversability assessment with explicit uncertainty.
- Mapping, localisation and robot-motion-state context.
- Inspection checklist support, change observations and traceable report generation.
- Safe-stop, safe-hold, retreat and operator-escalation proposals.

All tasks remain proposals or observations until the corresponding software, simulation, bench and physical validation gates are passed.

## Safety and proposal rules

- HOLD when required modalities are missing, degraded, stale, uncalibrated, out of distribution or materially conflicting.
- Abstain rather than force an interpretation when evidence is inadequate.
- AI output must never override independent mechanical/electrical safety controls or operator authority.
- No autonomous enforcement, accusation, detention, search, seizure or coercive action.
- No biometric identity inference or voice identity recognition.
- No entry into hazardous atmospheres or unstable structures based on camera, depth or LiDAR interpretation alone.
- Consequential actions require authorised human approval and a separately engineered control system.

## Evaluation gates

1. Validate shared schemas, provenance and modality-specific metadata.
2. Test missing, stale, degraded, corrupted, conflicting and out-of-distribution inputs.
3. Evaluate each modality separately before any multimodal fusion claim.
4. Test timestamp alignment, calibration handling and coordinate-frame consistency.
5. Evaluate perception and terrain tasks on permission-cleared, representative data with human-verified ground truth.
6. Report per-task metrics, class/sample counts, uncertainty, abstention, failure cases and measured CPU/RAM/runtime.
7. Keep synthetic, simulated, bench and physical results separate.
8. Verify safe-hold, operator escalation and recovery workflows independently of model confidence.

## Required report

Include mission scope, data provenance/permissions, sensor/device identity, calibration and health state, modality availability, software/model version, test split or scenario definition, metrics, failure cases, abstention rate, operating conditions, limitations and reviewer. If representative data, a suitable sensor or a reproducible evaluator is unavailable, report the relevant result as **NOT MEASURED**.

## Implementation boundary

This document is an adoption plan. It does not establish a physical Sentinel prototype, integrated sensor suite, validated locomotion, field accuracy, deployed multimodal runtime or certified safety performance.
