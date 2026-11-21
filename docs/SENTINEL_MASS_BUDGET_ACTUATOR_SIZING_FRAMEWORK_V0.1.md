# PUI89 Sentinel — Mass Budget & Actuator Sizing Framework v0.1

**Status:** Preliminary calculation framework; no hardware selected  
**Date:** 2026-11-21  
**Applies to:** Human-supervised four-legged quadruped  
**Baseline mass direction:** 18–22 kg complete robot, preliminary engineering target only  
**Procurement / fabrication / deployment:** Not authorised

## 1. Purpose and decision boundary

This document defines a traceable method to turn a selected Sentinel inspection mission into a subsystem mass budget, joint-load model, actuator requirements, electrical power estimate and battery-energy estimate.

It does **not** select motors, gearboxes, batteries, sensors, suppliers or materials. It does not claim that the 18–22 kg target has been achieved. Numerical sizing cannot be responsibly frozen until the mission, geometry, gait, payload, operating envelope and safety factors are defined.

Sentinel remains a four-legged quadruped. It is distinct from the four-wheel PUI89 AI NOMAD.

## 2. Inputs required before numerical sizing

| Input group | Required definition | Current status |
|---|---|---|
| Mission | Named inspection task, route, duration, operator role, required speed and stop/return behaviour | TBD |
| Environment | Surface classes, friction assumptions, slope, steps, gaps, obstacles, weather and temperature | TBD |
| Robot geometry | Body dimensions, stance, leg segment lengths, joint axes/ranges, foot geometry and clearances | TBD |
| Kinematics | Joint count and arrangement per leg, selected gait families, stance/swing timing and foot trajectories | TBD |
| Loading | Complete baseline mass, payload mass/location, centre of gravity and load cases | TBD |
| Performance | Walking speed, acceleration, turning, slope/step targets and endurance acceptance criteria | TBD |
| Safety | Stability margin, allowable impact loads, stop/recovery policy, derating and design factors | TBD |
| Electrical | Bus voltage, actuator/driver efficiency maps, compute/sensor duty cycle and battery reserve policy | TBD |

Unknown inputs must remain variables or explicit TBD entries. Do not replace missing mission data with a guessed motor model or an arbitrary payload.

## 3. Complete-robot mass budget

The approved preliminary target is **18–22 kg for the complete baseline robot**. Count the following in the total:

| Subsystem | Included items | Planned mass (kg) | Evidence / owner |
|---|---|---:|---|
| Main body and structural frame | Chassis, brackets, load-bearing covers and fasteners | TBD | CAD + material/part data |
| Four leg structures | Links, joint housings, bearings, shafts and structural fasteners | TBD | CAD + part data |
| Actuation and transmission | Motors, gearboxes, belts/gears, brakes if required, motor mounts | TBD | Exact datasheets + design |
| Feet and contact elements | Foot structures, compliant elements, replaceable pads | TBD | CAD + tests |
| Battery and BMS | Cells, enclosure, BMS, protection and mounting | TBD | Cell/BMS datasheets |
| Power electronics | Drivers, DC/DC, distribution, fuses, wiring harness | TBD | Datasheets + wiring design |
| Compute and storage | Onboard compute, storage, cooling and mounts | TBD | Exact datasheets |
| Baseline sensors | IMU, joint/foot sensing, cameras and other mission-independent sensors | TBD | Exact datasheets |
| Mission payload | Mission-specific sensors, illumination or instruments | Separate TBD | Mission approval |
| Covers and ingress protection | External covers, seals, guards and service panels | TBD | CAD + environmental test |
| Cables and connectors | Internal harnesses, connectors, strain relief | TBD | Harness estimate |
| **Complete baseline total** | Sum of all baseline rows; identify mission payload treatment explicitly | **Target 18–22** | Reviewed mass roll-up |

Rules:
- Do not double-count items included in a supplier assembly mass.
- Record estimated, datasheet, CAD-derived and measured masses separately.
- Add a mass contingency only after uncertainty is quantified; show it as a separate line, not hidden inside component estimates.
- Track payload separately until its inclusion in the formal configuration is approved.
- Reconcile the mass roll-up against the 18–22 kg target at each design review. If the target is infeasible, document the trade-off and seek a revised approval; do not silently weaken safety margins.

