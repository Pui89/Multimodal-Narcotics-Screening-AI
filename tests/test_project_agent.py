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
