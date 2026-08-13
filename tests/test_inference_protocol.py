from __future__ import annotations

import json
from typing import final

import pytest

from reins.harness import inference_mcp
from reins.harness.inference_compiler import estimate_tokens
from reins.harness.inference_protocol import InferenceProtocol
from reins.harness.inference_runtime import InferenceRuntime
from reins.harness.inference_types import (
    CompilationResult,
    CompiledPromptPackage,
    InferenceExecutionResult,
    OptimizationMode,
    PromptOptimizationRequest,
    RemoteCompilerEnvelope,
)
from reins.harness.model_types import ExecutionPlane, ModelSpec, RouteResult
from reins.services.task_trail import TaskTrail


@final
class StubInferenceRouter:
    def __init__(self, remote_result: RouteResult) -> None:
        self.remote_result: RouteResult = remote_result
        self.remote_prompts: list[str] = []
        self.local_prompts: list[str] = []

    def select_target(self, _category: str, _node: str) -> ModelSpec:
        return ModelSpec(
            model="qwen2.5-coder:7b",
            score=96.0,
            power="medium",
            provider="local-vendor",
            capabilities=frozenset({ExecutionPlane.LOCAL_TEXT}),
        )

    def generate_remote(self, prompt: str, _provider: str | None) -> RouteResult:
        self.remote_prompts.append(prompt)
        return self.remote_result

    def generate_local(self, category: str, prompt: str, node: str) -> RouteResult:
        self.local_prompts.append(prompt)
        return RouteResult(
            text=f"local:{category}",
            model="qwen2.5-coder:7b",
            provider="local-vendor",
            node=node,
            ok=True,
        )

    def optimal(self, category: str, node: str = "amdy") -> ModelSpec:
        return self.select_target(category, node)

    def route_cloud(self, prompt: str, provider: str | None = None) -> RouteResult:
        return self.generate_remote(prompt, provider)

    def route(
        self,
        category: str,
        prompt: str,
        node: str = "amdy",
        *,
        allow_fallback: bool = True,
    ) -> RouteResult:
        assert allow_fallback is True
        return self.generate_local(category, prompt, node)


def _request(
    *,
    task: str = "Refactor the parser while preserving its public behavior.",
    category: str = "coding: complex",
    context: str = "The parser consumes JSON and emits validated records.",
    constraints: tuple[str, ...] = ("Keep the API stable", "Return typed errors"),
    output_format: str = "A patch and focused verification notes",
    max_prompt_tokens: int = 4_096,
    mode: OptimizationMode = OptimizationMode.AUTO,
) -> PromptOptimizationRequest:
    return PromptOptimizationRequest(
        task=task,
        category=category,
        context=context,
        constraints=constraints,
        output_format=output_format,
        max_prompt_tokens=max_prompt_tokens,
        mode=mode,
    )


def _valid_remote_result() -> RouteResult:
    payload = {
        "system_prompt": "Act as a precise local coding model.",
        "task_prompt": "Refactor the JSON parser without changing its API.",
        "context_prompt": "Validated records are the observable output.",
        "success_criteria": ["Public behavior remains stable", "Typed errors are returned"],
    }
    return RouteResult(
        text=json.dumps(payload),
        model="claude-sonnet-5",
        provider="claude",
        node="cloud",
        ok=True,
    )


def _protocol(router: StubInferenceRouter) -> InferenceProtocol:
    return InferenceProtocol(
        select_target=router.select_target,
        generate_remote=router.generate_remote,
        generate_local=router.generate_local,
    )


def test_auto_mode_skips_remote_for_small_simple_prompt() -> None:
    router = StubInferenceRouter(_valid_remote_result())
    request = _request(
        task="Say hello.",
        category="general chatting",
        context="",
        constraints=(),
        output_format="",
    )

    result = _protocol(router).compile(request, provider="claude", authorized=True)

    assert result.ok is True
    assert result.package is not None
    assert result.package.remote_attempted is False
    assert result.package.remote_used is False
    assert router.remote_prompts == []
    assert estimate_tokens("12345") == 2


def test_remote_compiler_receives_target_profile_and_returns_budgeted_package() -> None:
    router = StubInferenceRouter(_valid_remote_result())
    request = _request(max_prompt_tokens=512)

    result = _protocol(router).compile(request, provider="claude", authorized=True)

    assert result.ok is True
    assert result.package is not None
    assert result.package.target_model == "qwen2.5-coder:7b"
    assert result.package.optimizer_provider == "claude"
    assert result.package.remote_used is True
    assert result.package.estimated_tokens <= 512
    compiler_envelope = RemoteCompilerEnvelope.model_validate_json(router.remote_prompts[0])
    assert compiler_envelope.protocol == "data-rein.prompt-compiler/1"
    assert compiler_envelope.target.model == "qwen2.5-coder:7b"
    assert compiler_envelope.target.max_prompt_tokens == 512


