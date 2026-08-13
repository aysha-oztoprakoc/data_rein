"""MCP access to the shared Wiki, Task Trail, and model-agnostic router.

``route_local`` remains on the local plane. ``escalate_cloud`` is the explicit,
trail-logged cloud boundary. The bridge creates no state of its own.
"""

from __future__ import annotations

import json
import sqlite3
from typing import Literal, Protocol

from mcp.server.auth.settings import AuthSettings
from mcp.server.fastmcp import FastMCP
from pydantic import AnyHttpUrl

from reins.harness.action_gate import ActionArgs, gate_call
from reins.harness.coordinator import CoordinatorStatus as CoordinatorStatusPayload
from reins.harness.dispatch import dispatch_cloud_generate, dispatch_local_generate
from reins.harness.inference_mcp import register_inference_tools
from reins.harness.mcp_security import (
    BearerTokenVerifier,
    McpHttpConfigurationError,
    SecretLoader,
    configure_http_security,
    is_loopback_host,
    load_http_token,
)
from reins.harness.provider_protocols import JsonValue
from reins.harness.wiki import WikiDB
from reins.services.task_trail import TaskTrail
from reins.services.token_ledger import budget_report

_http_token_verifier = BearerTokenVerifier()
mcp = FastMCP(
    "reins",
    token_verifier=_http_token_verifier,
    auth=AuthSettings(
        issuer_url=AnyHttpUrl("http://127.0.0.1"),
        resource_server_url=None,
    ),
)
register_inference_tools(mcp)


class CoordinatorStatus(Protocol):
    def status(self) -> "CoordinatorStatusPayload": ...


class HardwareStatus(Protocol):
    def profile_cluster(self, publish: bool = True) -> JsonValue: ...

    def gap_report(self) -> JsonValue: ...


def _coordinator_status(coordinator: CoordinatorStatus) -> CoordinatorStatusPayload:
    return coordinator.status()


def _hardware_profile(profiler: HardwareStatus) -> JsonValue:
    return profiler.profile_cluster(publish=False)


def _hardware_gaps(profiler: HardwareStatus) -> JsonValue:
    return profiler.gap_report()


def _row_to_json(row: sqlite3.Row) -> str:
    return json.dumps({key: row[key] for key in row.keys()})


@mcp.tool()
def wiki_search(query: str, limit: int = 8) -> str:
    """Full-text search the shared wiki (pages + memories) for ``query``."""
    with WikiDB() as db:
        res = db.search(query, limit)
    pages = ",".join(_row_to_json(row) for row in res["pages"])
    memories = ",".join(_row_to_json(row) for row in res["memories"])
    return f'{{"pages":[{pages}],"memories":[{memories}]}}'


@mcp.tool()
def wiki_get(slug: str) -> str:
    """Print one wiki page by slug."""
    with WikiDB() as db:
        row = db.get_page(slug)
    if not row:
        return json.dumps({"error": f"no such page: {slug}"})
    return _row_to_json(row)


@mcp.tool()
def wiki_add_memory(text: str, category: str = "general") -> str:
    """Store an atomic fact in the shared wiki, attributed to opencode."""
    with WikiDB() as db:
        uid = db.add_memory(text, category=category, source="opencode", owner="opencode")
    return json.dumps({"uid": uid})


@mcp.tool()
def trail_list(status: str = "") -> str:
    """List Task Trail entries, optionally filtered to one status."""
    trail = TaskTrail()
    tasks = trail.by_status(status) if status else trail.all_tasks()
    return json.dumps(tasks[-25:])


@mcp.tool()
def trail_create(task_type: str, prompt: str, target_node: str = "amdy") -> str:
    """Create a Task Trail entry (status=pending) so other agents see this work."""
    trail = TaskTrail()
    task_id = trail.create_task(f"opencode:{task_type}", prompt, target_node)
    return json.dumps({"task_id": task_id})


@mcp.tool()
def trail_update(task_id: str, status: str) -> str:
    """Update a Task Trail entry's status (pending/running/success/failed/...)."""
    trail = TaskTrail()
    trail.update_task(task_id, status)
    return json.dumps({"task_id": task_id, "status": status})


