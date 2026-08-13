from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from typing_extensions import override


class BreakerState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


class CircuitOpenError(ConnectionError):
    name: str
    remaining_seconds: float

    def __init__(self, name: str, remaining_seconds: float) -> None:
        self.name = name
        self.remaining_seconds = max(0.0, remaining_seconds)
        super().__init__(f"circuit {name!r} is open for {self.remaining_seconds:.2f}s more")


@dataclass(frozen=True, slots=True)
class ResilienceConfigurationError(ValueError):
    field: str
    reason: str

    @override
    def __str__(self) -> str:
        return f"{self.field} {self.reason}"


@dataclass(frozen=True, slots=True)
class CircuitConfig:
    failure_threshold: int = 3
    window_seconds: float = 60.0
    cooldown_seconds: float = 30.0

    def __post_init__(self) -> None:
        if self.failure_threshold < 1:
            raise ResilienceConfigurationError("failure_threshold", "must be positive")
        if self.window_seconds <= 0:
            raise ResilienceConfigurationError("window_seconds", "must be positive")
        if self.cooldown_seconds <= 0:
            raise ResilienceConfigurationError("cooldown_seconds", "must be positive")


@dataclass(frozen=True, slots=True)
class RetryPolicy:
    max_attempts: int = 3
    base_delay: float = 0.1
    max_delay: float = 1.0
    jitter_ratio: float = 0.1

    def __post_init__(self) -> None:
        if self.max_attempts < 1:
            raise ResilienceConfigurationError("max_attempts", "must be positive")
        if self.base_delay < 0 or self.max_delay < self.base_delay:
            raise ResilienceConfigurationError("retry delays", "are invalid")
        if not 0.0 <= self.jitter_ratio <= 1.0:
            raise ResilienceConfigurationError(
                "jitter_ratio",
                "must be between zero and one",
            )