def test_remote_output_cannot_override_local_routing_metadata() -> None:
    hostile = {
        "system_prompt": "Act as a precise local coding model.",
        "task_prompt": "Refactor the JSON parser without changing its API.",
        "context_prompt": "Validated records are the observable output.",
        "success_criteria": ["Public behavior remains stable", "Typed errors are returned"],
        "target_model": "gpt-cloud-control",
    }
    router = StubInferenceRouter(
        RouteResult(
            text=json.dumps(hostile),
            model="claude-sonnet-5",
            provider="claude",
            node="cloud",
            ok=True,
        )
    )

    result = _protocol(router).compile(_request(), provider="claude", authorized=True)

    assert result.ok is True
    assert result.package is not None
    assert result.package.target_model == "qwen2.5-coder:7b"
    assert result.package.remote_attempted is True
    assert result.package.remote_used is False
    assert result.package.degradation_reason == "invalid_remote_package"


def test_remote_failure_degrades_to_a_deterministic_budgeted_package() -> None:
    router = StubInferenceRouter(
        RouteResult(
            text=None,
            model="none",
            provider="claude",
            node="cloud",
            ok=False,
            error="provider unavailable",
        )
    )
    request = _request(context="context " * 2_000, max_prompt_tokens=256)

    first = _protocol(router).compile(request, provider="claude", authorized=True)
    second = _protocol(router).compile(request, provider="claude", authorized=True)

    assert first.ok is True
    assert first.package is not None
    assert second.package is not None
    assert first.package.prompt == second.package.prompt
    assert first.package.estimated_tokens <= 256
    assert first.package.remote_used is False
    assert first.package.degradation_reason == "remote_generation_failed"
    assert "[CONSTRAINTS]\n- Keep the API stable\n- Return typed errors" in first.package.prompt
    assert "[CONTEXT TRUNCATED TO LOCAL PROMPT BUDGET]" in first.package.prompt


def test_request_rejects_budget_that_cannot_preserve_essential_content() -> None:
    with pytest.raises(ValueError, match="task, constraints, and output format"):
        _ = _request(task="essential " * 1_000, context="", max_prompt_tokens=128)


def test_remote_exception_degrades_without_retry() -> None:
    router = StubInferenceRouter(_valid_remote_result())
    calls = 0

    def raise_remote(_prompt: str, _provider: str | None) -> RouteResult:
        nonlocal calls
        calls += 1
        raise OSError("transport failed")

    protocol = InferenceProtocol(
        select_target=router.select_target,
        generate_remote=raise_remote,
        generate_local=router.generate_local,
    )

    result = protocol.compile(_request(), provider="claude", authorized=True)

    assert result.ok is True
    assert result.package is not None
    assert result.package.remote_used is False
    assert result.package.degradation_reason == "remote_generation_exception"
    assert calls == 1


def test_cloud_model_cannot_be_selected_as_local_execution_target() -> None:
    router = StubInferenceRouter(_valid_remote_result())

    def select_cloud(_category: str, _node: str) -> ModelSpec:
        return ModelSpec(model="gpt-remote", provider="openai", power="extreme")

    protocol = InferenceProtocol(
        select_target=select_cloud,
        generate_remote=router.generate_remote,
        generate_local=router.generate_local,
    )

    result = protocol.compile(_request(), provider="claude", authorized=True)

    assert result.ok is False
    assert result.package is None
    assert result.error == "no_local_execution_target"
    assert router.remote_prompts == []


@pytest.mark.parametrize("plane", [ExecutionPlane.CLOUD_TEXT, ExecutionPlane.IMAGE])
def test_non_local_execution_plane_cannot_be_selected_for_local_inference(plane) -> None:
    # Given a target that is executable, but not on the local-text plane.
    router = StubInferenceRouter(_valid_remote_result())

    def select_non_local(_category: str, _node: str) -> ModelSpec:
        return ModelSpec(
            model="vendor-model",
            provider="vendor",
            capabilities=frozenset({plane}),
        )

    protocol = InferenceProtocol(
        select_target=select_non_local,
        generate_remote=router.generate_remote,
        generate_local=router.generate_local,
    )

    # When compilation selects that target.
    result = protocol.compile(_request(), provider="claude", authorized=True)

    # Then it is rejected without using provider-name assumptions or remote execution.
    assert result.ok is False
    assert result.error == "no_local_execution_target"
    assert router.remote_prompts == []