@mcp.tool()
def agent_budgets() -> str:
    """Show every known agent's CPU%/GPU-VRAM-GB resource budget."""
    from reins.services.resource_budgets import load_budgets

    return json.dumps(load_budgets())


@mcp.tool()
def set_agent_budget(agent_name: str, cpu_pct: int = -1, gpu_vram_gb: float = -1.0) -> str:
    """
    Update one agent's resource budget. Pass only the field(s) you want to
    change; leave the other at its sentinel default (-1 / -1.0) to leave it
    untouched. Returns the full updated budgets dict.
    """
    from reins.services.resource_budgets import save_budget

    budgets = save_budget(
        agent_name,
        cpu_pct=cpu_pct if cpu_pct >= 0 else None,
        gpu_vram_gb=gpu_vram_gb if gpu_vram_gb >= 0 else None,
    )
    return json.dumps(budgets)


@mcp.tool()
def agent_status() -> str:
    """
    Summarize what every agent identity (data-agy/data-hermes/data-ody/opencode)
    has been doing recently, per the Prime Directive's Rule of Awareness - check
    this before any systemic action to see what's running/pending/failed.
    """
    trail = TaskTrail()
    tasks = trail.all_tasks()
    by_owner: dict[str, dict[str, int]] = {}
    for task in tasks:
        owner = str(task.get("task_type", "generic")).split(":", 1)[0]
        status = str(task.get("status", "unknown"))
        bucket = by_owner.setdefault(owner, {})
        bucket[status] = bucket.get(status, 0) + 1
    return json.dumps({
        "by_owner": by_owner,
        "failed_tasks": trail.get_failed_tasks()[-10:],
        "total_tasks": len(tasks),
    })


@mcp.tool()
def route_local(category: str, prompt: str, node: str = "amdy") -> str:
    """
    Delegate a menial subtask (summarize/classify/extract/etc.) to a local Ollama
    model instead of spending an OpenCode agent turn on it. Never reaches cloud -
    for that, the caller must use ``escalate_cloud`` only when the user asked.

    Routed through the action_gate (blueprint.yaml action_gates): the proposed
    call is allowlist/schema/sanitize-checked before ModelRouter.route ever runs.
    """
    args: ActionArgs = {"prompt": prompt, "category": category, "node": node}
    gated = gate_call("route_local", "local_generate", args, dispatch_local_generate)
    if not gated["accepted"]:
        return json.dumps({"ok": False, "model": None, "node": node, "text": None, "error": gated["reason"]})
    return json.dumps(gated["result"])


@mcp.tool()
def escalate_cloud(prompt: str, provider: str = "") -> str:
    """
    Explicit, user-requested Claude/Gemini/OpenAI call. Only call this tool when
    the user has explicitly asked to use Claude or Gemini - never as a default or
    automatic step. Every call is logged to the Task Trail for auditability.

    Routed through the action_gate (blueprint.yaml action_gates): calling this
    tool at all is the explicit user authorization the billing guard requires.
    """
    args: ActionArgs = {
        "prompt": prompt,
        "provider": provider,
        "task_type": "opencode:cloud-escalation",
    }
    gated = gate_call("escalate_cloud", "cloud_generate", args, dispatch_cloud_generate, authorized=True)
    if not gated["accepted"]:
        return json.dumps({
            "ok": False, "model": None, "provider": provider or None,
            "text": None, "error": gated["reason"], "task_id": None, "usage": {},
        })
    return json.dumps(gated["result"])


@mcp.tool()
def judge_submit_graph(graph_id: str, nodes: str, edges: str = "[]") -> str:
    """Validate and judge a model-proposed dependency graph before dispatch."""
    from reins.harness.judge import execute_graph_json

    outcome = execute_graph_json(graph_id, nodes, edges)
    return json.dumps(outcome)


@mcp.tool()
def token_usage_status(provider: str = "") -> str:
    """Show self-tracked cloud usage and configured rolling-window budgets."""
    report = budget_report()
    if provider:
        report = {provider: report.get(provider, {})}
    return json.dumps(report)


