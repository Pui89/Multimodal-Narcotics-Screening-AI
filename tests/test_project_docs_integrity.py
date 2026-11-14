"""Documentation smoke tests for the current Sentinel inspection-robot identity."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CONCEPT = "docs/images/pui89-sentinel-quadruped-inspection-v3.svg"


def test_core_project_evidence_files_exist():
    required = [
        "README.md",
        "docs/COMPLETE_SYSTEM_BLUEPRINT.md",
        "docs/VALIDATION_MATRIX.md",
        CONCEPT,
    ]
    missing = [path for path in required if not (ROOT / path).is_file()]
    assert not missing, f"Missing project evidence/documentation files: {missing}"


def test_readme_links_to_architecture_validation_and_visual():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for relative_path in (
        "docs/COMPLETE_SYSTEM_BLUEPRINT.md",
        "docs/VALIDATION_MATRIX.md",
        CONCEPT,
    ):
        assert relative_path in readme, f"README should link to {relative_path}"


def test_sentinel_robot_concept_svg_is_well_formed():
    root = ET.parse(ROOT / CONCEPT).getroot()
    assert root.tag.endswith("svg"), "Sentinel concept must have an SVG root element"


def test_readme_keeps_human_review_and_evidence_limits_explicit():
    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    assert "human review" in readme
    assert "not validated" in readme
    assert "narcotics-screening" not in readme
    assert "multimodal screening" not in readme
