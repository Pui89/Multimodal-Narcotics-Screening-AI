# Sentinel Scope Migration & Legacy Artifact Register

**Current product:** PUI89 Sentinel — All-Terrain Exploration & Inspection Robot  
**Form factor:** Four-legged AI quadruped  
**Tagline:** Explore Anywhere  
**Current stage:** Stage 1 — new concept and requirements baseline  
**Portfolio distinction:** AI NOMAD remains a separate four-wheel mobile assistant; AI HOME remains a separate four-wheel indoor assistant.

## Why this register exists

This repository originated under a former Multimodal Narcotics Screening AI direction. The product has since changed. Sentinel is now a general-purpose quadruped for supervised exploration, environmental awareness, inspection and evidence capture. The former narcotics-screening mission is discontinued and is not part of the current product.

## Current scope

Active Sentinel work must address:
- quadruped mechanical and locomotion requirements;
- environmental perception and scene understanding;
- depth/spatial awareness, terrain and traversability estimation;
- mapping/localisation and uncertainty;
- robot body state, gait, joint and foot-contact awareness;
- inspection missions, visible asset/change observations and evidence;
- independent safety supervision, human authority and fail-safe behaviour.

Out of scope: narcotics or substance screening, X-ray/baggage screening, chemical identification, enforcement workflows, autonomous policing, weapons, pursuit, restraint, forced entry, biometric identification, drone or aerial flight.

## Migration rules

1. The root README, Product Brief, current system specification and this register define the active product scope.
2. Historical code, documents, schemas, dashboards, test fixtures, workflows and artwork from the former screening direction are legacy artifacts. They are not active Sentinel features, product evidence or capability claims.
3. Preserve Git history and legacy files during this transition. Do not bulk-delete, overwrite or rename historical assets without a reviewed file-level plan.
4. Do not execute legacy screening applications or workflows as Sentinel product demos.
5. Reuse any generic component only after a separate review of purpose, safety, architecture, provenance, licence, security and tests.
6. Replace old project identifiers only where they are part of the active Sentinel configuration or current public interface. Historical records must remain clearly identifiable as historical.
7. Reset product maturity and evidence baselines. Former screening metrics, CI results, readiness percentages and dataset records do not transfer to quadruped exploration.
8. Update website and Shared AI Core references to distinguish Sentinel quadruped from four-wheel NOMAD and four-wheel HOME.

## Known legacy areas

The default-branch scan identified screening-era material in the following areas. This is an initial bounded inventory, not a claim that every occurrence has been enumerated:

- Documentation: screening readiness, dataset plans, modality fusion, X-ray/chemical, baggage inspection, enforcement boundaries, screening roadmaps, historical status and old product/marketing briefs.
- Source packages: legacy screening/fusion pipelines and adapters under old screening-oriented namespaces.
- Applications and demos: former screening dashboards, synthetic screening examples and demo entrypoints.
- Schemas and data: screening event/review schemas, old project identifiers, screening labels and synthetic evaluation records.
- Configuration: old platform mission names, modality states and screening-specific robotics profiles.
- Tests and workflows: tests that exercise former screening contracts and workflow names.
- Visual assets: airport/baggage scenes, screening dashboards, X-ray/chemical illustrations and screening-themed robot storyboards.
- External references: historical links to the old repository name.

## Treatment by artifact class

| Artifact class | Treatment |
|---|---|
| Current README, product brief, safety, system spec, validation and active integration profile | Rewrite to quadruped exploration/inspection |
| Generic utilities with no screening assumptions | Review individually before reuse |
| Screening-specific application/source modules | Keep isolated as legacy; do not present or run as current Sentinel |
| Screening schemas, fixtures and test reports | Preserve as historical records; do not use as quadruped evidence |
| Screening images, dashboards and storyboards | Retain for history only; replace in active product presentation |
| Old workflows and automation | Disable from current product claims; review before any future execution |
| Git history and historical PR references | Preserve; do not rewrite history |

## Evidence and safety boundary

A concept image is not a physical prototype. A unit test is not a locomotion test. A simulation is not field validation. A sensor listed in a file is not proof of purchase, integration or calibration. No unrestricted all-terrain capability is claimed. No former screening metric or capability is part of the new Sentinel baseline.

## Completion criteria

- [x] Current product identity and portfolio distinction stated in core README and product brief.
- [x] Active robot concept, system blueprint, safety and validation matrix rewritten for quadruped exploration.
- [x] Current Shared AI Core adoption profile rewritten for terrain, quadruped state and inspection.
- [ ] Full file-level inventory of every legacy reference.
- [ ] Reusable generic code reviewed and separated from legacy modules.
- [ ] Legacy-only code, docs, schemas, demos, images and workflows isolated through reviewed, reversible changes.
- [ ] Repository-wide tests and website link/QR checks completed after migration.

This migration is in progress. Do not describe the entire repository as fully migrated until all remaining completion criteria are supported by evidence.
