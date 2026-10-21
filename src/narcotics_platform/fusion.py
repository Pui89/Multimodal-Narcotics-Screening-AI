from dataclasses import dataclass
import math
from typing import Iterable


@dataclass(frozen=True)
class ModalityEvidence:
    modality: str
    label: str
    confidence: float
    quality: float = 1.0
    source_id: str | None = None

    def __post_init__(self) -> None:
        for name, value in (("confidence", self.confidence), ("quality", self.quality)):
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or not 0.0 <= value <= 1.0
            ):
                raise ValueError(f"{name} must be a finite number between 0 and 1")
        if not isinstance(self.modality, str) or not self.modality.strip():
            raise ValueError("modality must be a non-empty string")
        if not isinstance(self.label, str) or not self.label.strip():
            raise ValueError("label must be a non-empty string")


@dataclass(frozen=True)
class FusionResult:
    label: str
    confidence: float
    agreement: float
    contributing_modalities: tuple[str, ...]
    contradiction: bool
    evidence_count: int


class MultimodalFusion:
    """Deterministic baseline fusion; a learned fusion model can replace it without changing the API."""

    def fuse(self, evidence: Iterable[ModalityEvidence]) -> FusionResult:
        items = tuple(evidence)
        if not items:
            return FusionResult("unknown_substance", 0.0, 0.0, (), False, 0)
        scores: dict[str, float] = {}
        modality_labels: dict[str, set[str]] = {}
        for item in items:
            weight = item.quality * item.confidence
            scores[item.label] = scores.get(item.label, 0.0) + weight
            modality_labels.setdefault(item.modality, set()).add(item.label)
        total = sum(scores.values())
        label, best = max(scores.items(), key=lambda pair: pair[1])
        confidence = best / total if total else 0.0
        winning = {item.modality for item in items if item.label == label}
        agreement = len(winning) / max(1, len(modality_labels))
        contradiction = len({item.label for item in items if item.confidence >= 0.5}) > 1
        return FusionResult(label, confidence, agreement, tuple(sorted(winning)), contradiction, len(items))
