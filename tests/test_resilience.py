from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import anyio
import pytest
from typing_extensions import override

from reins.harness.resilience import (
    BreakerRegistry,
    CircuitBreaker,
    with_retry,
)
from reins.harness.resilience_types import (
    BreakerState,
    CircuitConfig,
    CircuitOpenError,
    ResilienceConfigurationError,
    RetryPolicy,
)


@dataclass(frozen=True, slots=True)
class BackendUnavailableError(RuntimeError):
    message: str

    @override
    def __str__(self) -> str:
        return self.message


@pytest.mark.parametrize(
    ("factory", "expected_message"),
    [
        (lambda: CircuitConfig(failure_threshold=0), "failure_threshold must be positive"),
        (lambda: CircuitConfig(window_seconds=0.0), "window_seconds must be positive"),
        (lambda: CircuitConfig(cooldown_seconds=0.0), "cooldown_seconds must be positive"),
        (lambda: RetryPolicy(max_attempts=0), "max_attempts must be positive"),
        (lambda: RetryPolicy(base_delay=-0.1), "retry delays are invalid"),
        (lambda: RetryPolicy(jitter_ratio=1.1), "jitter_ratio must be between zero and one"),
    ],
)
def test_invalid_resilience_configuration_raises_typed_error(
    factory: Callable[[], CircuitConfig | RetryPolicy],
    expected_message: str,
) -> None:
    # Given hostile values cross the public policy-construction boundary.
    # When construction rejects the invalid value.
    with pytest.raises(ResilienceConfigurationError, match=expected_message) as caught:
        _ = factory()

    # Then callers receive one typed contract without losing the diagnostic.
    assert str(caught.value) == expected_message


class FakeClock:
    now: float

    def __init__(self) -> None:
        self.now = 0.0

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


def test_breaker_opens_and_recovers_through_half_open() -> None:
    # Given a backend that reaches its bounded failure threshold.
    clock = FakeClock()
    transitions: list[tuple[BreakerState, BreakerState]] = []
    breaker = CircuitBreaker(
        "provider:model",
        failure_threshold=2,
        window_seconds=60.0,
        cooldown_seconds=10.0,
        clock=clock,
        on_transition=lambda _name, old, new: transitions.append((old, new)),
    )

    def fail() -> str:
        raise BackendUnavailableError("backend unavailable")

    # When repeated failures open the circuit.
    for _attempt in range(2):
        with pytest.raises(BackendUnavailableError, match="backend unavailable"):
            _ = breaker.call(fail)

    # Then calls fast-fail until one cooldown probe succeeds.
    assert breaker.state is BreakerState.OPEN
    with pytest.raises(CircuitOpenError):
        _ = breaker.call(lambda: "must not execute")
    clock.advance(10.0)
    assert breaker.call(lambda: "recovered") == "recovered"
    assert breaker.state is BreakerState.CLOSED
    assert transitions == [
        (BreakerState.CLOSED, BreakerState.OPEN),
        (BreakerState.OPEN, BreakerState.HALF_OPEN),
        (BreakerState.HALF_OPEN, BreakerState.CLOSED),
    ]


def test_breaker_failure_window_is_bounded() -> None:
    # Given failures separated by more than the configured observation window.
    clock = FakeClock()
    breaker = CircuitBreaker(
        "bounded",
        failure_threshold=3,
        window_seconds=5.0,
        cooldown_seconds=10.0,
        clock=clock,
    )

    def fail() -> None:
        raise BackendUnavailableError("transient")

    # When each old failure expires before the next one occurs.
    for _attempt in range(10):
        with pytest.raises(BackendUnavailableError, match="transient"):
            _ = breaker.call(fail)
        clock.advance(6.0)

    # Then history remains incremental and the circuit never opens.
    assert breaker.failure_count == 0
    assert breaker.state is BreakerState.CLOSED


