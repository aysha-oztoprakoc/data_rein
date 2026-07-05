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
def agent_status() -> str:
    """
    Summarize what every agent identity (data-agy/data-hermes/data-ody/opencode)
    has been doing recently, per the Prime Directive's Rule of Awareness - check
    this before any systemic action to see what's running/pending/failed.
    """
    trail = TaskTrail()
    tasks = trail.all_tasks()
    by_owner: dict[str, dict[str, int]] = {}
    for t in tasks:
        owner = str(t.get("task_type", "generic")).split(":", 1)[0]
        bucket = by_owner.setdefault(owner, {})
        status = t.get("status", "unknown")
        bucket[status] = bucket.get(status, 0) + 1
    failed = trail.get_failed_tasks()
    return json.dumps({
        "by_owner": by_owner,
        "failed_tasks": failed[-10:],
        "total_tasks": len(tasks),
    })


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


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
