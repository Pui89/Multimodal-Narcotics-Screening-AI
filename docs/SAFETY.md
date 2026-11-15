# PUI89 Sentinel — Safety Requirements

Sentinel is a proposed quadruped exploration and inspection robot. It is not a built or validated physical system. “Explore Anywhere” does not override a defined operating envelope, site permission or safety review.

## Mission and human authority

- An authorised operator defines the mission, permitted area, route limits, data policy and abort conditions.
- Human oversight remains mandatory for consequential decisions and recovery.
- No autonomous enforcement, pursuit, restraint, forced access or weaponisation.
- No facial recognition, biometric identification, person scoring or covert unrestricted surveillance.

## Motion and terrain safety

- Physical movement must remain disabled until an independent low-level controller, emergency stop, watchdog and safety interlocks are tested.
- Stop/safe-hold on uncertain footing, obstacle clearance, localisation, joint/foot state, sensor health, communications, battery or thermal status.
- Deep water, cliffs, unstable structures, fire, explosive/hazardous atmospheres, extreme slopes and unknown confined spaces are no-go until specifically engineered and validated.
- A camera, depth sensor or LiDAR cannot certify structural integrity or breathable air. Use site procedures and suitable calibrated instruments where required.
- Simulation is not proof of physical stability or safe locomotion.

## AI and evidence safety

- AI models provide observations and bounded proposals only; they do not directly authorise actuators.
- Preserve UNKNOWN and CONFLICT rather than forcing a confident answer.
- Keep safety rules independent from model confidence and language-model output.
- Record provenance, timestamps, calibration, quality, uncertainty, software/model version and operator decisions.
- Minimise personal data and retain only what is necessary and authorised.

## Current boundary

No physical prototype, validated locomotion, terrain capability, sensor integration or field safety performance is claimed. No narcotics-screening, chemical-identification or X-ray function belongs to the current product.
