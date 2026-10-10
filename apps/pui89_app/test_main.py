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


if __name__ == "__main__":
    unittest.main()
