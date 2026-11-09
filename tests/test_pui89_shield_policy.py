"""Standard-library regression tests for the PUI89 SHIELD reference policy."""
import json
import unittest
from pathlib import Path

from pui89_shield_policy import (
    HazardAssessment,
    WarningState,
    classify_warning,
    proposal_requires_human_review,
)


ROOT = Path(__file__).resolve().parents[1]


class ShieldWarningPolicyTests(unittest.TestCase):
    def test_valid_low_risk_evidence_is_normal(self):
        self.assertEqual(classify_warning(HazardAssessment(
            observation_valid=True, severity="low", evidence_refs=("ev-001",)
        )), WarningState.NORMAL)

    def test_advisory_is_preserved(self):
        self.assertEqual(classify_warning(HazardAssessment(
            observation_valid=True, advisory=True, evidence_refs=("ev-002",)
        )), WarningState.ADVISORY)

    def test_high_severity_is_warning(self):
        self.assertEqual(classify_warning(HazardAssessment(
            observation_valid=True, severity="high", evidence_refs=("ev-003",)
        )), WarningState.WARNING)

    def test_critical_severity_is_critical(self):
        self.assertEqual(classify_warning(HazardAssessment(
            observation_valid=True, severity="critical", evidence_refs=("ev-004",)
        )), WarningState.CRITICAL)

    def test_missing_observation_fails_degraded_not_normal(self):
        self.assertEqual(classify_warning(HazardAssessment(
            observation_valid=False
        )), WarningState.UNKNOWN_DEGRADED)

    def test_conflicting_sensors_fail_degraded(self):
        self.assertEqual(classify_warning(HazardAssessment(
            observation_valid=True, sensor_conflict=True
        )), WarningState.UNKNOWN_DEGRADED)

    def test_unsubstantiated_hazard_fails_degraded(self):
        self.assertEqual(classify_warning(HazardAssessment(
            observation_valid=True, severity="critical"
        )), WarningState.UNKNOWN_DEGRADED)

    def test_confirmed_imminent_hazard_requires_evidence(self):
        self.assertEqual(classify_warning(HazardAssessment(
            observation_valid=True, imminent_hazard_confirmed=True
        )), WarningState.UNKNOWN_DEGRADED)

    def test_confirmed_imminent_hazard_with_evidence_is_emergency(self):
        self.assertEqual(classify_warning(HazardAssessment(
            observation_valid=True, imminent_hazard_confirmed=True,
            evidence_refs=("ev-009",)
        )), WarningState.EMERGENCY)

    def test_physical_action_proposal_requires_human_review(self):
        self.assertTrue(proposal_requires_human_review(physical_action=True))

    def test_nonphysical_report_does_not_claim_actuation_authority(self):
        self.assertFalse(proposal_requires_human_review(physical_action=False))


class ShieldContractTests(unittest.TestCase):
    def test_event_schema_has_required_contract_fields(self):
        schema_path = ROOT / "schemas/pui89-shield-event.schema.json"
        if not schema_path.is_file():
            schema_path = ROOT / "schemas/pui89-shield-warning-event-v1.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        required = set(schema["required"])
        expected = {
            "event_id", "schema_version", "project", "component", "observed_at",
            "source_id", "value", "unit", "quality", "evidence_refs",
            "uncertainty", "hazard", "severity", "warning_state", "decision",
            "rationale", "human_approval_required", "software_version"
        }
        self.assertTrue(expected.issubset(required))

    def test_profile_keeps_physical_validation_unverified(self):
        profile = json.loads((ROOT / ".github/pui89-resilience.json").read_text(encoding="utf-8"))
        self.assertEqual(profile["shield_system"]["physical_validation"], "NOT_VERIFIED")
        self.assertEqual(len(profile["shield_system"]["warning_states"]), 6)

    def test_scenario_catalog_is_explicitly_not_test_evidence(self):
        catalog = json.loads((ROOT / "docs/PUI89_SHIELD_TEST_SCENARIOS.json").read_text(encoding="utf-8"))
        self.assertEqual(catalog["status"], "scenario_catalog_only_not_simulation_evidence")
        self.assertIn("project", catalog)
        self.assertGreaterEqual(len(catalog["scenarios"]), 13)

    def test_six_project_matrix_covers_vehicle_projects_and_existing_projects(self):
        matrix = (ROOT / "docs/PUI89_SHIELD_PROJECT_IMPLEMENTATION_MATRIX.md").read_text(encoding="utf-8")
        for project in ("Coconut Harvest AI", "Flood Rescue AI",
                        "Multimodal Screening AI", "Homeguard AI Nomad",
                        "AI Robot Car", "AI Robot Motorcycle"):
            self.assertIn(project, matrix)
        self.assertIn("Repository not found / not created", matrix)


