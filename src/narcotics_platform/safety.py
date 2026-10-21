from __future__ import annotations

from dataclasses import dataclass
import math


def _is_finite_number(value: int | float) -> bool:
    """Return False for values that cannot be safely checked for finiteness."""
    try:
        return math.isfinite(value)
    except (OverflowError, TypeError, ValueError):
        return False


@dataclass(frozen=True)
class NavigationState:
    localization_confidence: float
    obstacle_distance_m: float
    human_in_exclusion_zone: bool = False
    emergency_stop: bool = False


class SafetyGate:
    """Fail-closed software motion gate; this is not a certified safety controller."""

    def __init__(
        self,
        min_localization_confidence: float = 0.70,
        min_obstacle_distance_m: float = 0.50,
    ) -> None:
        if (
            isinstance(min_localization_confidence, bool)
            or not isinstance(min_localization_confidence, (int, float))
            or not _is_finite_number(min_localization_confidence)
            or not 0.0 <= min_localization_confidence <= 1.0
        ):
            raise ValueError("min_localization_confidence must be a finite number in [0, 1]")
        if (
            isinstance(min_obstacle_distance_m, bool)
            or not isinstance(min_obstacle_distance_m, (int, float))
            or not _is_finite_number(min_obstacle_distance_m)
            or min_obstacle_distance_m < 0.0
        ):
            raise ValueError("min_obstacle_distance_m must be a finite non-negative number")
        self.min_localization_confidence = float(min_localization_confidence)
        self.min_obstacle_distance_m = float(min_obstacle_distance_m)

    def allow_motion(self, state: NavigationState) -> bool:
        """Return False for malformed, non-finite, or unsafe navigation state."""
        if not isinstance(state, NavigationState):
            return False
        if not isinstance(state.emergency_stop, bool):
            return False
        if not isinstance(state.human_in_exclusion_zone, bool):
            return False
        if state.emergency_stop or state.human_in_exclusion_zone:
            return False

        confidence = state.localization_confidence
        distance = state.obstacle_distance_m
        if (
            isinstance(confidence, bool)
            or not isinstance(confidence, (int, float))
            or not _is_finite_number(confidence)
            or not 0.0 <= confidence <= 1.0
        ):
            return False
        if (
            isinstance(distance, bool)
            or not isinstance(distance, (int, float))
            or not _is_finite_number(distance)
            or distance < 0.0
        ):
            return False

        return (
            confidence >= self.min_localization_confidence
            and distance >= self.min_obstacle_distance_m
        )
