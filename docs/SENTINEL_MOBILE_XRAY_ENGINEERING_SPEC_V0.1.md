# PUI89 Sentinel — Mobile X-ray Engineering Specification (Preliminary)

**Status:** Concept / requirements definition only  |  **Revision:** 0.1
**Hardware status:** No X-ray payload selected, purchased, integrated, certified or tested.
**Approval:** This document does not authorise procurement, radiation generation or field operation.

## 1. System objective

Define a quadruped mobile inspection robot that carries a removable X-ray payload while travelling between authorised inspection locations. The robot may transport the payload while walking, but X-ray emission is prohibited while the robot is moving. Scanning is permitted only after the robot is stationary, stabilised, the inspection arrangement and controlled area are established, and an authorised operator enables the certified system.

The X-ray subsystem must be a complete, commercially supplied and appropriately certified source/detector solution selected for a clearly defined inspection task. Generator design, exposure settings and shielding construction are outside this concept document and must be handled by qualified suppliers and radiation-safety specialists.

## 2. System architecture and interfaces

| Subsystem | Required function | Key interface / evidence |
|---|---|---|
| Quadruped mobility | Carry payload between inspection locations; stand and hold a stable posture | Payload envelope, mounting loads, joint state, foot contact, IMU |
| Removable payload carrier | Secure equipment and permit controlled removal/service | Mechanical interface drawing, retention inspection, mass properties |
| X-ray source/detector package | Produce and capture images for the defined object class | Manufacturer datasheet, certification, intended-use statement, service requirements |
| RGB camera | External object and scene context | Camera calibration, image-quality checks, timestamp |
| Depth camera | Surface geometry and relative positioning | Validated operating range and calibration |
| Thermal camera | Surface-temperature context where relevant | Sensor specification and calibrated-use limits |
| 360-degree LiDAR | Navigation and spatial mapping | Sensor specification, calibration and environmental limits |
| IMU and robot-state sensing | Estimate posture, movement and stability | Timestamped orientation, acceleration, joint and foot-contact state |
| Edge AI computer | Image-quality checks, modality-specific inference and evidence management | Compute, memory, thermal and power budget |
| Independent safety subsystem | Enforce safe state and inhibit X-ray unless all required conditions are met | Safety case, interlock evidence, radiation monitoring and operator authorisation |

RGB, depth, thermal, LiDAR and X-ray are distinct evidence modalities. They must retain their own source identity, timestamps, calibration status, uncertainty and quality flags. X-ray imagery alone must not be represented as chemical identification or proof that an item contains a narcotic substance.

## 3. Payload and mass budget

No payload mass or external dimensions are approved yet. Populate this ledger only from exact manufacturer datasheets or measured prototype parts.

| Item | Quantity | Unit mass | Subtotal | Source / status |
|---|---:|---:|---:|---|
| Certified X-ray source assembly | TBD | TBD kg | TBD kg | Manufacturer datasheet required |
| Compatible digital detector | TBD | TBD kg | TBD kg | Manufacturer datasheet required |
| Manufacturer-approved protective enclosure / shielding assembly | TBD | TBD kg | TBD kg | Supplier and radiation-safety approval required |
| Interlocks, indicators and radiation monitor | TBD | TBD kg | TBD kg | Certified component datasheets required |
| Payload frame, mounts and retention | TBD | TBD kg | TBD kg | CAD and structural assessment |
| RGB camera | TBD | TBD kg | TBD kg | Selected sensor datasheet |
| Depth camera | TBD | TBD kg | TBD kg | Selected sensor datasheet |
| Thermal camera | TBD | TBD kg | TBD kg | Selected sensor datasheet |
| 360-degree LiDAR | TBD | TBD kg | TBD kg | Selected sensor datasheet |
| Edge computer and storage | TBD | TBD kg | TBD kg | Selected hardware datasheet |
| Power conversion and wiring | TBD | TBD kg | TBD kg | Electrical design |
| Other robot payload accessories | TBD | TBD kg | TBD kg | Itemised evidence required |

Payload mass = sum of all installed payload item subtotals.
Gross robot mass = base robot mass (including legs, actuators and base battery) + installed payload mass + any carried accessories not already counted.

Avoid double-counting batteries, mounts, cables or protective enclosures. Record both travel configuration and scan configuration if any component is repositioned or deployed.

## 4. Packaging and centre-of-gravity assessment

Record the following from the selected equipment and a dimensioned CAD assembly:
- Payload length, width, height and keep-out envelope: TBD.
- Mounting interface, fasteners and retention method: TBD.
- Payload centre of gravity in robot coordinates: TBD.
- Complete robot centre of gravity in travel and scan configurations: TBD.
- Clearance from legs, joints, cameras, LiDAR field of view and service access: TBD.
- Permitted body pitch/roll and foot-placement envelope: established by locomotion testing, not assumed.

For each configuration, calculate the combined centre of gravity from measured component masses and their three-dimensional positions:

r_CG = (sum(m_i × r_i)) / (sum(m_i))

