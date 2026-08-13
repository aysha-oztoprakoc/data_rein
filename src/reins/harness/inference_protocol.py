from __future__ import annotations

import hashlib
import logging
from collections.abc import Callable
from typing import final

from pydantic import ValidationError

from reins.harness.inference_compiler import (
    build_package,
    compiler_envelope,
    estimate_tokens,
    fallback_package,
    render_remote,
)
from reins.harness.inference_types import (
    CompilationResult,
    CompiledPromptPackage,
    InferenceExecutionResult,
    OptimizationMode,
    PromptOptimizationRequest,
    RemotePromptPackage,
)
from reins.harness.model_types import ExecutionPlane, ModelSpec, RouteResult

logger = logging.getLogger(__name__)

SelectTarget = Callable[[str, str], ModelSpec]
GenerateRemote = Callable[[str, str | None], RouteResult]
GenerateLocal = Callable[[str, str, str], RouteResult]

_COMPLEX_CATEGORIES = frozenset(
    {
        "coding: complex",
        "data processing",
        "deep search",
        "prompt optimization",
        "self-optimization",
    }
)


def is_remote_optimization_eligible(request: PromptOptimizationRequest) -> bool:
    if request.mode is OptimizationMode.REQUIRED:
        return True
    if request.mode is OptimizationMode.BYPASS:
        return False
    return (
        request.category.lower() in _COMPLEX_CATEGORIES
        or estimate_tokens(request.task + request.context) >= 512
        or len(request.constraints) >= 2
    )


@final
class InferenceProtocol:
    def __init__(
        self,
        *,
        select_target: SelectTarget,
        generate_remote: GenerateRemote,
        generate_local: GenerateLocal,
    ) -> None:
        self._select_target: SelectTarget = select_target
        self._generate_remote: GenerateRemote = generate_remote
        self._generate_local: GenerateLocal = generate_local

    def compile(
        self,
        request: PromptOptimizationRequest,
        *,
        provider: str | None,
        authorized: bool,
    ) -> CompilationResult:
        target = self._select_target(request.category, request.node)
        if target.model == "none" or ExecutionPlane.LOCAL_TEXT not in target.capabilities:
            return CompilationResult(ok=False, error="no_local_execution_target")
        eligible = is_remote_optimization_eligible(request)
        if eligible and not authorized:
            return CompilationResult(
                ok=False,
                error="remote_optimization_requires_explicit_authorization",
            )
        if not eligible:
            return CompilationResult(ok=True, package=fallback_package(request, target))

        try:
            remote = self._generate_remote(compiler_envelope(request, target), provider)
        except Exception:
            logger.exception("remote prompt generation degraded")
            return CompilationResult(
                ok=True,
                package=fallback_package(
                    request,
                    target,
                    provider=provider,
                    attempted=True,
                    reason="remote_generation_exception",
                ),
            )
        if not remote.ok or remote.text is None:
            return CompilationResult(
                ok=True,
                package=fallback_package(
                    request,
                    target,
                    provider=remote.provider or provider,
                    optimizer_model=remote.model,
                    attempted=True,
                    reason="remote_generation_failed",
                ),
            )
        try:
            optimized = RemotePromptPackage.model_validate_json(remote.text)
        except ValidationError:
            return CompilationResult(
                ok=True,
                package=fallback_package(
                    request,
                    target,
                    provider=remote.provider,
                    optimizer_model=remote.model,
                    attempted=True,
                    reason="invalid_remote_package",
                ),
            )

        prompt = render_remote(optimized, request)
        if estimate_tokens(prompt) > request.max_prompt_tokens:
            return CompilationResult(
                ok=True,
                package=fallback_package(
                    request,
                    target,
                    provider=remote.provider,
                    optimizer_model=remote.model,
                    attempted=True,
                    reason="remote_package_exceeds_budget",
                ),
            )
        return CompilationResult(
            ok=True,
            package=build_package(
                request,
                target,
                prompt,
                optimized.success_criteria,
                provider=remote.provider,
                optimizer_model=remote.model,
                attempted=True,
                remote_used=True,
            ),
        )

    def execute(self, package: CompiledPromptPackage) -> InferenceExecutionResult:
        result = self._generate_local(package.category, package.prompt, package.node)
        return InferenceExecutionResult(
            ok=result.ok,
            text=result.text,
            model=result.model,
            provider=result.provider,
            node=result.node,
            error=result.error,
            package_sha256=hashlib.sha256(package.model_dump_json().encode()).hexdigest(),
        )
