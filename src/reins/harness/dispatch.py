"""
Tool dispatch registry: the real functions a judge-approved, gate-cleared
leaf action is allowed to invoke. Kept separate from `action_gate` (generic
pipeline) and `judge` (graph evaluation) so each module has one job.

Node targeting defaults to amdy only - tell is offline/unreachable, so no
dispatcher here ever targets it until a live hardware scan brings it back
(knowledge_base/HARDWARE.md).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

from typing_extensions import override

from reins.harness.action_gate import ActionArgs, ActionResult, Dispatcher, REPO_ROOT
from reins.harness.models import ModelRouter
from reins.services.task_trail import TaskTrail
from reins.services.token_ledger import budget_report


@dataclass(frozen=True, slots=True)
class InvalidActionArgumentError(TypeError):
    key: str

    @override
    def __str__(self) -> str:
        return f"{self.key} must be a string"


def _string_arg(args: ActionArgs, key: str, default: str | None = None) -> str:
    value = args.get(key, default)
    if isinstance(value, str):
        return value
    raise InvalidActionArgumentError(key)


def dispatch_local_generate(args: ActionArgs) -> ActionResult:
    """Route a menial subtask to a local (Ollama) model on amdy. Never reaches cloud."""
    router = ModelRouter()
    res = router.route(
        _string_arg(args, "category", "general chatting"),
        _string_arg(args, "prompt"),
        _string_arg(args, "node", "amdy"),
        allow_fallback=True,
    )
    return {
        "ok": res.ok,
        "model": res.model,
        "provider": res.provider,
        "node": res.node,
        "text": res.text,
        "error": res.error,
    }


def dispatch_cloud_generate(args: ActionArgs) -> ActionResult:
    """Explicit cloud call, logged to the Task Trail for auditability."""
    trail = TaskTrail()
    prompt = _string_arg(args, "prompt")
    task_id = trail.create_task(_string_arg(args, "task_type", "cloud-escalation"), prompt, "cloud")
    trail.update_task(task_id, "running")

    router = ModelRouter()
    provider = args.get("provider")
    res = router.route_cloud(prompt, provider=provider if isinstance(provider, str) else None)

    trail.update_task(task_id, "success" if res.ok else "failed")
    report: ActionResult = budget_report()
    raw_usage = report.get(res.provider, {}) if res.ok else {}
    usage = raw_usage if isinstance(raw_usage, dict) else {}
    return {
        "ok": res.ok,
        "model": res.model,
        "provider": res.provider,
        "text": res.text,
        "error": res.error,
        "task_id": task_id,
        "usage": usage,
    }


def dispatch_read_file(args: ActionArgs) -> ActionResult:
    """Read a file within the repo root. Degrades to an error payload, never raises."""
    resolved = (REPO_ROOT / _string_arg(args, "path")).resolve()
    try:
        return {"ok": True, "text": resolved.read_text(encoding="utf-8", errors="replace")}
    except OSError as exc:
        return {"ok": False, "error": str(exc)}


TOOL_DISPATCHERS: Final[dict[str, Dispatcher]] = {
    "local_generate": dispatch_local_generate,
    "cloud_generate": dispatch_cloud_generate,
    "read_file": dispatch_read_file,
}
