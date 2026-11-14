# PUI89 Sentinel — Mobile X-ray Engineering Specification (Preliminary)

**Status:** Concept / requirements definition only  |  **Revision:** 0.2
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

## 8. Port, cargo-yard and container-entry inspection

### 8.1 Mission scope

Sentinel's proposed port mission is to support authorised inspection teams across defined port operating areas, including cargo yards, container rows, approved inspection zones and selected container interiors. This is a design target only; no port deployment, access permission, port-system integration or field capability is claimed.

The mission may include:
- Patrol and mapping of approved routes in container yards and logistics areas.
- Navigation around parked containers, trailers, pallets and other static cargo.
- Detection and avoidance of moving vehicles, forklifts, cranes, workers and pedestrians, with conservative yielding and safe-stop behaviour.
- Approach to an assigned container and assessment of doorway, threshold, floor and interior clearance.
- Entry, internal mapping, visual/thermal inspection and safe exit where geometry, floor condition, air quality and operating permissions are suitable.
- Inspection evidence capture, anomaly flagging and operator-reviewed reporting with container/task identifiers supplied by authorised workflows.

Sentinel must not enter active vehicle lanes, crane operating envelopes, restricted areas or a container with unknown or unsafe conditions. Port traffic control, site rules and authorised human supervision take precedence over robot navigation.

### 8.2 Container access and interior navigation

### Difficult container environments

| Environment | Required capability |
|---|---|
| Narrow entrance | Accurate approach, alignment and verified body/leg clearance |
| Raised floor threshold | Controlled step-over with foot-contact and body-stability monitoring |
| Dark interior | Low-light imaging and onboard illumination with exposure/lighting checks |
| Crowded cargo | Narrow-space navigation, cargo-edge awareness and safe retreat |
| Uneven floor | Adaptive foot placement and slip/stumble detection |
| Long container | Local mapping, localisation and return-route planning |
| Lost communication | Safe hold, onboard fault handling and recovery/exit procedure; no blind continuation |

These are engineering requirements, not validated capabilities. Each condition requires representative mock-up testing and documented acceptance criteria. If Sentinel cannot confirm clearance, stable footing, localisation or a viable exit route, it must stop safely and request operator assistance rather than continue blindly.

Before entry, the system must assess the opening width and height, threshold height, door position, available turning space, visible floor condition, cargo protrusions, overhead clearance and a viable exit path. The robot's complete body, legs, sensor modules, carried payload and any moving joints must remain within the verified clearance envelope.

Required capabilities to engineer and test:
- Precise approach alignment and low-speed threshold traversal.
- Body and leg configuration suitable for narrow doorways and constrained interior clearance.
- Forward, reverse and turning manoeuvres, including a verified retreat strategy.
- Obstacle, cargo-edge, overhead and protrusion awareness.
- Low-light illumination and camera exposure control without obscuring evidence.
- Local mapping and localisation with safe behaviour when GNSS is unavailable indoors.
- Detection of unstable stacks, blocked routes, damaged flooring, liquid, loose straps and other visible hazards where sensors support it.
- Safe hold and operator escalation if the route is blocked, localisation confidence is inadequate, communication is lost or the robot cannot confirm an exit path.

Container interiors may contain hazardous atmospheres, oxygen deficiency, fumigants, chemicals, heat, dust, unstable cargo or other risks not reliably detectable by the proposed camera/LiDAR package. Entry requires a site-specific risk assessment and confirmation by the responsible port operator that the space is safe for robotic entry. Sentinel is not an atmosphere-safety certification device; dedicated calibrated gas/atmosphere instruments and approved procedures are required where relevant. No human-entry or confined-space safety rule is replaced by the robot.

### 8.3 Port sensing and mission data

Potential sensor inputs include RGB and low-light cameras, depth sensing, LiDAR, thermal imaging, IMU and robot-state sensors, and authorised site/map data. GNSS may be unavailable or degraded between container rows and inside containers; local localisation and mapping must therefore be tested independently. Optional connectivity to terminal operating systems, container manifests, OCR or RFID is a separately authorised integration and must not be assumed.

Every observation must retain timestamp, sensor identity, calibration/health status, location or local map reference, uncertainty and task/container association. OCR or visible container markings may be used as candidate identifiers only; an authorised workflow must verify identity before records are linked. Minimise collection of worker/visitor imagery and apply site-approved privacy, access, retention and cybersecurity controls.

### 8.4 X-ray and other inspection modalities in port operations

The quadruped may carry a removable certified X-ray payload between authorised inspection points, subject to the payload feasibility gates in this specification. X-ray exposure remains prohibited during locomotion. A scan may occur only when the robot is stationary and stabilised, the complete certified inspection arrangement and controlled area are established, independent safety permissives are satisfied and an authorised qualified operator enables the procedure. Whether an X-ray system can safely and legally be used inside a container, in a cargo yard or near other workers must be assessed for the exact equipment, geometry, jurisdiction and site; no universal permission is implied.

RGB, thermal, X-ray and any calibrated chemical-instrument measurements remain distinct evidence channels. X-ray structure images do not identify a chemical or prove narcotics. Chemical instruments can report only defined analytes within validated calibration and operating limits. AI outputs are inspection decision support, not grounds for automatic accusation, detention, search or enforcement.

### 8.5 Port and container validation gates

| Gate | Evidence required | Status |
|---|---|---|
| P0 — Site and mission definition | Port operator approval, mapped operating zones, traffic interfaces, task scope and jurisdictional review | Open |
| P1 — Port mobility | Simulation and supervised tests for container rows, pedestrian/vehicle interactions, stopping distance and communications loss | Open |
| P2 — Doorway access | Measured doorway/threshold envelope and repeatable entry/exit tests using an inert payload | Open |
| P3 — Interior navigation | Clearance, turning/reversing, localisation, obstacle and exit-route tests in representative mock-up containers | Open |
| P4 — Environmental safety | Site-specific assessment for atmosphere, temperature, dust, water, floor integrity and cargo stability; dedicated instruments where required | Open |
| P5 — Inspection evidence | Modality-specific image quality, timestamping, container/task association, uncertainty and human-review workflow | Open |
| P6 — X-ray port use | Equipment-specific radiation safety case, controlled-area design, operator qualification and regulatory/site approvals | Open |
| P7 — Operational trial | Port-authorised supervised trial, incident/recovery records, privacy/security review and acceptance criteria | Open |

No gate is passed by design documentation alone. Physical access, mobility, sensing and safe operation require representative testing and site approval.

## 9. Verification and validation gates


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

## 10. Procurement and provenance controls

Before any purchase proposal, record exact manufacturer, model/part number, country of manufacture, manufacturer origin evidence, datasheet revision, certification, intended use, mass, dimensions, power, warranty, service availability, indicative price/date/source, shipping and import constraints. Verify provenance independently; unknown origin or incomplete certification is UNVERIFIED — NOT APPROVED.

No purchase, download, installation, supplier commitment or paid service is authorised by this specification.

## 11. Current engineering decision

The design requirement is onboard carriage of a removable X-ray payload. This does not establish that a compact, safe, compliant payload meeting the robot's eventual mass and power limits is commercially available. If supplier evidence shows that the payload cannot meet the validated mobility envelope, revise the platform or mission concept rather than weakening radiation-safety requirements.

**Current status:** concept only; all dimensions, mass, actuator, battery, imaging and compliance values are TBD. No prototype, integration, radiation emission or field capability is claimed.