# PUI89 Sentinel — All-Terrain Exploration & Inspection Robot

**Official project name:** PUI89 Sentinel — All-Terrain Exploration & Inspection Robot  
**Product identity:** Four-legged quadruped mobile inspection robot  
**Mission:** Supervised inspection, situational awareness and evidence capture in authorised industrial, infrastructure, logistics and selected outdoor environments.  
**Relationship to NOMAD:** Sentinel uses four articulated legs; PUI89 NOMAD is a separate four-wheel mobile assistant.  
**Development status:** Product concept and engineering requirements. No physical Sentinel prototype, field capability or sensor integration is claimed.

![PUI89 Sentinel quadruped robot-dog concept](docs/images/pui89-sentinel-quadruped-inspection-v3.svg)

*Concept illustration only. It is not evidence of a built, tested or validated robot.*

## Product direction

PUI89 Sentinel is being repositioned as a general-purpose **All-Terrain Exploration & Inspection Robot**, a general-purpose inspection platform; it does not include drug detection, X-ray payloads or chemical-identification functions. The product is intended to help authorised operators inspect environments, assets and visible conditions, collect traceable sensor evidence and report findings for human review.

### Target operating contexts

- Industrial facilities, plant rooms and infrastructure inspection.
- Warehouses, logistics yards, ports and authorised cargo areas.
- Selected container and confined-area inspection, subject to clearance, atmosphere and exit-route checks.
- Outdoor paths, paved surfaces, gravel, grass, soil, moderate slopes, steps and selected uneven terrain.
- Disaster-site reconnaissance from safe, authorised locations.
- Routine inspection patrols and documented condition monitoring.

These are target use cases, not validated deployments. Each site requires a risk assessment, operating permissions, environmental limits and task-specific verification.

## Mobility and physical design requirements

Sentinel is a four-legged robot with articulated legs, not a wheeled base. The mobility ambition is strong, agile and stable walking—not unrestricted movement everywhere.

- Controlled forward/reverse walking, turning, sidestepping and speed transitions.
- Terrain-aware gait selection and adaptive foot placement.
- IMU, joint-state and foot-contact estimation.
- Slip, stumble, obstacle and fall-risk detection.
- Managed centre of mass, payload envelope and power/thermal budget.
- Controlled stop, safe hold, supervised recovery and emergency-stop provisions.
- Local mapping and safe retreat planning where communications or GNSS are unavailable.

Candidate research methods include state estimation, gait planning, model-predictive control and whole-body control. These are candidate methods only, not selected or validated implementations.

**Terrain limits:** cliffs, deep water, unstable structures, hazardous atmospheres, inaccessible gaps, extreme slopes and any environment outside the validated operating envelope are no-go conditions. “All-terrain” is an engineering ambition, not a guarantee.

### Container and confined-area inspection

Before approaching or entering a container, the system must assess doorway width/height, threshold, body/leg clearance, floor condition, overhead and cargo hazards, localisation confidence and a viable exit route. It must support careful approach/alignment, controlled threshold step-over, low-light sensing, narrow-space navigation, mapping, turn/reverse/retreat and safe stop.

**Atmosphere safety:** RGB, depth and LiDAR do not certify breathable air or detect all hazardous gases. Entry requires site-authorised procedures and suitable calibrated atmosphere instruments where the risk assessment requires them. If clearance, footing, localisation, atmosphere status or exit route cannot be established, Sentinel must not enter or must stop and request operator assistance.

## Six Core Intelligence Groups

1. **Vision Intelligence** — scene understanding, object detection/classification, tracking, segmentation, depth and visual change/anomaly cues.
2. **Audio Intelligence** — speech interface, alarms, sirens and relevant acoustic events; no real-world speaker identity inference.
3. **Multimodal Intelligence** — context-aware combination of authorised image, audio, text, map and sensor/time-series evidence with provenance and uncertainty.
4. **Robotics Intelligence** — robot state, localisation, mapping, navigation, gait/motion planning and task-appropriate interaction.
5. **Action & Reaction Intelligence** — inspection task decomposition, bounded planning, event response, escalation, safe retreat and recovery proposals.
6. **Safety & Control Intelligence** — independent operating limits, permissions, verification, human approval, fault containment, safe hold and emergency-stop policy.

Safety policy is independent of model confidence. AI outputs are observations or bounded proposals, not direct authority to perform hazardous actions.

