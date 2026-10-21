import math

import pytest

from narcotics_platform.fusion import ModalityEvidence, MultimodalFusion


def test_fusion_prefers_multi_modal_agreement():
    result = MultimodalFusion().fuse([
        ModalityEvidence("rgb", "amphetamine", 0.8),
        ModalityEvidence("depth", "amphetamine", 0.7),
        ModalityEvidence("thermal", "unknown_substance", 0.3),
    ])
    assert result.label == "amphetamine"
    assert result.agreement > 0.5


@pytest.mark.parametrize(
    "bad_value",
    [math.nan, math.inf, -math.inf, -0.01, 1.01, True, "0.8", None],
)
@pytest.mark.parametrize("field", ["confidence", "quality"])
def test_modality_evidence_rejects_invalid_numeric_values(field, bad_value):
    values = {"modality": "rgb", "label": "unknown_substance", "confidence": 0.8, "quality": 1.0}
    values[field] = bad_value
    with pytest.raises(ValueError):
        ModalityEvidence(**values)


@pytest.mark.parametrize("field", ["modality", "label"])
@pytest.mark.parametrize("bad_value", ["", "   ", None, 3])
def test_modality_evidence_rejects_missing_or_invalid_identity(field, bad_value):
    values = {"modality": "rgb", "label": "unknown_substance", "confidence": 0.8, "quality": 1.0}
    values[field] = bad_value
    with pytest.raises(ValueError):
        ModalityEvidence(**values)
