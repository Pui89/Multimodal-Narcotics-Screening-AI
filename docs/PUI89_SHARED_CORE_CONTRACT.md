# PUI89 Shared AI Core Contract — Sentinel Quadruped Profile

## Purpose

This contract maps common PUI89 vocabulary for observations, uncertainty, stale data, unknown state and conflicts to Sentinel's quadruped exploration and inspection requirements. It is an integration direction, not proof of runtime integration or physical capability.

## Interface

- Observation: value, source provenance, observation timestamp, confidence/uncertainty and optional calibration status.
- assess_observation: returns ACCEPT, REVIEW or REJECT with machine-readable reason codes.
- WorldState: timestamped local environment and robot-state representation with conservative conflict checks.
- ActionProposal: advisory mission or inspection proposal only; never direct actuator permission.
- FailureReport: fault, severity, safe state, evidence references and recovery request.
- Physical actuation remains disabled unless a separate, independently validated safety and control system authorises it.

## Decision policy

Missing values, invalid confidence, future timestamps, stale or low-quality observations, missing provenance, uncalibrated inputs and conflicting observations must be rejected, reviewed or represented as UNKNOWN/CONFLICT. Do not infer safe terrain from a single image or model score.

## Project-specific use

- **Coconut Harvest AI:** confidence and freshness gates before target localisation or harvestability proposals; reachability and cutting safety remain separate validation tasks.
- **Extreme Flood Rescue AI:** treat stale/conflicting water, current, localisation and person/animal observations conservatively; this contract is not flood physics or rescue validation.
- **PUI89 Sentinel:** terrain, obstacle, spatial, localisation, IMU, joint-state and foot-contact observations; safe-hold and supervised recovery proposals. No locomotion or sensor integration is established.
- **PUI89 AI HOME:** indoor scene and obstacle awareness under a separate product-specific profile.
- **PUI89 AI NOMAD:** four-wheel mobile-assistant awareness under a separate product-specific profile.

## Run tests

From the repository root, using Python 3.10+:

```bash
python -m unittest discover -s tests -p "test_pui89_world_state.py" -v
```

The tests use only the Python standard library. They do not install packages, download models, contact a hosted API or control hardware.

## Status

This file and its tests are engineering scaffolding. Run the command and record actual output before describing tests as passed. No accuracy, latency, calibration quality, quadruped locomotion or field performance is claimed.
