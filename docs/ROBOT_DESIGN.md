# PUI89 Sentinel — Quadruped Exploration Robot Design Direction

## Design goal

Develop a compact, robust four-legged robot for supervised exploration, environmental awareness and inspection across selected terrain and facilities. “Explore Anywhere” is the long-term design ambition, not a guarantee of unrestricted operation.

## Concept architecture

1. **Quadruped chassis:** four articulated legs, protected joints and a central payload/compute bay. Joint count, dimensions, mass and payload remain TBD.
2. **Perception:** forward RGB and depth/stereo cameras; optional 360-degree LiDAR after range, power and cost review.
3. **Body state:** IMU, joint encoders and foot-contact sensing for attitude, gait and contact awareness.
4. **Mission sensors:** optional thermal, audio or calibrated environmental sensors only when a defined use case requires them.
5. **Edge compute:** local CPU-first processing with optional accelerator support; exact board and power budget TBD.
6. **Operator interface:** mission definition, map/terrain context, live status, uncertainty, evidence and emergency-stop/abort status.
7. **Independent safety:** hardware emergency stop, watchdog, safe torque/power handling and independent low-level control before physical movement.

## AI functions

Scene understanding and object/asset observations; terrain geometry and traversability estimation; obstacle/free-space and dynamic-obstacle awareness; mapping/localisation confidence; quadruped state and foot-contact monitoring; inspection checklists, visible anomaly/change detection and evidence reporting; bounded waypoint, safe-stop and retreat proposals.

## Engineering constraints

Evaluate stability, centre of gravity, joint torque, foot-ground interaction, actuator thermal limits, battery safety, payload, ingress protection, repairability and total cost before hardware selection. Use non-Chinese-origin components where technically suitable and require origin evidence. No BOM or procurement decision is approved here.

## Exclusions

No narcotics screening, X-ray, chemical identification, enforcement, weapons, pursuit, restraint, biometric identification, drone or aerial capability. No claim of prototype or validated locomotion.