if __name__ == "__main__":
    unittest.main()


class SharedCoreAdapterTests(unittest.TestCase):
    def test_observation_preserves_provenance_and_degraded_quality(self):
        from pui89_shield_policy import build_core_observation
        item = build_core_observation(
            observation_id="obs-1", observed_at="2026-11-09T10:00:00Z",
            source_id="camera-1", source_type="sensor", modality="rgb",
            payload={"asset_ref": "fixture://image-1"}, quality_status="degraded",
            provenance={"recorded_at": "2026-11-09T10:00:01Z", "dataset_or_file": "synthetic-fixture"},
            uncertainty={"description": "synthetic fixture", "value": 0.8, "method": "test-only"},
        )
        self.assertEqual(item["schema_version"], "0.1.0")
        self.assertEqual(item["quality"]["status"], "degraded")
        self.assertEqual(item["provenance"]["dataset_or_file"], "synthetic-fixture")

    def test_world_state_keeps_unknowns_and_conflicts(self):
        from pui89_shield_policy import build_core_world_state
        item = build_core_world_state(
            state_id="state-1", updated_at="2026-11-09T10:00:00Z",
            evidence_refs=["obs-1", "obs-1"], unknowns=["chemical modality unavailable"],
            conflicts=["two synthetic sources disagree"],
        )
        self.assertEqual(item["evidence_refs"], ["obs-1"])
        self.assertIn("chemical modality unavailable", item["unknowns"])
        self.assertTrue(item["conflicts"])

    def test_proposal_is_advisory_and_never_authorizes_execution(self):
        from pui89_shield_policy import build_human_review_proposal
        item = build_human_review_proposal(
            proposal_id="proposal-1", created_at="2026-11-09T10:00:00Z",
            objective="request qualified human review", action_id="review-1",
            description="Ask an authorised reviewer to inspect the evidence",
            risk_level="moderate", preconditions=["evidence provenance available"],
            expected_effect="human assessment", evidence_refs=["obs-1"],
        )
        self.assertEqual(item["authority"]["mode"], "advisory_only")
        self.assertIs(item["authority"]["human_approval_required"], True)
        self.assertIs(item["authority"]["execution_authorized"], False)

    def test_failure_report_records_evidence_and_open_status(self):
        from pui89_shield_policy import build_core_failure_report
        item = build_core_failure_report(
            failure_id="failure-1", occurred_at="2026-11-09T10:00:00Z",
            component="screening-input", severity="moderate",
            summary="Synthetic sensor disagreement", observed_result="conflict",
            evidence_refs=["obs-1"], response_status="investigating",
        )
        self.assertEqual(item["schema_version"], "0.1.0")
        self.assertEqual(item["response_status"], "investigating")
        self.assertEqual(item["evidence_refs"], ["obs-1"])

    def test_invalid_contract_values_are_rejected(self):
        from pui89_shield_policy import build_core_observation, build_human_review_proposal
        with self.assertRaises(ValueError):
            build_core_observation(
                observation_id="obs-2", observed_at="now", source_id="cam",
                source_type="unknown-device", modality="rgb", payload=None,
                quality_status="usable", provenance={"recorded_at": "now"},
            )
        with self.assertRaises(ValueError):
            build_human_review_proposal(
                proposal_id="p", created_at="now", objective="review",
                action_id="a", description="review", risk_level="unbounded",
                preconditions=[], expected_effect="review",
            )
