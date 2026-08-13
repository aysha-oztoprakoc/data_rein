from __future__ import annotations

import hashlib

from reins.harness.inference_types import (
    CompiledPromptPackage,
    CompilerTarget,
    PromptOptimizationRequest,
    RemoteCompilerEnvelope,
    RemotePromptPackage,
)
from reins.harness.model_types import ModelSpec


def estimate_tokens(text: str) -> int:
    return max(1, (len(text) + 3) // 4)


def compiler_envelope(request: PromptOptimizationRequest, target: ModelSpec) -> str:
    envelope = RemoteCompilerEnvelope(
        protocol="data-rein.prompt-compiler/1",
        operation="compress_context_and_adapt_format",
        request=request,
        target=CompilerTarget(
            model=target.model,
            power=target.power,
            node=request.node,
            max_prompt_tokens=request.max_prompt_tokens,
        ),
        output_schema={
            "system_prompt": "non-empty string",
            "task_prompt": "non-empty string",
            "context_prompt": "string",
            "success_criteria": "one or more strings",
        },
        rules=(
            "Return exactly one JSON object matching output_schema.",
            "Preserve task intent and explicit constraints.",
            "Compress supplied context; do not invent facts.",
            "Do not emit routing, provider, authorization, or tool-call fields.",
            "Keep the rendered package within target.max_prompt_tokens.",
        ),
    )
    return envelope.model_dump_json()


def render_remote(optimized: RemotePromptPackage, request: PromptOptimizationRequest) -> str:
    sections = [
        f"[SYSTEM]\n{optimized.system_prompt}",
        f"[TASK]\n{optimized.task_prompt}",
        "[SUCCESS CRITERIA]\n" + "\n".join(f"- {item}" for item in optimized.success_criteria),
    ]
    if request.constraints:
        sections.append(
            "[NON-NEGOTIABLE CONSTRAINTS]\n"
            + "\n".join(f"- {item}" for item in request.constraints)
        )
    if request.output_format:
        sections.append(f"[OUTPUT FORMAT]\n{request.output_format}")
    if optimized.context_prompt:
        sections.append(f"[CONTEXT]\n{optimized.context_prompt}")
    return "\n\n".join(sections)


def fallback_package(
    request: PromptOptimizationRequest,
    target: ModelSpec,
    *,
    provider: str | None = None,
    optimizer_model: str | None = None,
    attempted: bool = False,
    reason: str | None = None,
) -> CompiledPromptPackage:
    criteria = request.constraints or ("Complete the requested task without changing its intent.",)
    sections = [f"[TASK]\n{request.task}"]
    if request.constraints:
        sections.append(
            "[CONSTRAINTS]\n" + "\n".join(f"- {item}" for item in request.constraints)
        )
    if request.output_format:
        sections.append(f"[OUTPUT FORMAT]\n{request.output_format}")
    prompt = "\n\n".join(sections)
    if request.context:
        prompt = append_context(prompt, request.context, request.max_prompt_tokens)
    return build_package(
        request,
        target,
        prompt,
        criteria,
        provider=provider,
        optimizer_model=optimizer_model,
        attempted=attempted,
        remote_used=False,
        reason=reason,
    )


def append_context(prompt: str, context: str, max_tokens: int) -> str:
    char_budget = max_tokens * 4
    prefix = prompt + "\n\n[CONTEXT]\n"
    if len(prefix) + len(context) <= char_budget:
        return prefix + context
    marker = "\n[CONTEXT TRUNCATED TO LOCAL PROMPT BUDGET]"
    available = char_budget - len(prefix) - len(marker)
    if available <= 0:
        return prompt
    return prefix + context[:available].rstrip() + marker


def build_package(
    request: PromptOptimizationRequest,
    target: ModelSpec,
    prompt: str,
    criteria: tuple[str, ...],
    *,
    provider: str | None,
    optimizer_model: str | None,
    attempted: bool,
    remote_used: bool,
    reason: str | None = None,
) -> CompiledPromptPackage:
    source = request.model_dump_json()
    return CompiledPromptPackage(
        source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        category=request.category,
        node=request.node,
        target_model=target.model,
        target_power=target.power,
        max_prompt_tokens=request.max_prompt_tokens,
        estimated_tokens=estimate_tokens(prompt),
        prompt=prompt,
        success_criteria=criteria,
        optimizer_provider=provider,
        optimizer_model=optimizer_model,
        remote_attempted=attempted,
        remote_used=remote_used,
        degradation_reason=reason,
    )