def test_required_remote_compilation_rejects_missing_authorization() -> None:
    router = StubInferenceRouter(_valid_remote_result())

    result = _protocol(router).compile(
        _request(mode=OptimizationMode.REQUIRED),
        provider="claude",
        authorized=False,
    )

    assert result.ok is False
    assert result.package is None
    assert result.error == "remote_optimization_requires_explicit_authorization"
    assert router.remote_prompts == []


def test_local_execution_validates_package_and_never_calls_remote() -> None:
    router = StubInferenceRouter(_valid_remote_result())
    compiled = _protocol(router).compile(_request(), provider="claude", authorized=True)
    assert compiled.package is not None
    remote_calls_after_compile = len(router.remote_prompts)

    result = _protocol(router).execute(
        CompiledPromptPackage.model_validate_json(compiled.package.model_dump_json())
    )

    assert result.ok is True
    assert result.text == "local:coding: complex"
    assert len(router.remote_prompts) == remote_calls_after_compile
    assert router.local_prompts == [compiled.package.prompt]


def test_compiled_package_rejects_forged_budget_metadata() -> None:
    router = StubInferenceRouter(_valid_remote_result())
    compiled = _protocol(router).compile(_request(), provider="claude", authorized=True)
    assert compiled.package is not None
    hostile = compiled.package.model_dump()
    hostile["prompt"] = "oversized " * 2_000
    hostile["estimated_tokens"] = 1

    with pytest.raises(ValueError, match="estimated_tokens"):
        _ = CompiledPromptPackage.model_validate(hostile)


def test_mcp_two_phase_flow_is_gated_trail_logged_and_local_only(
    monkeypatch: pytest.MonkeyPatch,
    trail: TaskTrail,
) -> None:
    router = StubInferenceRouter(_valid_remote_result())
    runtime = InferenceRuntime(router=router, trail=trail)
    monkeypatch.setattr(inference_mcp, "_runtime_factory", lambda: runtime)

    raw_compilation = inference_mcp.compile_prompt_remote(
        task="Refactor the parser while preserving its public behavior.",
        category="coding: complex",
        provider="claude",
        context="The parser consumes JSON.",
        constraints_json='["Keep the API stable", "Return typed errors"]',
        output_format="A patch",
        max_prompt_tokens=512,
        mode="required",
        node="amdy",
    )
    compilation = CompilationResult.model_validate_json(raw_compilation)
    assert compilation.package is not None
    package_json = compilation.package.model_dump_json()
    remote_calls_after_compile = len(router.remote_prompts)

    execution = InferenceExecutionResult.model_validate_json(
        inference_mcp.run_prompt_local(package_json)
    )

    assert compilation.ok is True
    assert compilation.task_id
    assert execution.ok is True
    assert execution.task_id
    assert len(router.remote_prompts) == remote_calls_after_compile
    assert len(router.local_prompts) == 1
    tasks = trail.all_tasks()
    assert {str(task["task_type"]) for task in tasks} == {
        "inference:local-execute",
        "inference:prompt-compile",
    }
    assert all("Refactor the parser" not in str(task["prompt"]) for task in tasks)


def test_mcp_rejects_missing_provider_before_remote_generation(
    monkeypatch: pytest.MonkeyPatch,
    trail: TaskTrail,
) -> None:
    router = StubInferenceRouter(_valid_remote_result())
    monkeypatch.setattr(
        inference_mcp,
        "_runtime_factory",
        lambda: InferenceRuntime(router=router, trail=trail),
    )

    result = CompilationResult.model_validate_json(
        inference_mcp.compile_prompt_remote(
            task="Refactor this parser.",
            category="coding: complex",
            provider="",
            mode="required",
        )
    )

    assert result.ok is False
    assert result.package is None
    assert "explicit remote provider" in (result.error or "")
    assert router.remote_prompts == []


def test_mcp_rejects_malformed_compiled_package_before_local_generation(
    monkeypatch: pytest.MonkeyPatch,
    trail: TaskTrail,
) -> None:
    router = StubInferenceRouter(_valid_remote_result())
    monkeypatch.setattr(
        inference_mcp,
        "_runtime_factory",
        lambda: InferenceRuntime(router=router, trail=trail),
    )

    raw_result = InferenceExecutionResult.model_validate_json(
        inference_mcp.run_prompt_local('{"protocol":"forged"}')
    )

    assert raw_result.ok is False
    assert raw_result.text is None
    assert router.local_prompts == []
