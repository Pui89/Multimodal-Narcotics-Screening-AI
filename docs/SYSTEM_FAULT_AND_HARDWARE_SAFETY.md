# System Fault and Hardware Safety Playbook

**Status: design guidance only.** This document is not certification for screening equipment or a physical robot. It does not establish chemical identity from an image, and an AI flag must not independently trigger enforcement action.

## Safety and decision priority

When input quality, equipment health, authorisation, or system integrity is uncertain, stop automated classification, preserve safe status/diagnostic functions, and send the case to an authorised human reviewer. Do not invent a result from missing data.

## Fault response matrix

| Fault or situation | Required response to design and test |
|---|---|
| AI/model crash, timeout, unsupported class, or uncertain output | Cancel automated classification; display an unavailable/uncertain status and require human review. |
| Camera, illumination, scale, scanner, sensor, or modality missing/stale/out of calibration | Mark the affected modality unavailable; do not infer a conclusion from absent or unreliable input. |
| Modalities conflict or image quality is poor | Flag the conflict/quality issue; request recapture or expert review, not an automatic positive/negative decision. |
| Network, database, or remote service unavailable | Use only an authorised, explicitly approved local workflow if available; otherwise pause and preserve the case safely. Never silently bypass access controls. |
| Power loss, low battery, overheating, or unstable voltage | Stop the active scan safely; preserve data using validated mechanisms and do not resume until equipment health is checked. |
| Main computer or process freezes | Independent watchdog and hardware interlocks should place moving/scanning hardware in its designed safe state; test independently of application software. |
| Conveyor, gripper, robotic arm, door, or sample-handling mechanism jams or moves unexpectedly | Stop the relevant mechanism, prevent access to pinch/crush zones, alert operator, and use a planned recovery procedure. |
| Electrical fault, damaged cable, liquid ingress, smoke, unusual heat, or battery damage | Keep people clear, isolate power only if safe, and request qualified inspection. Do not handle exposed conductors or wet equipment. |
| Emergency stop, guard/door interlock, or safety sensor fault | Keep motion disabled until inspected and intentionally reset. Reset must not automatically restart the mechanism or scan. |
| Unauthorised user, tampered file, integrity check failure, or missing audit record | Deny the affected operation, preserve security logs without exposing sensitive data, and escalate to an authorised administrator. |
| Storage full, corrupted record, wrong timestamp, or failed logging | Do not issue a final screening report if traceability is required; preserve the case and request operator review. |
| Software/model/configuration update or unknown fault | Pause automated use until version, data handling, and relevant regression tests are checked. |

## Hardware, electrical, and data-protection checklist

- Use a physical emergency stop, guarded moving parts, appropriate interlocks, and independent actuator-disable circuitry for any physical machinery, based on a qualified risk assessment.
- Keep hardware safety functions independent of AI inference, application code, network availability, and database status.
- Use appropriately rated power supplies, fuses, wiring, connectors, grounding/isolation, thermal management, and enclosure protection for the real equipment.
- Prevent unexpected restart after power or network recovery and after emergency-stop reset.
- Restrict access by role; minimise personal data; protect case records and logs; record model/software versions and human review decisions. Do not store unnecessary sensitive images.
- Provide a safe manual procedure for jam clearing and maintenance; isolate hazardous energy before reaching into moving equipment.
- Test missing inputs, conflicting inputs, network loss, power loss, watchdog action, interlocks, emergency stop, data-integrity failure, and recovery before real deployment.

## Recovery and verification

For each fault, document how it is detected, the safe output state, operator notification, data-preservation behaviour, recovery and reset authority, test setup, expected/actual results, and evidence. Test combinations such as network loss during a scan. Mark untested cases **NOT TESTED**. No software can promise protection from every possible fault without hardware-specific design and validation.

## Current project boundary

This repository provides workflow and software design guidance; it does not establish a trained chemical detector, validated physical screening robot, or certified safety system. AI outputs require authorised human review and must not be treated as proof of chemical identity or guilt.

## Security, intrusion, and physical-threat scenarios

These are design requirements for the software and any future screening equipment—not a claim that all controls exist today.

| Threat or incident | Required response to design |
|---|---|
| Stolen credentials or unauthorised access | Apply least privilege and MFA where supported; revoke access/tokens; rotate exposed credentials; review audit logs. |
| Malware, ransomware, destructive virus, or compromised model/update | Isolate affected workstation/equipment; stop automated classification; preserve logs and case integrity; restore from known-good backups after security review. |
| Tampered evidence, spoofed sensor input, or altered model/configuration | Verify file hashes/signatures and model/configuration versions where available; quarantine untrusted inputs; require authorised review before resuming. |
| Data theft or privacy breach | Restrict access, minimise retained personal data, secure backups, follow incident-reporting duties and applicable law, and avoid exposing sensitive records in logs. |
| Physical theft, tampering, vandalism, or attempted robbery | Secure the equipment and records; alert authorised site security; do not confront or pursue a suspect; inspect and re-authorise equipment before use. |
| Threatening person, gunshot, or suspected armed attack | Do not approach or confront the threat. If safe, stop machinery and follow the site's shelter/evacuation procedure; contact emergency services. Screening equipment must not be used as a weapon. |
| Fire, electrical damage, or deliberate sabotage | Keep people clear, isolate power only if safe, follow site emergency procedures, and require qualified inspection before restarting. |
| Untrusted network or unavailable database | Pause any operation requiring unavailable authorisation or audit records; do not bypass access controls or fabricate a screening result. |

**Do not infer guilt or chemical identity from appearance alone, and do not use the system to target, pursue, restrain, or harm people.** Threat response belongs to trained people and established emergency procedures.
