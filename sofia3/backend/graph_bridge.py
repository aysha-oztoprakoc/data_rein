"""Graph bridge — assembles the unified knowledge graph from reins state.

Inputs (all single source of truth):
  * Wiki DB pages + memories (reins.harness.wiki.WikiDB)
  * Task Trail (reins.services.task_trail.TaskTrail)
  * Model registry (config/model_registry.json via paths.model_registry)

Node model (decision #7):
  Task / Agent / Page / Memory / Model + hub nodes Category, Owner, Session.

Edges:
  Task→Agent (target_node) · Task→Owner (task_type owner) · Memory→Page
  (source_path) · Page/Memory→Category · Page/Memory→Owner · Memory→Session ·
  Memory→Model (model name match).

Rendering: semantica ContextGraph is the builder; the frontend draws it with
react-force-graph from `to_dict()` JSON. Analytics that need the heavy `kg`
subpackage (centrality, community detection) are reported as unavailable and
degrade gracefully — see third_party/semantica/README.md.
"""

from __future__ import annotations

import json
import logging
import time
from typing import Any, Optional

logger = logging.getLogger("sofia3.graph_bridge")

# TTL cache: the graph is large (~2k nodes), so rebuild it at most every N sec.
_GRAPH_TTL = 60.0
_cache: dict[str, Any] = {"at": 0.0, "payload": None}

_GRAPH_AVAILABLE = False
_GRAPH_ERROR: Optional[str] = None
try:
    from semantica.context import ContextGraph  # noqa: F401

    _GRAPH_AVAILABLE = True
except ImportError as exc:
    _GRAPH_AVAILABLE = False
    _GRAPH_ERROR = f"vendored semantica not available ({exc})"


def available() -> bool:
    return _GRAPH_AVAILABLE


def _safe(builder: Any) -> dict[str, Any]:
    """Run a loader; on any failure return a degraded envelope."""
    try:
        return builder()
    except Exception as exc:  # graceful degradation
        logger.warning("graph source read degraded: %s", exc)
        return {"degraded": True, "error": str(exc)}


def _load_pages() -> list[dict[str, Any]]:
    from reins.harness.wiki import WikiDB

    with WikiDB() as db:
        return [dict(p) for p in db.list_pages(limit=5000, offset=0, order="recent")]


def _load_memories() -> list[dict[str, Any]]:
    from reins.harness.wiki import WikiDB

    with WikiDB() as db:
        rows = db.conn.execute(
            "SELECT uid, text, category, source, owner, session_id, timestamp FROM memories"
        ).fetchall()
        return [dict(r) for r in rows]


def _load_tasks() -> list[dict[str, Any]]:
    from reins.services.task_trail import TaskTrail

    return TaskTrail().all_tasks()


def _load_models() -> list[dict[str, str]]:
    from reins.harness import paths

    # model_registry.json is a hardware profile (overwritten by SysProfiler);
    # the static model catalog is the canonical candidate-model list.
    path = paths.model_catalog()
    if not path.is_file():
        return []
    raw = json.loads(path.read_text(encoding="utf-8"))
    # Catalog shape: {"_comment": str, "candidates": [{model, backend, ...}]}.
    if isinstance(raw, dict):
        raw = raw.get("candidates", raw)
    models: list[dict[str, str]] = []
    # Catalog may be a dict keyed by model id, or a list.
    if isinstance(raw, dict):
        for key, value in raw.items():
            if isinstance(value, dict):
                models.append(
                    {
                        "id": str(value.get("model", key)),
                        "name": str(value.get("model", key)),
                        "provider": str(value.get("backend", "")),
                    }
                )
            else:
                models.append({"id": str(key), "name": str(key), "provider": ""})
    elif isinstance(raw, list):
        for value in raw:
            if isinstance(value, dict):
                models.append(
                    {
                        "id": str(value.get("model", value.get("id", ""))),
                        "name": str(value.get("model", value.get("name", ""))),
                        "provider": str(value.get("backend", value.get("provider", ""))),
                    }
                )
    return models


def _hub_id(kind: str, name: str) -> str:
    return f"{kind}:{name}"


