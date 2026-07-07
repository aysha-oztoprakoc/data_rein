"""
The reins MCP bridge - gives an interactive front end (OpenCode) first-class,
structured access to the same shared state every other harness agent uses:
the monolith Wiki DB, the Universal Task Trail, and the local-first ModelRouter.

No new state is introduced here. Every tool is a thin wrapper over
``reins.harness.wiki.WikiDB``, ``reins.services.task_trail.TaskTrail``, and
``reins.harness.models.ModelRouter`` - the same objects ``reins`` itself uses,
so an OpenCode session and a `reins run`/`reins trail list` call see one
consistent picture.

Policy encoded here, not just in prompts:
* ``route_local``     - only ever reaches local (Ollama) candidates; cloud is
  never a side effect of a "menial subtask" delegation.
* ``escalate_cloud``   - the only path from OpenCode to Claude/Gemini/OpenAI.
  Always logs a Task Trail entry so a cloud call from OpenCode is exactly as
  auditable as ``reins run``'s own last-resort ``remote_fallback``.
"""

from __future__ import annotations

import json

from mcp.server.fastmcp import FastMCP

from reins.harness.models import ModelRouter
from reins.harness.wiki import WikiDB
from reins.services.task_trail import TaskTrail
from reins.services.token_ledger import budget_report

mcp = FastMCP("reins")


def _row_to_dict(row) -> dict:
    return {k: row[k] for k in row.keys()}


@mcp.tool()
def wiki_search(query: str, limit: int = 8) -> str:
    """Full-text search the shared wiki (pages + memories) for ``query``."""
    with WikiDB() as db:
        res = db.search(query, limit)
    return json.dumps({
        "pages": [_row_to_dict(r) for r in res["pages"]],
        "memories": [_row_to_dict(r) for r in res["memories"]],
    })


@mcp.tool()
def wiki_get(slug: str) -> str:
    """Print one wiki page by slug."""
    with WikiDB() as db:
        row = db.get_page(slug)
    if not row:
        return json.dumps({"error": f"no such page: {slug}"})
    return json.dumps(_row_to_dict(row))


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


def _agent_status_payload() -> dict:
    trail = TaskTrail()
    tasks = trail.all_tasks()
    by_owner: dict[str, dict[str, int]] = {}
    for t in tasks:
        owner = str(t.get("task_type", "generic")).split(":", 1)[0]
        bucket = by_owner.setdefault(owner, {})
        status = t.get("status", "unknown")
        bucket[status] = bucket.get(status, 0) + 1
    failed = trail.get_failed_tasks()
    return {
        "by_owner": by_owner,
        "failed_tasks": failed[-10:],
        "total_tasks": len(tasks),
    }


@mcp.tool()
def agent_status() -> str:
    """
    Summarize what every agent identity (data-agy/data-hermes/data-ody/opencode)
    has been doing recently, per the Prime Directive's Rule of Awareness - check
    this before any systemic action to see what's running/pending/failed.
    """
    return json.dumps(_agent_status_payload())


@mcp.tool()
def route_local(category: str, prompt: str, node: str = "amdy") -> str:
    """
    Delegate a menial subtask (summarize/classify/extract/etc.) to a local Ollama
    model instead of spending an OpenCode agent turn on it. Never reaches cloud -
    for that, the caller must use ``escalate_cloud`` only when the user asked.
    """
    router = ModelRouter()
    res = router.route(category, prompt, node, allow_fallback=True, allow_cloud=False)
    return json.dumps({"ok": res.ok, "model": res.model, "node": res.node, "text": res.text, "error": res.error})


@mcp.tool()
def escalate_cloud(prompt: str, provider: str = "") -> str:
    """
    Explicit, user-requested Claude/Gemini/OpenAI call. Only call this tool when
    the user has explicitly asked to use Claude or Gemini - never as a default or
    automatic step. Every call is logged to the Task Trail for auditability.
    """
    trail = TaskTrail()
    task_id = trail.create_task("opencode:cloud-escalation", prompt, "cloud")
    trail.update_task(task_id, "running")

    router = ModelRouter()
    res = router.route_cloud(prompt, provider=provider or None)

    trail.update_task(task_id, "success" if res.ok else "failed")
    return json.dumps({
        "ok": res.ok, "model": res.model, "provider": res.provider,
        "text": res.text, "error": res.error, "task_id": task_id,
        "usage": budget_report().get(res.provider, {}) if res.ok else {},
    })


@mcp.tool()
def token_usage_status(provider: str = "") -> str:
    """
    Show self-tracked Claude/Gemini/OpenAI usage vs configured budgets across the
    5-hour, daily, weekly, and monthly rolling windows - answers "how much of my
    quota have I used right now?" Call this any time the user asks about usage or
    before an escalate_cloud call if you want to warn them they're close to a limit.
    Budgets come from config/token_budgets.json (user-editable; unset = 0 = no %%
    shown, just raw counts) since neither provider exposes a remaining-quota API.
    """
    report = budget_report()
    if provider:
        report = {provider: report.get(provider, {})}
    return json.dumps(report)


@mcp.tool()
def trail_queue(goal: str, context: str = "", task_type: str = "generic", node: str = "amdy") -> str:
    """
    Queue a chunked task on the Task Trail for local-model (maestro) pickup -
    ``goal``+``context`` are split to fit qwen2.5-coder:7b's window and
    executed one chunk at a time via ``trail_pickup``, so long work can
    continue on the local node between OpenCode turns.
    """
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

    return json.dumps(get_coordinator().status())


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
def dataset_export(out_path: str, categories: str = "", modality: str = "", kind: str = "completion",
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

    return json.dumps(SysProfiler().profile_cluster(publish=False))


@mcp.tool()
def hardware_gaps() -> str:
    """Report hardware capability gaps (e.g. missing quantization/ROCm support) against the harness's needs."""
    from reins.services.sys_profiler import SysProfiler

    return json.dumps(SysProfiler().gap_report())


@mcp.tool()
def train_status() -> str:
    """Probe local QLoRA/LoRA fine-tuning capability (NF4/fp16/CPU degradation chain) without starting a run."""
    from dataclasses import asdict

    from reins.training import capability

    return json.dumps(asdict(capability.probe()))


def main(http: bool = False, host: str = "127.0.0.1", port: int = 8765) -> None:
    """
    Default (``http=False``): stdio transport, unchanged - what Claude Code,
    OpenCode, and Antigravity already use. ``http=True`` instead serves the
    same tools over streamable-HTTP, the transport a Docker container (e.g.
    the Odysseus dashboard, which can't share a stdio pipe with the host)
    needs to reach this server as a network client.
    """
    if http:
        mcp.settings.host = host
        mcp.settings.port = port
        mcp.run(transport="streamable-http")
    else:
        mcp.run()


if __name__ == "__main__":
    main()