Assess the projected centre of gravity against the support polygon throughout the intended stationary inspection postures, including the effect of uneven ground, payload movement and external disturbances. This equation is a bookkeeping model, not proof of dynamic stability. Dynamic stability and fall risk require simulation and physical testing.

## 5. Leg, actuator and structure sizing inputs

Do not select motors from robot body mass alone. The engineering team must determine:
- Maximum gross mass and payload distribution from the verified mass ledger.
- Leg geometry, segment lengths, joint locations and mechanical transmission.
- Static support loads and dynamic load cases for walking, stopping, turning, stepping and recovery.
- Ground-contact assumptions for each target terrain.
- Joint torque-speed envelope, peak and continuous thermal limits, duty cycle and braking/holding requirements from actuator manufacturer data.
- Structural strength, fatigue, joint backlash, impact protection and serviceability.
- Safe payload and operating-envelope limits for each gait and posture.

Required outputs: joint torque-speed requirements, actuator thermal margins, structural safety assessment, foot-ground load estimates and a validated payload envelope. All numeric limits remain TBD until the robot geometry, verified mass properties and terrain test cases are defined.

## 6. Electrical power and battery budget

Create separate loads for locomotion, compute, cameras, LiDAR, communications, detector, X-ray source package, safety electronics and power conversion. Use exact manufacturer input-voltage and power data.

For each load, record nominal power, peak power, duty cycle, voltage, start-up behaviour and thermal constraints. Do not assume the X-ray source can be powered by the quadruped battery; confirm its certified power arrangement with the supplier.

E_required (Wh) = sum(P_i (W) × t_i (h)) / system_efficiency

Add an explicitly justified reserve after measuring the real mission profile. Verify battery discharge limits, peak current, wiring, connectors, fusing, isolation, thermal management, charging and emergency shutdown. Runtime is not to be published until measured under a representative payload and terrain mission.

## 7. Operating states and safety gates

1. **Travel:** X-ray emission hardware remains inhibited. Robot may move only within its separately validated locomotion envelope.
2. **Arrive and stabilise:** stop, verify posture, foot contacts, IMU state, payload retention and ground suitability.
3. **Inspection-area authorisation:** establish the controlled area, access restrictions, warning indicators and radiation-monitoring arrangements as defined by the approved system.
4. **Pre-scan checks:** certified equipment self-check, interlock state, detector readiness, operator authorisation and independent safety-system permissives.
5. **Scan:** only the certified system's approved operating procedure may enable exposure. Robot remains stationary; no locomotion command may coexist with exposure enable.
6. **Exposure complete:** confirm beam-off state, verify monitoring status and release the controlled area only under the approved procedure.
7. **Resume travel:** retract/secure any deployed components, verify payload retention and only then enable locomotion.

Any loss of interlock integrity, unexpected motion, loss of safety monitoring, unauthorised access, communications fault affecting the safety case or emergency-stop event must inhibit exposure and transition to the certified system's defined safe state. The safety subsystem must be independent of AI perception or model confidence.

## 8. Verification and validation gates

| Gate | Evidence required | Status |
|---|---|---|
| G0 — Requirements | Intended object classes, inspection purpose, operating environments and jurisdiction identified | Open |
| G1 — Supplier selection | Certified source/detector package datasheets, mass, dimensions, power, service and intended-use documents | Open |
| G2 — Mechanical feasibility | CAD envelope, mass properties, centre-of-gravity analysis, mounting and retention review | Open |
| G3 — Mobility feasibility | Simulation and physical tests with representative inert payload; gait, stability, braking and fall-risk evidence | Open |
| G4 — Electrical feasibility | Measured power budget, battery and thermal assessment, electrical safety review | Open |
| G5 — Radiation safety | Complete-system shielding assessment, interlock validation, radiation survey, qualified specialist and regulatory approvals | Open |
| G6 — Imaging performance | Image-quality and detection-performance tests using authorised test objects and documented acceptance criteria | Open |
| G7 — Integrated operation | Stationary-only exposure interlock, no-motion permissive, emergency-stop and fault-injection tests | Open |
| G8 — Field release | Site-specific risk assessment, operator training, maintenance plan, legal approvals and controlled trial evidence | Open |

No gate is passed by documentation alone where physical measurement, independent review or regulatory approval is required.

## 9. Procurement and provenance controls

Before any purchase proposal, record exact manufacturer, model/part number, country of manufacture, manufacturer origin evidence, datasheet revision, certification, intended use, mass, dimensions, power, warranty, service availability, indicative price/date/source, shipping and import constraints. Verify provenance independently; unknown origin or incomplete certification is UNVERIFIED — NOT APPROVED.

No purchase, download, installation, supplier commitment or paid service is authorised by this specification.

## 10. Current engineering decision

The design requirement is onboard carriage of a removable X-ray payload. This does not establish that a compact, safe, compliant payload meeting the robot's eventual mass and power limits is commercially available. If supplier evidence shows that the payload cannot meet the validated mobility envelope, revise the platform or mission concept rather than weakening radiation-safety requirements.

**Current status:** concept only; all dimensions, mass, actuator, battery, imaging and compliance values are TBD. No prototype, integration, radiation emission or field capability is claimed.