## 4. Joint-load and torque calculation method

### 4.1 Define each load case

At minimum, model:
1. Static standing on level ground.
2. Slow controlled walking, including single-, double- and multi-foot support phases as applicable to the chosen gait.
3. Acceleration, deceleration and turning.
4. Slope ascent/descent and lateral slope.
5. Step-up, step-down and obstacle clearance.
6. Foot impact, slip recovery and controlled stop.
7. Payload extremes and centre-of-gravity offsets.
8. A fault or degraded condition that requires a safe stop.

For each case, state robot mass, payload, posture, foot contacts, terrain assumptions, acceleration, uncertainty and design factor.

### 4.2 First-order support-force check

For a simplified static check only:

\[
W = m g, \qquad F_{z,\,foot} \approx \frac{m g}{n_s}
\]

where (m) is total supported mass, (g) is gravitational acceleration and (n_s) is the number of feet assumed to support the load. This equal-sharing approximation is **not** a dynamic leg-load prediction and must not be used alone to select actuators.

For dynamic cases, solve body and leg equilibrium with inertial terms, contact constraints and the selected gait. Use multibody simulation or a validated inverse-dynamics model.

### 4.3 Joint torque

For a leg Jacobian (J(q)) and foot/contact force vector (F):

\[
\tau_{joint} = J(q)^T F + \tau_{gravity} + \tau_{inertia} + \tau_{friction}
\]

Use consistent coordinate frames, sign conventions and units. Include the worst credible posture and contact geometry, not only a neutral standing pose. Validate the model against simulation and, later, instrumented bench measurements.

For a transmission with ratio (N = \omega_{motor}/\omega_{joint}) and efficiency \(\eta_g\), a first-order motor-side estimate is:

\[
\tau_{motor} \approx \frac{\tau_{joint}}{N\eta_g}, \qquad
\omega_{motor} = N\omega_{joint}
\]

This relation is only a sizing approximation. Gearbox efficiency varies with speed, torque, temperature and direction; include backlash, compliance, peak load, bearing limits and thermal duty.

### 4.4 Peak, continuous and RMS duty

Do not size an actuator from peak torque alone. For a repeating duty cycle with torque \(\tau_i\) over duration \(t_i\), a simplified RMS torque is:

\[
\tau_{RMS} = \sqrt{\frac{\sum_i \tau_i^2 t_i}{\sum_i t_i}}
\]

Compare peak torque, RMS/continuous torque, speed-torque envelope, allowable peak duration, thermal limits and life rating against the exact actuator and transmission datasheets. RMS torque is not a substitute for manufacturer thermal modelling or a full mission duty-cycle analysis.

### 4.5 Mechanical power

\[
P_{mech}(t) = \tau(t)\,\omega(t)
\]

Evaluate positive and regenerative/braking regions separately. Electrical input power must account for motor, driver and transmission losses. Do not assume regenerative energy is recovered unless the driver, battery and control system are designed and verified to accept it.

## 5. Actuator requirement sheet

Create one record per joint, not one generic motor choice for the entire robot.

| Field | Required value |
|---|---|
| Joint identifier / leg / axis | TBD |
| Joint range and mechanical stops | TBD |
| Required joint peak torque | Derived for each load case |
| Required continuous / RMS torque | Derived from mission duty cycle |
| Required joint speed and acceleration | Derived from gait and geometry |
| Output power and thermal dissipation | Derived and verified |
| Transmission ratio and efficiency map | TBD from candidate datasheet |
| Backlash, stiffness and bearing/radial load limits | TBD |
| Position/velocity/torque sensing | TBD |
| Driver voltage/current and peak duration | TBD |
| Environmental rating and service life | TBD |
| Manufacturer, exact part number, manufacturing country and origin evidence | Mandatory before evaluation |
| Firmware/software provenance and update controls | Mandatory before integration |
| Supplier ownership/control and replaceability review | Mandatory under PUI89 integrity policy |

Reject a candidate if its published continuous rating, speed-torque curve, thermal conditions, peak duration, mechanical limits or provenance cannot be verified.

## 6. Electrical power and battery sizing