@mcp.tool()
def trail_queue(goal: str, context: str = "", task_type: str = "generic", node: str = "amdy") -> str:
    """Queue a chunked Task Trail job for local-model pickup."""
    from reins.harness.handoff import queue_chunked_task

    context_blocks = [context] if context else []
    task_id = queue_chunked_task(task_type, goal, context_blocks, node=node)
    return json.dumps({"task_id": task_id})


@mcp.tool()
def trail_pickup(category: str = "coding: menial", node: str = "amdy") -> str:
    """Execute exactly one queued chunk (maestro fast-path, ModelRouter fallback)."""
    from reins.harness.handoff import pickup_next

    result = pickup_next(category=category, node=node)
    return json.dumps(result if result is not None else {"status": "empty"})


@mcp.tool()
def coord_status() -> str:
    """Show the local model-residency coordinator's slot state (loaded/loading/busy models, VRAM budget)."""
    from reins.harness.coordinator import get_coordinator

    return json.dumps(_coordinator_status(get_coordinator()))


@mcp.tool()
def coord_load(model: str) -> str:
    """Warm-load a model into the coordinator's residency plane (admits against the VRAM budget, may evict LRU)."""
    from dataclasses import asdict

    from reins.harness.coordinator import get_coordinator

    slot = get_coordinator().load(model)
    return json.dumps(asdict(slot), default=str)


@mcp.tool()
def coord_unload(model: str) -> str:
    """Unload a model from the coordinator's residency plane, freeing its VRAM budget."""
    from dataclasses import asdict

    from reins.harness.coordinator import get_coordinator

    slot = get_coordinator().unload(model)
    return json.dumps(asdict(slot), default=str)


@mcp.tool()
def dataset_export(out_path: str, categories: str = "", modality: str = "",
                    kind: Literal["completion", "memories"] = "completion",
                    min_chars: int = 64, limit: int = 0) -> str:
    """
    Export the wiki into a JSONL training/eval dataset for local fine-tuning.
    ``categories`` is a comma-separated list; ``modality`` filters e.g. text/image/audio.
    """
    from dataclasses import asdict

    from reins.harness.dataset import export_jsonl

    cats = [c.strip() for c in categories.split(",") if c.strip()] or None
    stats = export_jsonl(out_path, categories=cats, modality=modality or None, kind=kind,
                          min_chars=min_chars, limit=limit)
    return json.dumps(asdict(stats))


@mcp.tool()
def hardware_scan() -> str:
    """Profile the local hardware cluster (VRAM/RAM/CPU, model fit scoring) without publishing to MQTT."""
    from reins.services.sys_profiler import SysProfiler

    return json.dumps(_hardware_profile(SysProfiler()))


@mcp.tool()
def hardware_gaps() -> str:
    """Report hardware capability gaps (e.g. missing quantization/ROCm support) against the harness's needs."""
    from reins.services.sys_profiler import SysProfiler

    return json.dumps(_hardware_gaps(SysProfiler()))


@mcp.tool()
def train_status() -> str:
    """Probe local QLoRA/LoRA fine-tuning capability (NF4/fp16/CPU degradation chain) without starting a run."""
    from dataclasses import asdict

    from reins.training import capability

    return json.dumps(asdict(capability.probe()))


def main(
    http: bool = False,
    host: str = "127.0.0.1",
    port: int = 8765,
    *,
    allow_remote_http: bool = False,
    secret_loader: SecretLoader | None = None,
) -> None:
    """
    Default (``http=False``): stdio transport, unchanged - what Claude Code,
    OpenCode, and Antigravity already use. ``http=True`` instead serves the
    same tools over streamable-HTTP, the transport a Docker container (e.g.
    the Odysseus dashboard, which can't share a stdio pipe with the host)
    needs to reach this server as a network client.
    """
    if http:
        if not is_loopback_host(host) and not allow_remote_http:
            raise McpHttpConfigurationError(
                "non-loopback HTTP MCP requires --allow-remote-http"
            )
        token = load_http_token(secret_loader)
        _http_token_verifier.configure(token)
        _ = configure_http_security(mcp, host)
        mcp.settings.host = host
        mcp.settings.port = port
        try:
            mcp.run(transport="streamable-http")
        except KeyboardInterrupt:
            return
    else:
        mcp.run()


if __name__ == "__main__":
    main()
