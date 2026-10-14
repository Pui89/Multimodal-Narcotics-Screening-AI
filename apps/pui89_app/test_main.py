import unittest
from apps.pui89_app.main import ScreenRequest, screen


class ScreeningAppTests(unittest.TestCase):
    def test_insufficient_sensors_returns_unknown(self):
        result = screen(ScreenRequest(observation_id="a", rgb_valid=False,
            depth_valid=False, timestamp_skew_ms=0, visual_anomaly_score=.9,
            temporal_consistency_score=.8, ood_score=.1))
        self.assertEqual(result["decision"], "UNKNOWN")
        self.assertFalse(result["chemical_identity_established"])

    def test_high_ood_requires_review(self):
        result = screen(ScreenRequest(observation_id="b", rgb_valid=True,
            depth_valid=True, timestamp_skew_ms=2, visual_anomaly_score=.3,
            depth_consistency_score=.9, temporal_consistency_score=.9, ood_score=.8))
        self.assertEqual(result["decision"], "UNKNOWN")
        self.assertEqual(result["review_status"], "HUMAN_REVIEW")
        self.assertFalse(result["enforcement_action_authorized"])

    def test_no_chemical_claim(self):
        result = screen(ScreenRequest(observation_id="c", rgb_valid=True,
            depth_valid=True, timestamp_skew_ms=2, visual_anomaly_score=.1,
            depth_consistency_score=.9, temporal_consistency_score=.9, ood_score=.1))
        self.assertFalse(result["chemical_identity_established"])
        self.assertFalse(result["actuator_commands_sent"])


    def test_timestamp_skew_returns_unknown(self):
        result = screen(ScreenRequest(observation_id="skew", rgb_valid=True,
            depth_valid=True, timestamp_skew_ms=51, visual_anomaly_score=.2,
            depth_consistency_score=.9, temporal_consistency_score=.9, ood_score=.1))
        self.assertEqual(result["decision"], "UNKNOWN")
        self.assertIn("TIMESTAMP_SKEW_EXCEEDED", result["reasons"])

    def test_spatial_contradiction_returns_unknown(self):
        result = screen(ScreenRequest(observation_id="spatial", rgb_valid=True,
            depth_valid=True, timestamp_skew_ms=1, visual_anomaly_score=.2,
            depth_consistency_score=.2, temporal_consistency_score=.9, ood_score=.1))
        self.assertEqual(result["decision"], "UNKNOWN")
        self.assertIn("SPATIAL_EVIDENCE_CONTRADICTION", result["reasons"])

    def test_temporal_inconsistency_returns_unknown(self):
        result = screen(ScreenRequest(observation_id="temporal", rgb_valid=True,
            depth_valid=True, timestamp_skew_ms=1, visual_anomaly_score=.2,
            depth_consistency_score=.9, temporal_consistency_score=.2, ood_score=.1))
        self.assertEqual(result["decision"], "UNKNOWN")
        self.assertIn("TEMPORAL_EVIDENCE_INCONSISTENT", result["reasons"])

    def test_anomaly_hypothesis_still_requires_review(self):
        result = screen(ScreenRequest(observation_id="anomaly", rgb_valid=True,
            depth_valid=True, timestamp_skew_ms=1, visual_anomaly_score=.9,
            depth_consistency_score=.9, temporal_consistency_score=.9, ood_score=.5))
        self.assertEqual(result["decision"], "SCREENING_ANOMALY_HYPOTHESIS")
        self.assertEqual(result["review_status"], "HUMAN_REVIEW")
        self.assertFalse(result["enforcement_action_authorized"])
        self.assertFalse(result["actuator_commands_sent"])

    def test_invalid_scores_are_rejected_by_schema(self):
        from pydantic import ValidationError
        with self.assertRaises(ValidationError):
            ScreenRequest(observation_id="bad", rgb_valid=True, depth_valid=True,
                timestamp_skew_ms=0, visual_anomaly_score=1.2,
                temporal_consistency_score=.8, ood_score=.1)


if __name__ == "__main__":
    unittest.main()