Build a time-indexed mission profile. At each segment record duration and power for:
- Joint actuators and motor drivers, including idle/holding and transient loads.
- Onboard compute, storage and cooling.
- Sensors, illumination and communications.
- DC/DC conversion and distribution losses.
- Safety reserve, safe-stop and return-to-start energy.

Total battery-terminal energy is estimated by integrating the load profile:

\[
E_{load} = \int_0^T P_{battery}(t)\,dt
\]

For discrete mission segments:

\[
E_{load} \approx \sum_i P_{battery,i}\,t_i
\]

A preliminary nominal battery-energy requirement can be expressed as:

\[
E_{nominal} \geq \frac{E_{load}}{f_{usable}\,\eta_{system}}
\]

where (f_{usable}) is the approved usable fraction of nominal battery energy and \(\eta_{system}\) accounts for relevant conversion/distribution losses not already included in (P_{battery}). Define these terms consistently to avoid counting losses twice. Add an explicitly justified reserve for safe stop/return and battery ageing/temperature only after the mission and cell limits are known.

Also verify:
- Peak and continuous bus current, voltage sag and connector ratings.
- BMS current, temperature, cell-voltage and short-circuit protections.
- Cell chemistry, operating temperature, charge limits and transport constraints.
- Battery enclosure, impact protection, thermal propagation and service access.
- Low-state-of-charge behaviour, safe hold and controlled shutdown.
- Charging time and charger provenance/compatibility.

Energy capacity (Wh) alone is insufficient: peak power, current, thermal limits and safe reserve can be the binding constraints.

## 7. Mass–power–thermal iteration

Mass, torque, power and battery are coupled. More battery increases supported mass; more supported mass increases joint loads and energy use; larger actuators and transmissions increase mass and thermal load.

Use an iterative loop:
1. Establish mission and geometry assumptions.
2. Estimate subsystem masses and centre of gravity.
3. Calculate load cases and joint torque/speed.
4. Screen actuator/transmission candidates against verified datasheets.
5. Estimate electrical duty cycle and thermal dissipation.
6. Size battery and power electronics.
7. Update total mass and centre of gravity.
8. Recalculate loads and repeat until margins converge.
9. Record sensitivities and unresolved risks; do not hide a failed iteration.

A spreadsheet or script used for this process must expose assumptions, units, equations, source references, revision history and test status. No opaque single-number sizing.

## 8. Required evidence and design gates

| Gate | Evidence required to pass |
|---|---|
| M1 — Mission inputs | Approved representative mission, environment, operating envelope and measurable acceptance criteria |
| M2 — Mass roll-up | Traceable subsystem estimates, payload definition, uncertainty and total against 18–22 kg |
| M3 — Kinematics and load cases | Robot geometry, gait assumptions, contact cases and reproducible inverse-dynamics results |
| M4 — Actuator shortlist | Exact datasheets, verified torque-speed/thermal limits, provenance and interface compatibility |
| M5 — Power and battery | Time-based load profile, peak-current analysis, battery/BMS protection and reserve rationale |
| M6 — Simulation and bench | Reproducible simulation plus instrumented actuator, driver, power and thermal bench evidence |
| M7 — Controlled robot test | Approved risk assessment and measured results across staged configurations and surfaces |

A gate is not passed by completing a document alone; evidence must be reviewed against acceptance criteria. Simulation is not physical validation.

## 9. PUI89 integrity and safety constraints

- Apply the PUI89 zero China-origin and China-controlled dependency policy to components, manufacturers, suppliers, ownership/control, firmware, software, materials and data access.
- Unknown or unverifiable origin/provenance is a blocker, not an assumed pass.
- Prefer modular, repairable, replaceable interfaces and avoid single-vendor lock-in.
- No procurement, fabrication, installation or field deployment is authorised by this framework.
- No claim of payload, speed, endurance, fall resistance, terrain capability or actuator performance is permitted without measured evidence.
- Safety limits and emergency-stop behaviour must not depend solely on AI model outputs.

## 10. Current decision record

The 18–22 kg complete-robot target remains a preliminary engineering study target. Mission, dimensions, joint count, gait, payload, actuator architecture, battery chemistry/capacity, runtime, cost and supplier shortlist remain **TBD**. The next technical decision is to approve one representative supervised inspection mission and its measurable operating envelope. Only then should numerical torque and battery calculations be populated.
