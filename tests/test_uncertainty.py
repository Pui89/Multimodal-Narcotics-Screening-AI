import math

import pytest

from narcotics_platform.uncertainty import estimate_uncertainty


def test_degraded_inputs_increase_uncertainty():
    good = estimate_uncertainty(0.9, 1.0, 1.0, 0.0)
    degraded = estimate_uncertainty(0.9, 0.5, 0.4, 0.7)
    assert degraded.uncertainty > good.uncertainty


@pytest.mark.parametrize(
    "bad_value",
    [math.nan, math.inf, -math.inf, -0.01, 1.01, True, "0.8", None],
)
@pytest.mark.parametrize("position", [0, 1, 2, 3])
def test_uncertainty_rejects_invalid_probability_inputs(position, bad_value):
    values = [0.8, 0.9, 1.0, 0.0]
    values[position] = bad_value
    with pytest.raises(ValueError):
        estimate_uncertainty(*values)
