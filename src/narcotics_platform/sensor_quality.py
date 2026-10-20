from dataclasses import dataclass, field
import math
from numbers import Real
from typing import Mapping


def _unit_interval(value: object, field_name: str) -> float:
    """Validate a finite, non-boolean real value in the inclusive [0, 1] range."""
    if (
        isinstance(value, bool)
        or not isinstance(value, Real)
        or not math.isfinite(value)
        or not 0.0 <= value <= 1.0
    ):
        raise ValueError(f"{field_name} must be a finite number between 0 and 1")
    return float(value)


@dataclass(frozen=True)
class SensorStatus:
    name: str
    available: bool = True
    quality: float = 1.0
    synchronized: bool = True
    calibration_id: str | None = None
    notes: str = ""

    def __post_init__(self) -> None:
        _unit_interval(self.quality, "quality")


@dataclass(frozen=True)
class QualityReport:
    usable: bool
    aggregate_quality: float
    degraded_modalities: tuple[str, ...] = field(default_factory=tuple)
    missing_modalities: tuple[str, ...] = field(default_factory=tuple)
    reasons: tuple[str, ...] = field(default_factory=tuple)


def assess_sensor_quality(
    statuses: Mapping[str, SensorStatus], minimum_quality: float = 0.50
) -> QualityReport:
    _unit_interval(minimum_quality, "minimum_quality")
    if not statuses:
        return QualityReport(False, 0.0, reasons=("no sensor status supplied",))
    missing = tuple(name for name, status in statuses.items() if not status.available)
    degraded = tuple(
        name
        for name, status in statuses.items()
        if status.available and status.quality < minimum_quality
    )
    usable_scores = [status.quality for status in statuses.values() if status.available]
    aggregate = sum(usable_scores) / len(usable_scores) if usable_scores else 0.0
    reasons: list[str] = []
    if missing:
        reasons.append("one or more modalities are unavailable")
    if degraded:
        reasons.append("one or more modalities are degraded")
    if any(not status.synchronized for status in statuses.values() if status.available):
        reasons.append("timestamp synchronization is incomplete")
    usable = (
        bool(usable_scores)
        and aggregate >= minimum_quality
        and not any(
            not status.synchronized
            for status in statuses.values()
            if status.available
        )
    )
    return QualityReport(usable, aggregate, degraded, missing, tuple(reasons))
