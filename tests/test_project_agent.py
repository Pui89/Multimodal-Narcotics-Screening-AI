from agents.project_agent import run_agent


def test_unauthorised_context_is_held():
    assert run_agent({}).recommendation == "VERIFY_AUTHORITY_AND_PROCEDURE"


def test_conflicting_inputs_refer_to_human():
    d = run_agent({"authorised_context": True, "modalities": ["image", "sensor"],
                   "conflicting_inputs": True})
    assert d.recommendation == "REFER_TO_QUALIFIED_HUMAN"


def test_no_chemical_identity_claim():
    d = run_agent({"authorised_context": True, "modalities": ["image"]})
    assert d.requires_human_approval is True
    assert d.actuator_command is None
    assert "chemical identity" in " ".join(d.reasons)


def test_empty_modalities_requests_data():
    assert run_agent({"authorised_context": True}).status == "NEED_DATA"


def test_blank_modality_name_is_rejected():
    assert run_agent({"authorised_context": True, "modalities": ["   "]}).status == "NEED_DATA"


def test_non_dictionary_observation_is_rejected():
    import pytest

    with pytest.raises(TypeError, match="observation must be a dictionary"):
        run_agent(None)


def test_failed_sensor_check_stops_triage():
    d = run_agent({"sensor_ok": False, "authorised_context": True, "modalities": ["image"]})
    assert d.status == "STOP"
    assert d.recommendation == "CHECK_SENSOR_AND_CHAIN_OF_CUSTODY"
    assert d.requires_human_approval is True
    assert d.actuator_command is None


def test_unreviewed_record_always_routes_to_human():
    d = run_agent({"authorised_context": True, "modalities": ["image", "sensor"]})
    assert d.status == "REVIEW_REQUIRED"
    assert d.recommendation == "REFER_TO_QUALIFIED_HUMAN"
    assert d.actuator_command is None


def test_recorded_review_does_not_claim_chemical_identity():
    d = run_agent({
        "authorised_context": True,
        "modalities": ["image", "sensor"],
        "human_reviewed": True,
    })
    assert d.status == "REVIEW_RECORDED"
    assert d.requires_human_approval is True
    assert d.actuator_command is None
    assert "chemical-identification claim" in " ".join(d.reasons)
