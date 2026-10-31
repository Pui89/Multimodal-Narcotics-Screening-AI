import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from pui89_screening_model_adapter import adapt_screening_mock

def request():
    return {"request_id":"screen-1","timestamp":"2026-11-01T00:00:01Z",
      "evidence":{"source_id":"fixture-1","source_ref":"synthetic://screening/1",
        "timestamp":"2026-11-01T00:00:00Z","evidence_kind":"synthetic","lineage":["unit-test"]},
      "mock_observation":{"modality_observations":[
        {"modality":"rgb","context":"synthetic image context"},
        {"modality":"thermal","context":"synthetic thermal context"}]}}

class ScreeningModelAdapterTests(unittest.TestCase):
    def test_valid_fixture_always_requests_human_review(self):
        r=adapt_screening_mock(request())
        self.assertEqual(r["project_id"],"multimodal_narcotics_screening")
        self.assertEqual(r["policy_result"]["action"],"REQUEST_HUMAN_REVIEW")
        self.assertEqual(r["proposed_actions"],[])
        self.assertFalse(r["physical_actuation_permitted"])
    def test_unknown_modality_rejected(self):
        q=request(); q["mock_observation"]["modality_observations"][0]["modality"]="chemical_sensor"
        with self.assertRaises(ValueError): adapt_screening_mock(q)
    def test_chemical_identity_key_rejected(self):
        q=request(); q["mock_observation"]["chemical_identity"]="cocaine"
        with self.assertRaises(ValueError): adapt_screening_mock(q)
    def test_guilt_or_suspect_score_rejected(self):
        q=request(); q["mock_observation"]["suspect_score"]=0.9
        with self.assertRaises(ValueError): adapt_screening_mock(q)
    def test_enforcement_action_rejected(self):
        q=request(); q["mock_observation"]["enforcement_action"]="detain"
        with self.assertRaises(ValueError): adapt_screening_mock(q)
    def test_top_level_chemical_identity_rejected(self):
        q=request(); q["chemical_identity"]="cocaine"
        with self.assertRaises(ValueError): adapt_screening_mock(q)
    def test_hardware_command_rejected(self):
        q=request(); q["robot_command"]={"approach":"target"}
        with self.assertRaises(ValueError): adapt_screening_mock(q)
if __name__=="__main__": unittest.main()