## Target sensor and compute architecture

| Capability | Candidate role | Status |
|---|---|---|
| RGB cameras | Visual inspection, scene context and evidence capture | Candidate |
| Depth camera | Near-field geometry and obstacle clearance | Candidate |
| 360° LiDAR | Mapping, localisation and obstacle awareness | Candidate |
| Thermal camera | Temperature-pattern observation where justified | Optional candidate |
| Microphones/speaker | Acoustic events and operator communication | Candidate |
| IMU + joint/foot sensors | Body state, gait and contact estimation | Required design function |
| Edge AI computer | Local perception, planning support and evidence handling | Candidate |
| Calibrated gas/atmosphere instruments | Specific atmosphere hazards when mission risk requires | Mission-specific; not included by default |

Exact manufacturers, part numbers, country of manufacture/origin, compatibility, supplier, dated price, lead time and warranty must be evidenced before procurement. No hardware has been selected or purchased through this specification.

## Safety, privacy and human oversight

- Operate only in authorised locations and within a documented operating envelope.
- Detect people and vehicles as dynamic obstacles; follow site traffic and exclusion rules.
- No autonomous enforcement, accusation, detention, search or coercive action.
- No biometric identity inference or voice identity recognition.
- Do not enter hazardous atmospheres or unstable structures based on camera/LiDAR interpretation alone.
- Stop safely on loss of localisation, unsafe footing, sensor disagreement, communications failure or unknown hazards.
- Preserve evidence provenance, timestamps, uncertainty, model/data version and operator review.
- Require human authorisation for consequential actions and site-specific procedures.

## Prototype cost — preliminary planning estimate

**Indicative allowance for one engineering prototype: ฿1,225,000–฿2,990,000.**

This is a high-uncertainty planning estimate for a custom four-legged platform, actuators and locomotion control, battery/power, core perception sensors, edge compute, integration and controlled testing. It is not a supplier quotation, verified BOM, fixed budget or evidence that a prototype exists.

Excludes engineering salaries, facilities, taxes/VAT, import duty, international freight, certification, production tooling, mass production and long-term maintenance. Thermal and specialist gas instruments may add cost depending on mission. Final cost requires a mass/payload definition, supplier-verified BOM and written quotations. No purchase is authorised.

## Development approach

1. Define mission scenarios, operating envelope and measurable acceptance criteria.
2. Build software workflows and simulation before hardware procurement.
3. Evaluate quadruped platform alternatives and non-Chinese-origin sourcing evidence.
4. Verify locomotion, stability, payload, endurance, thermal and environmental performance in controlled tests.
5. Conduct supervised site trials only after safety review and approvals.
6. Publish capability claims only when supported by reproducible evidence.

## Evidence and maturity boundary

Current status is **concept / requirements definition** for the physical robot. Software tools or simulated scenarios do not establish physical mobility, terrain capability, inspection accuracy or field readiness. No physical prototype, all-terrain performance, fall recovery, container entry, hazardous-atmosphere detection or industrial deployment is claimed.

## Architecture, validation and visual reference

- [Complete system blueprint](docs/COMPLETE_SYSTEM_BLUEPRINT.md)
- [Validation matrix](docs/VALIDATION_MATRIX.md)
- [Sentinel quadruped inspection concept v3](docs/images/pui89-sentinel-quadruped-inspection-v3.svg)

## Engineering requirements

- [All-Terrain Inspection Robot Dog requirements v0.2](docs/SENTINEL_ALL_TERRAIN_INSPECTION_ROBOT_DOG_REQUIREMENTS_V0.2.md)

## Project links

