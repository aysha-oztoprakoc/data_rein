"""
Deterministic action-gate pipeline, per `blueprint.yaml`'s `action_gates`
section: a lesser model's proposed tool call is a proposal, never an
instruction. Every call passes capture -> allowlist -> schema -> sanitize ->
billing/idempotency-guard before the real dispatcher ever runs (GD-2, GD-3).

No model output reaches a real effect without going through `gate_call`.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Protocol, TypedDict

from reins.harness.provider_protocols import JsonValue
from reins.services.task_trail import TaskTrail

REPO_ROOT = Path(__file__).resolve().parents[3]

# context -> allowlisted tool names for that calling context
ALLOWLISTS: dict[str, set[str]] = {
    "route_local": {"local_generate", "read_file"},
    "escalate_cloud": {"cloud_generate"},
    "compile_prompt_remote": {"remote_prompt_compile"},
    "run_prompt_local": {"compiled_local_generate"},
}

# tool_name -> {arg_name: expected_type}
ActionArgs = dict[str, str | int | float | bool | None]
ActionResult = dict[str, JsonValue]


class Dispatcher(Protocol):
    def __call__(self, args: ActionArgs) -> ActionResult: ...


class GateResult(TypedDict):
    accepted: bool
    reason: str | None
    result: ActionResult | None


class ValidationResult(TypedDict):
    accepted: bool
    reason: str | None


SCHEMAS: dict[str, dict[str, type[str] | type[int] | type[float] | type[bool]]] = {
    "local_generate": {"prompt": str, "category": str, "node": str},
    "read_file": {"path": str},
    "cloud_generate": {"prompt": str, "provider": str, "task_type": str},
    "remote_prompt_compile": {
        "task": str,
        "category": str,
        "provider": str,
        "context": str,
        "constraints_json": str,
        "output_format": str,
        "max_prompt_tokens": int,
        "mode": str,
        "node": str,
    },
    "compiled_local_generate": {"package_json": str},
}

OPTIONAL_ARGS: dict[str, set[str]] = {
    "local_generate": {"category", "node"},
    "read_file": set(),
    "cloud_generate": {"provider", "task_type"},
    "remote_prompt_compile": set(),
    "compiled_local_generate": set(),
}

# tools whose calls are billable/non-idempotent and require explicit authorization
BILLABLE_TOOLS: set[str] = {"cloud_generate", "remote_prompt_compile"}


def _log_rejection(context: str, tool_name: str, reason: str) -> None:
    """GD-3: every rejection leaves a diagnostic trace, never a silent drop."""
    trail = TaskTrail()
    task_id = trail.create_task(
        "gate:reject",
        json.dumps({"context": context, "tool_name": tool_name, "reason": reason}),
        context,
    )
    trail.update_task(task_id, "failed")


def _schema_valid(tool_name: str, args: ActionArgs) -> bool:
    schema = SCHEMAS.get(tool_name)
    if schema is None:
        return False
    optional = OPTIONAL_ARGS[tool_name]
    if not set(args).issubset(schema):
        return False
    for key, expected_type in schema.items():
        if key not in args:
            if key in optional:
                continue
            return False
        if not isinstance(args[key], expected_type):
            return False
    return True


def _sanitize_ok(args: ActionArgs) -> bool:
    """Path arguments must resolve inside the repo root; no traversal outside it.
    Prompts must also pass the KnowledgeValidator to prevent prompt injection."""
    path_value = args.get("path")
    if isinstance(path_value, str):
        resolved = (REPO_ROOT / path_value).resolve()
        if resolved != REPO_ROOT and REPO_ROOT not in resolved.parents:
            return False
            
    # Validate prompt content against poisoning/injection
    prompt = args.get("prompt") or args.get("text") or args.get("context")
    if isinstance(prompt, str):
        from reins.harness.trust_anchor import KnowledgeValidator
        score = KnowledgeValidator().validate_update(prompt, "action_gate")
        if score < 0.5:
            return False
            
    return True


def _check_stages(
    context: str,
    tool_name: str,
    args: ActionArgs,
    authorized: bool,
) -> str | None:
    """Run the allowlist/schema/sanitize/billing stages. Returns a rejection reason, or None if all pass."""
    if tool_name not in ALLOWLISTS.get(context, set()):
        return "not_allowlisted"
    if not _schema_valid(tool_name, args):
        return "schema_invalid"
    if not _sanitize_ok(args):
        return "sanitize_failed"
    if tool_name in BILLABLE_TOOLS and not authorized:
        return "billing_or_idempotency_guard"
    return None


def gate_call(
    context: str,
    tool_name: str,
    args: ActionArgs,
    dispatch: Dispatcher,
    authorized: bool = True,
) -> GateResult:
    """
    Run one proposed tool call through the action-gate pipeline. Returns
    ``{"accepted": False, "reason": ...}`` on rejection (dispatch is never
    called), or ``{"accepted": True, "result": dispatch(args)}`` on success.
    """
    reason = _check_stages(context, tool_name, args, authorized)
    if reason is not None:
        _log_rejection(context, tool_name, reason)
        return {"accepted": False, "reason": reason, "result": None}
    return {"accepted": True, "reason": None, "result": dispatch(args)}


def gate_validate(
    context: str,
    tool_name: str,
    args: ActionArgs,
    authorized: bool = True,
) -> ValidationResult:
    """
    Run the same allowlist/schema/sanitize/billing checks as ``gate_call`` but
    never dispatch - for pre-execution checks (e.g. the agent_as_a_judge leaf
    check) that must confirm a proposed action *would* clear the gate without
    actually producing its effect yet. Rejections are still trail-logged.
    """
    reason = _check_stages(context, tool_name, args, authorized)
    if reason is not None:
        _log_rejection(context, tool_name, reason)
        return {"accepted": False, "reason": reason}
    return {"accepted": True, "reason": None}
