from __future__ import annotations

import random
import threading
import time
from collections import deque
from collections.abc import Awaitable, Callable
from typing import TypeVar

from reins.harness.resilience_types import (
    BreakerState,
    CircuitConfig,
    CircuitOpenError,
    RetryPolicy,
)

__all__ = [
    "BreakerRegistry",
    "BreakerState",
    "CircuitBreaker",
    "CircuitConfig",
    "CircuitOpenError",
    "RetryPolicy",
    "with_retry",
]

T = TypeVar("T")
TransitionHandler = Callable[[str, "BreakerState", "BreakerState"], None]


class CircuitBreaker:
    name: str
    _config: CircuitConfig
    _clock: Callable[[], float]
    _on_transition: TransitionHandler | None
    _failures: deque[float]
    _state: BreakerState
    _opened_at: float | None
    _half_open_in_flight: bool
    _lock: threading.RLock

    def __init__(
        self,
        name: str,
        *,
        failure_threshold: int = 3,
        window_seconds: float = 60.0,
        cooldown_seconds: float = 30.0,
        clock: Callable[[], float] = time.monotonic,
        on_transition: TransitionHandler | None = None,
    ) -> None:
        config = CircuitConfig(
            failure_threshold=failure_threshold,
            window_seconds=window_seconds,
            cooldown_seconds=cooldown_seconds,
        )
        self.name = name
        self._config = config
        self._clock = clock
        self._on_transition = on_transition
        self._failures = deque(maxlen=config.failure_threshold)
        self._state = BreakerState.CLOSED
        self._opened_at = None
        self._half_open_in_flight = False
        self._lock = threading.RLock()

    @property
    def state(self) -> BreakerState:
        with self._lock:
            return self._state

    @property
    def failure_count(self) -> int:
        with self._lock:
            self._prune(self._clock())
            return len(self._failures)

    def call(
        self,
        operation: Callable[[], T],
        *,
        is_success: Callable[[T], bool] | None = None,
    ) -> T:
        self._admit()
        try:
            result = operation()
        except Exception:
            self._record_failure()
            raise
        if is_success is not None and not is_success(result):
            self._record_failure()
        else:
            self._record_success()
        return result

    async def call_async(
        self,
        operation: Callable[[], Awaitable[T]],
        *,
        is_success: Callable[[T], bool] | None = None,
    ) -> T:
        self._admit()
        try:
            result = await operation()
        except Exception:
            self._record_failure()
            raise
        if is_success is not None and not is_success(result):
            self._record_failure()
        else:
            self._record_success()
        return result

    def _admit(self) -> None:
        with self._lock:
            now = self._clock()
            self._prune(now)
            if self._state is BreakerState.OPEN:
                opened_at = self._opened_at if self._opened_at is not None else now
                elapsed = now - opened_at
                if elapsed < self._config.cooldown_seconds:
                    raise CircuitOpenError(
                        self.name,
                        self._config.cooldown_seconds - elapsed,
                    )
                self._transition(BreakerState.HALF_OPEN)
            if self._state is BreakerState.HALF_OPEN:
                if self._half_open_in_flight:
                    raise CircuitOpenError(self.name, self._config.cooldown_seconds)
                self._half_open_in_flight = True

    def _record_failure(self) -> None:
        with self._lock:
            now = self._clock()
            if self._state is BreakerState.HALF_OPEN:
                self._half_open_in_flight = False
                self._opened_at = now
                self._transition(BreakerState.OPEN)
                return
            self._prune(now)
            self._failures.append(now)
            if len(self._failures) >= self._config.failure_threshold:
                self._opened_at = now
                self._transition(BreakerState.OPEN)

    def _record_success(self) -> None:
        with self._lock:
            self._failures.clear()
            self._opened_at = None
            self._half_open_in_flight = False
            self._transition(BreakerState.CLOSED)

    def _prune(self, now: float) -> None:
        cutoff = now - self._config.window_seconds
        while self._failures and self._failures[0] <= cutoff:
            _ = self._failures.popleft()

    def _transition(self, new_state: BreakerState) -> None:
        old_state = self._state
        if old_state is new_state:
            return
        self._state = new_state
        if self._on_transition is not None:
            self._on_transition(self.name, old_state, new_state)


class BreakerRegistry:
    _config: CircuitConfig
    _clock: Callable[[], float]
    _on_transition: TransitionHandler | None
    _breakers: dict[str, CircuitBreaker]
    _lock: threading.Lock

    def __init__(
        self,
        config: CircuitConfig | None = None,
        *,
        clock: Callable[[], float] = time.monotonic,
        on_transition: TransitionHandler | None = None,
    ) -> None:
        self._config = config or CircuitConfig()
        self._clock = clock
        self._on_transition = on_transition
        self._breakers = {}
        self._lock = threading.Lock()

    def get(self, name: str) -> CircuitBreaker:
        with self._lock:
            breaker = self._breakers.get(name)
            if breaker is None:
                breaker = CircuitBreaker(
                    name,
                    failure_threshold=self._config.failure_threshold,
                    window_seconds=self._config.window_seconds,
                    cooldown_seconds=self._config.cooldown_seconds,
                    clock=self._clock,
                    on_transition=self._on_transition,
                )
                self._breakers[name] = breaker
            return breaker


def with_retry(
    operation: Callable[[], T],
    *,
    breaker: CircuitBreaker,
    idempotent: bool,
    policy: RetryPolicy | None = None,
    wait: Callable[[float], object] | None = None,
    jitter: Callable[[float, float], float] | None = None,
) -> T:
    if not idempotent:
        return breaker.call(operation)

    active_policy = policy or RetryPolicy()
    active_wait = wait or threading.Event().wait
    active_jitter: Callable[[float, float], float] = jitter or random.uniform
    next_delay = active_policy.base_delay
    for attempt in range(active_policy.max_attempts):
        try:
            return breaker.call(operation)
        except CircuitOpenError:
            raise
        except Exception:
            if attempt + 1 >= active_policy.max_attempts:
                raise
            base = min(next_delay, active_policy.max_delay)
            extra: float = active_jitter(0.0, base * active_policy.jitter_ratio)
            _ = active_wait(base + extra)
            next_delay = min(base * 2.0, active_policy.max_delay)
    raise RuntimeError("retry attempts exhausted without a result")
