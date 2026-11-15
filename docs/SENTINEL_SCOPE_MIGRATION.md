# Sentinel scope migration and legacy artifact register

**Current product identity:** PUI89 Sentinel — All-Terrain Inspection Robot Dog (quadruped).  
**Current mission:** supervised inspection, situational awareness and evidence capture in authorised industrial, infrastructure, logistics and selected outdoor environments.  
**Status:** concept and engineering requirements; no physical robot or field capability is validated.

## Why this register exists

The repository previously contained a different project direction called “Multimodal Narcotics Screening AI”. That earlier work left documentation, scripts, schemas, workflows, dashboards, tests, robot models and artwork with screening-related terminology. The current Sentinel product is not a narcotics-screening product. It does not claim chemical identification, X-ray screening, narcotics detection or enforcement capability.

## Migration policy

1. The current product definition is the quadruped inspection robot dog described in the root README and current product brief.
2. Historical screening code and artifacts are not automatically considered Sentinel features or evidence of quadruped capability.
3. Preserve Git history and existing files during this scope transition. Do not perform bulk deletion or rename operations without a reviewed migration plan.
4. Where legacy files remain necessary for provenance, mark them as historical/legacy and link to this register.
5. New active Sentinel documentation must use quadruped inspection terminology and must not reuse screening-specific claims, interfaces or images.
6. Any code reused from legacy work must undergo a separate relevance, security, licence, architecture and test review before adoption.
7. Update the shared AI Core product mapping to Sentinel quadruped capabilities: perception, terrain/traversability, localisation/motion state, inspection evidence, uncertainty, safe hold and supervised recovery.

## Known legacy indicators

The following terms and paths were found in the default-branch repository search during this review. This is a bounded discovery list, not an exhaustive inventory of every occurrence:

- Former project title: “Multimodal Narcotics Screening AI”.
- Screening-specific documents such as docs/PRODUCT_BRIEF.md (now rewritten), docs/SCREENING_PRODUCT_READINESS.md, docs/MULTIMODAL_SCREENING_ROBOT_CONCEPT.md, and older screening roadmaps.
- Screening-oriented code namespaces and modules such as src/narcotics_platform/, tools/pui89_screening_model_adapter.py, schemas/screening_event.schema.json and examples/multimodal_screening_demo.py.
- Older workflows, robot descriptions, demos and SVG/3D artwork whose filenames or content refer to screening/narcotics.
- Old security and integration documents that described screening data, chemical evidence or chain-of-custody workflows.

The presence of these files is not a statement that they are currently maintained, deployed, connected to hardware or part of the Sentinel baseline.

## Validation boundary

- A quadruped concept illustration is not a physical prototype.
- A software unit test is not a locomotion or sensor-integration test.
- A simulation result is not a physical terrain or safety validation.
- A sensor name in documentation is not proof that the sensor has been purchased, integrated, calibrated or tested.
- No narcotics, chemical-identification, X-ray or enforcement capability is part of the Sentinel baseline.

## Next migration sequence

1. Maintain a complete file-level inventory of legacy references across the repository.
2. Classify each file as historical archive, reusable generic component, or obsolete artifact.
3. Review reusable components individually; preserve tests and provenance.
4. Mark or relocate historical-only material in a dedicated, clearly labelled legacy area through small pull requests.
5. Remove obsolete assets only after explicit review, dependency checks and confirmation that history/recovery requirements are met.
6. Run the repository test suite and verify active README/docs/workflows consistently describe Sentinel as a quadruped inspection robot.

This register documents a scope boundary. It does not claim the entire repository migration is complete.