- [English website](https://pui89.github.io/sentinel.html)
- [เว็บไซต์ภาษาไทย](https://pui89.github.io/sentinel-th.html)
- [PUI89 portfolio](https://pui89.github.io/)
- [Hardware & Materials Sourcing](https://pui89.github.io/materials.html)
- [PUI89 engineering standard](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_SIMPLE_SAFE_PROFESSIONAL_STANDARD.md)

**PUI89 | Intelligent Systems. Verifiable Decisions. Safer Outcomes.**

## Operator Interaction Intelligence — PUI89 Sentinel

Sentinel uses the shared PUI89 interaction architecture for supervised operator communication:

- Receive spoken inspection instructions and support push-to-talk operator commands.
- Convert speech to text and provide concise spoken status, warning and task-completion reports.
- Explain a detected object, visible condition or sensor event by referring to the recorded evidence, timestamp, modality and uncertainty.
- Ask the operator to clarify ambiguous instructions and confirm consequential task changes.
- Support human review, correction, override and escalation.

**Sentinel-specific decision boundary:** interaction models may help communicate screening or inspection observations, but they must not independently identify a person, accuse someone of wrongdoing, declare a substance to be narcotics, or make a final screening or enforcement decision. All consequential findings require authorised human review and appropriate independent evidence.

**Recommended model candidates for Sentinel (not approved or integrated):**

| Model/tool | Role in Sentinel | Status |
|---|---|---|
| [openai/whisper-small](https://huggingface.co/openai/whisper-small) | Operator speech-to-text for push-to-talk inspection instructions; evaluate noisy field conditions | PENDING_REVIEW |
| [microsoft/Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct) | Optional operator dialogue, clarification and report phrasing; higher-resource candidate | PENDING_REVIEW |
| [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) | English spoken status and warning reports; Thai TTS is not established | PENDING_REVIEW |
| [qualcomm/YamNet](https://huggingface.co/qualcomm/YamNet) | Selected environmental audio-event labels, subject to sensor and false-alarm testing | PENDING_REVIEW |
| [Silero VAD](https://github.com/snakers4/silero-vad) | Speech-segment detection for operator communication | PENDING_REVIEW |
| [HuggingFaceTB/SmolVLM2-500M-Video-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct) | Optional bounded visual descriptions to assist human review; never a screening verdict | PENDING_REVIEW |

No candidate may identify a person, determine that a substance is narcotics, accuse anyone, or issue a final screening/enforcement decision. Do not add openWakeWord's included pretrained weights at this stage because their CC BY-NC-SA 4.0 terms require separate review.

**Maturity:** proposed operator-interface configuration only. No interaction model, microphone, speaker or voice pipeline is claimed as installed, integrated or validated.

## World-Class Engineering Standard v1.0

This product follows the [PUI89 World-Class Engineering Standard v1.0](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_WORLD_CLASS_ENGINEERING_STANDARD_V1.0.md), alongside the [PUI89 Simple, Safe & Professional Engineering Standard](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_SIMPLE_SAFE_PROFESSIONAL_STANDARD.md). The shared standard defines requirements traceability, Shared AI Core contracts, PTI evaluation, simulation, safety, hardware provenance, cost engineering, verification and release gates. Product capabilities remain subject to their stated evidence and validation boundaries; this reference does not imply that a gate has been passed.


## PUI89 Technical Visual — AI workflow

![PUI89 Sentinel quadruped robot inspection AI workflow with sensor fusion, terrain perception, safe route planning and operator supervision.](docs/images/pui89-technical-visual.svg)

*Proposed quadruped inspection architecture. No physical Sentinel prototype, gait capability, sensor integration or field validation is claimed.*

This diagram follows the [PUI89 Technical Visual Standard v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/PUI89_TECHNICAL_VISUAL_STANDARD_V1.0.md). It explains the proposed product-specific AI workflow and does not imply unverified implementation or physical capability.

## Portfolio consistency and founder-approved requirements

**PUI89 Sentinel — All-Terrain Exploration & Inspection Robot**

Founder-approved sequencing: define the first supervised inspection mission, target site/environment, operating envelope, hazards, human roles and measurable acceptance criteria before selecting hardware. Current physical status remains concept/requirements unless separate bench or field evidence is linked.

**ข้อกำหนดภาษาไทย**

ลำดับที่ผู้ก่อตั้งอนุมัติ: กำหนดภารกิจตรวจสอบแบบมีมนุษย์กำกับ พื้นที่และสภาพแวดล้อม ขอบเขตการทำงาน อันตราย บทบาทมนุษย์ และเกณฑ์ยอมรับที่วัดผลได้ ก่อนเลือกฮาร์ดแวร์ สถานะทางกายภาพยังเป็นแนวคิด/ข้อกำหนด เว้นแต่มีหลักฐาน bench หรือ field แยกต่างหาก

**Portfolio boundary:** PUI89 has exactly six active products. Shared AI Core is infrastructure, not a product. Extreme Flood Rescue AI is inactive as a standalone product; preserve historical records but do not present it as an active product.