def build_graph() -> dict[str, Any]:
    """Assemble the unified graph through semantica ContextGraph."""
    if not _GRAPH_AVAILABLE:
        return {"degraded": True, "error": _GRAPH_ERROR or "graph bridge unavailable"}

    now = time.time()
    if _cache["payload"] is not None and now - _cache["at"] < _GRAPH_TTL:
        return _cache["payload"]

    pages = _safe(_load_pages)
    memories = _safe(_load_memories)
    tasks = _safe(_load_tasks)
    models = _safe(_load_models)

    pages = pages if isinstance(pages, list) else []
    memories = memories if isinstance(memories, list) else []
    tasks = tasks if isinstance(tasks, list) else []
    models = models if isinstance(models, list) else []

    # Map page source_path basename -> slug so Memory→Page provenance edges
    # resolve exactly (memory.source is a filename, not a slug).
    page_by_source: dict[str, str] = {}
    for page in pages:
        src = page.get("source_path") or ""
        if src:
            page_by_source[src.split("/")[-1].lower()] = page.get("slug") or page.get("title") or ""

    g = ContextGraph()
    model_names = {m.get("name", "").lower() for m in models} | {m.get("id", "").lower() for m in models}

    def ensure_hub(kind: str, name: str) -> str:
        h = _hub_id(kind, name)
        g.add_node(h, kind, content=name)
        return h

    # -- nodes -----------------------------------------------------------------
    for page in pages:
        slug = page.get("slug") or page.get("title") or "page"
        g.add_node(f"page:{slug}", "Page", content=page.get("title") or slug,
                   category=page.get("category") or "general", owner=page.get("owner") or "unknown")
    for mem in memories:
        uid = mem.get("uid") or "mem"
        g.add_node(f"memory:{uid}", "Memory", content=str(mem.get("text") or "")[:140],
                   category=mem.get("category") or "general", owner=mem.get("owner") or "unknown",
                   session=mem.get("session_id") or "")
    for task in tasks:
        tid = task.get("task_id") or "task"
        g.add_node(f"task:{tid}", "Task", content=str(task.get("prompt") or tid)[:140],
                   status=task.get("status") or "pending", target_node=task.get("target_node") or "amdy")
    for agent in sorted({t.get("target_node") or "amdy" for t in tasks}):
        ensure_hub("Agent", agent)
    for model in models:
        mname = model.get("name") or model.get("id")
        if mname:
            g.add_node(f"model:{mname}", "Model", content=mname, provider=model.get("provider") or "")

    # -- edges -----------------------------------------------------------------
    # Task→Agent and Task→Owner
    for task in tasks:
        tid = task.get("task_id") or "task"
        node = f"task:{tid}"
        target = task.get("target_node") or "amdy"
        if target:
            g.add_edge(node, _hub_id("Agent", target), edge_type="executed_by")
        owner = str(task.get("task_type", "generic")).split(":", 1)[0]
        if owner:
            g.add_edge(node, ensure_hub("Owner", owner), edge_type="belongs_to")
    # Memory→Page (provenance), Memory→Category/Owner/Session/Model
    for mem in memories:
        uid = mem.get("uid") or "mem"
        node = f"memory:{uid}"
        src = str(mem.get("source") or "").split("/")[-1].lower()
        target_slug = page_by_source.get(src) if src else None
        if target_slug:
            g.add_edge(node, f"page:{target_slug}", edge_type="derived_from")
        cat = mem.get("category") or "general"
        if cat:
            g.add_edge(node, ensure_hub("Category", cat), edge_type="in_category")
        owner = mem.get("owner") or "unknown"
        if owner:
            g.add_edge(node, ensure_hub("Owner", owner), edge_type="authored_by")
        session = mem.get("session_id")
        if session:
            g.add_edge(node, ensure_hub("Session", session), edge_type="in_session")
        text = str(mem.get("text") or "").lower()
        for mname in model_names:
            if mname and mname in text:
                g.add_edge(node, f"model:{mname}", edge_type="about_model")
                break
    # Page→Category/Owner
    for page in pages:
        slug = page.get("slug") or page.get("title") or "page"
        node = f"page:{slug}"
        cat = page.get("category") or "general"
        if cat:
            g.add_edge(node, ensure_hub("Category", cat), edge_type="in_category")
        owner = page.get("owner") or "unknown"
        if owner:
            g.add_edge(node, ensure_hub("Owner", owner), edge_type="authored_by")

    stats = g.stats()
    payload = {
        "degraded": False,
        "stats": stats,
        "graph": g.to_dict(),
        "built_at": now,
        "ttl": _GRAPH_TTL,
        "notes": {
            "pages": len(pages),
            "memories": len(memories),
            "tasks": len(tasks),
            "models": len(models),
            "centrality": "unavailable (heavy kg subpackage not vendored)",
            "communities": "unavailable (heavy kg subpackage not vendored)",
        },
    }
    _cache["at"] = now
    _cache["payload"] = payload
    return payload


def invalidate() -> None:
    _cache["at"] = 0.0
    _cache["payload"] = None