def test_retry_uses_exponential_backoff_only_for_idempotent_calls() -> None:
    # Given an idempotent operation with two transient failures.
    clock = FakeClock()
    waits: list[float] = []
    attempts: list[int] = []
    breaker = CircuitBreaker(
        "idempotent",
        failure_threshold=5,
        window_seconds=60.0,
        cooldown_seconds=10.0,
        clock=clock,
    )

    def operation() -> str:
        attempts.append(len(attempts) + 1)
        if len(attempts) < 3:
            raise BackendUnavailableError("retryable")
        return "ok"

    # When disciplined retry is explicitly enabled.
    result = with_retry(
        operation,
        breaker=breaker,
        idempotent=True,
        policy=RetryPolicy(max_attempts=3, base_delay=0.1, max_delay=1.0),
        wait=waits.append,
        jitter=lambda _low, _high: 0.0,
    )

    # Then the backoff is deterministic and bounded.
    assert result == "ok"
    assert attempts == [1, 2, 3]
    assert waits == [0.1, 0.2]


def test_retry_never_repeats_non_idempotent_generation() -> None:
    # Given a billable generation operation that fails.
    attempts: list[bool] = []
    breaker = CircuitBreaker("generation")

    def generation() -> str:
        attempts.append(True)
        raise BackendUnavailableError("provider error")

    # When it passes through the retry boundary as non-idempotent.
    with pytest.raises(BackendUnavailableError, match="provider error"):
        _ = with_retry(generation, breaker=breaker, idempotent=False)

    # Then it executes exactly once.
    assert attempts == [True]


def test_breaker_observes_failed_result_without_rewriting_it() -> None:
    # Given an external API reports failure in its return object instead of raising.
    breaker = CircuitBreaker("return-code", failure_threshold=2)
    result = {"returncode": 1}

    # When the breaker evaluates the operation-specific success predicate.
    observed = breaker.call(lambda: result, is_success=lambda value: value["returncode"] == 0)

    # Then the original result is preserved and the failure enters bounded history.
    assert observed is result
    assert breaker.failure_count == 1


def test_async_breaker_observes_awaited_failure() -> None:
    # Given an awaited transport fails after admission.
    breaker = CircuitBreaker("async-transport", failure_threshold=2)

    async def fail() -> str:
        raise BackendUnavailableError("async backend unavailable")

    # When the asynchronous breaker owns the awaited operation.
    with pytest.raises(BackendUnavailableError, match="async backend unavailable"):
        _ = anyio.run(breaker.call_async, fail)

    # Then the failure is retained for later open-circuit decisions.
    assert breaker.failure_count == 1


def test_model_router_fast_fails_an_open_provider_circuit(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given one configured model whose provider fails repeatedly.
    from reins.harness.models import ModelRouter

    calls: list[str] = []
    registry = BreakerRegistry(
        CircuitConfig(
            failure_threshold=2,
            window_seconds=60.0,
            cooldown_seconds=30.0,
        )
    )
    router = ModelRouter(breaker_registry=registry)

    def admit(_node: str, _model: str) -> bool:
        return True

    monkeypatch.setattr(router.model_inventory, "admit", admit)
    router.table = {"x": {"amdy": [{"model": "broken-model"}]}}
    router.remote_fallback = []
    monkeypatch.setattr("reins.harness.local.list_models", lambda: list[str]())

    def fail(_self: ModelRouter, model: str, _prompt: str, _node: str) -> str:
        calls.append(model)
        raise BackendUnavailableError("provider unavailable")

    monkeypatch.setattr(ModelRouter, "_ollama", fail)

    # When two failures open the model-specific circuit and a third request arrives.
    first = router.route("x", "one", allow_fallback=False)
    second = router.route("x", "two", allow_fallback=False)
    third = router.route("x", "three", allow_fallback=False)

    # Then the third request degrades without executing another generation call.
    assert first.ok is False
    assert second.ok is False
    assert third.ok is False
    assert "circuit" in (third.error or "")
    assert calls == ["broken-model", "broken-model"]
