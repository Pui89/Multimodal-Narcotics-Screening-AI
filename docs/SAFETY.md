# Sentinel Safety Requirements

**Status:** engineering requirements for future simulation and hardware validation; not a safety certification.

## Operating principles

- Operate only in authorised locations and within a documented, validated operating envelope.
- AI models provide observations and bounded proposals; they do not override deterministic safety controls.
- No autonomous enforcement, coercive action, diagnosis or consequential decision is permitted.
- Unknown, missing, stale or contradictory critical information must lead to STOP / SAFE_HOLD and human review.

## Independent motion-safety gate

Before any motion request is accepted, the safety layer must check:

- Emergency-stop state and hardware safety-controller health.
- Localisation confidence and sensor-data freshness.
- Collision clearance, human exclusion zones and dynamic obstacles.
- Workspace, joint, speed, force and stability limits.
- Actuator, battery, power and thermal health.
- Communications watchdog and operator-control availability.
- Approved mission, access permissions and task boundary.

Any failed or unknown critical check must block the motion request. A software STOP/HOLD state does not physically stop hardware unless an independent, validated hardware stop path is installed.

## Perception and uncertainty

Keep UNSEEN, OCCLUDED, UNKNOWN, OBSERVED and SUSPECTED_ANOMALY states distinct. A missing detection is not proof that an object, hazard or condition is absent. Conflicting sensors, poor image quality, uncalibrated instruments and out-of-distribution inputs must be surfaced explicitly.

## People, privacy and evidence

- Treat people and vehicles as dynamic obstacles; respect site rules and exclusion zones.
- Do not perform biometric identity inference.
- Minimise personal data and apply access control, retention limits and audit logging.
- Preserve source, timestamp, sensor/configuration, model version, uncertainty and operator review for evidence records.

## Required fault scenarios

Validate emergency stop, sensor failure, stale data, localisation loss, unsafe footing, actuator fault, battery/thermal fault, communications loss, watchdog timeout, obstacle intrusion and operator override. Record expected response, measured response, test configuration and evidence.

No safety or mobility claim may be published until supported by reproducible tests for the exact hardware/software configuration.
