"""Graph bridge — assembles the unified knowledge graph directly via Kùzu & reins state.

Replaces vendored semantica ContextGraph with direct, high-performance Kùzu graph queries.

Inputs (all single source of truth):
  * Kùzu Graph DB (knowledge graph chunks, documents, memories, relations)
  * Wiki DB pages + memories fallback (reins.harness.wiki.WikiDB)
  * Task Trail (reins.services.task_trail.TaskTrail)
  * Model registry (config/model_catalog.json via paths.model_catalog)
  * Skill registry (reins.harness.skill_registry)

PON compliance:
  * zero polling — reads on-demand, cache invalidated reactively on events.
  * graceful degradation — database / catalog anomalies degrade without crashing.
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from reins.harness import paths

logger = logging.getLogger("sofia3.graph_bridge")

# TTL cache: rebuild graph at most every N sec unless invalidated
_GRAPH_TTL = 60.0
_cache: dict[str, Any] = {"at": 0.0, "payload": None}

_KUZU_AVAILABLE = False
try:
    import kuzu  # type: ignore

    _KUZU_AVAILABLE = True
except ImportError:
    _KUZU_AVAILABLE = False


def available() -> bool:
    return True


def _safe(builder: Any) -> Any:
    """Run a loader; on any failure return empty list / fallback."""
    try:
        return builder()
    except Exception as exc:
        logger.warning("graph source read degraded: %s", exc)
        return []


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
    path = paths.model_catalog()
    if not path.is_file():
        return []
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    if isinstance(raw, dict):
        raw = raw.get("candidates", raw)
    models: list[dict[str, str]] = []
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


def _load_skills() -> list[dict[str, Any]]:
    try:
        from reins.harness.skill_registry import canonical_skills

        skills = canonical_skills()
        results = []
        for s in skills:
            mtime = s.path.stat().st_mtime if s.path.exists() else 0
            results.append(
                {
                    "name": s.name,
                    "description": s.description,
                    "path": str(s.path),
                    "updated_at": mtime,
                }
            )
        return results
    except Exception as exc:
        logger.warning("skills loading degraded in graph bridge: %s", exc)
        return []


def classify_domain(category: str, text: str = "") -> str:
    cat = (category or "").lower()
    t = (text or "").lower()
    if any(k in cat for k in ["pon", "architecture", "system", "directive", "kad", "sofia3"]):
        return "Architecture & PON"
    if any(
        k in cat
        for k in [
            "tdd",
            "python",
            "code-review",
            "codebase",
            "refactor",
            "diagnos",
            "git",
            "wizard",
            "qa",
            "triage",
            "prototype",
            "domain",
            "ubiquitous",
            "spec",
            "ticket",
            "wayfinder",
            "handoff",
        ]
    ):
        return "Core Engineering & TDD"
    if any(
        k in cat
        for k in [
            "fuzz",
            "sanitizer",
            "vuln",
            "audit",
            "security",
            "c-review",
            "rust-review",
            "codeql",
            "semgrep",
            "trailmark",
            "yara",
            "zeroize",
            "sarif",
            "fp-check",
            "burp",
            "wyche",
        ]
    ):
        return "AppSec & Fuzzing"
    if any(
        k in cat
        for k in [
            "paper",
            "lean",
            "proof",
            "culture",
            "writing",
            "article",
            "academic",
            "fate",
            "tcc",
            "abnt",
            "teach",
            "book",
        ]
    ):
        return "Academic & Writing"
    if any(k in cat for k in ["model", "router", "token", "budget", "hardware", "coordinator", "vram"]):
        return "Fleet Models & Hardware"
    if any(k in cat for k in ["corpus", "ingested", "digest", "sofia_protocol", "wiki", "history"]):
        return "Corpus & Knowledge Base"
    if any(k in cat for k in ["log", "task", "telemetry", "system", "audit-trail"]):
        return "System Logs, Tasks & Telemetry"
    return "General Knowledge"


def _hub_id(kind: str, name: str) -> str:
    return f"{kind}:{name}"


def _load_kuzu_graph_elements(kuzu_dir: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Query persistent Kùzu graph DB for chunk nodes and relations if available."""
    if not _KUZU_AVAILABLE or not kuzu_dir.exists():
        return [], []

    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []
    try:
        import kuzu  # type: ignore

        db = kuzu.Database(str(kuzu_dir))
        conn = kuzu.Connection(db)

        # Chunks
        try:
            res = conn.execute("MATCH (c:Chunk) RETURN c.id, c.content, c.token_count LIMIT 500;")
            while res.has_next():
                row = res.get_next()
                cid, content, token_cnt = row[0], row[1], row[2]
                nodes.append(
                    {
                        "id": f"chunk:{cid}",
                        "type": "Chunk",
                        "content": str(content)[:100] + ("..." if len(str(content)) > 100 else ""),
                        "properties": {"token_count": token_cnt, "chunk_id": cid},
                        "metadata": {"token_count": token_cnt},
                    }
                )
        except Exception:
            pass

        # Contains (Document -> Chunk)
        try:
            res = conn.execute("MATCH (d:Document)-[r:Contains]->(c:Chunk) RETURN d.slug, c.id LIMIT 1000;")
            while res.has_next():
                row = res.get_next()
                slug, cid = row[0], row[1]
                edges.append(
                    {
                        "id": f"edge:page:{slug}->chunk:{cid}",
                        "source": f"page:{slug}",
                        "target": f"chunk:{cid}",
                        "type": "contains",
                    }
                )
        except Exception:
            pass

        # DerivesFrom (MemoryNode -> Chunk)
        try:
            res = conn.execute("MATCH (m:MemoryNode)-[r:DerivesFrom]->(c:Chunk) RETURN m.uid, c.id LIMIT 1000;")
            while res.has_next():
                row = res.get_next()
                uid, cid = row[0], row[1]
                edges.append(
                    {
                        "id": f"edge:memory:{uid}->chunk:{cid}",
                        "source": f"memory:{uid}",
                        "target": f"chunk:{cid}",
                        "type": "derives_from",
                    }
                )
        except Exception:
            pass

    except Exception as exc:
        logger.debug("Kùzu graph loading error: %s", exc)

    return nodes, edges


def build_graph() -> dict[str, Any]:
    """Assemble the unified graph directly via Kùzu and canonical reins state."""
    now = time.time()
    if _cache["payload"] is not None and now - _cache["at"] < _GRAPH_TTL:
        return _cache["payload"]

    pages = _safe(_load_pages) or []
    memories = _safe(_load_memories) or []
    tasks = _safe(_load_tasks) or []
    models = _safe(_load_models) or []
    skills = _safe(_load_skills) or []

    nodes_map: dict[str, dict[str, Any]] = {}
    edges_list: list[dict[str, Any]] = []
    edge_ids: Set[str] = set()

    def add_node(nid: str, ntype: str, content: str, **kwargs: Any) -> None:
        if nid not in nodes_map:
            nodes_map[nid] = {
                "id": nid,
                "type": ntype,
                "content": content,
                "properties": kwargs,
                "metadata": kwargs,
            }

    def add_edge(source: str, target: str, edge_type: str, weight: float = 1.0) -> None:
        eid = f"e:{source}->{target}:{edge_type}"
        if eid not in edge_ids:
            edge_ids.add(eid)
            edges_list.append(
                {
                    "id": eid,
                    "source": source,
                    "target": target,
                    "type": edge_type,
                    "weight": weight,
                }
            )

    def ensure_hub(kind: str, name: str) -> str:
        hid = _hub_id(kind, name)
        add_node(hid, kind, content=name)
        return hid

    # 1. Pages
    page_by_source: dict[str, str] = {}
    for page in pages:
        slug = page.get("slug") or page.get("title") or "page"
        cat = page.get("category") or "general"
        domain = classify_domain(cat, page.get("title") or "")
        origin = page.get("owner") or "knowledge_base"
        date_val = page.get("updated_at") or page.get("created_at") or ""
        src = page.get("source_path") or ""
        if src:
            page_by_source[src.split("/")[-1].lower()] = slug

        add_node(
            f"page:{slug}",
            "Page",
            content=page.get("title") or slug,
            category=cat,
            domain=domain,
            origin=origin,
            owner=origin,
            date=date_val,
        )

    # 2. Memories
    for mem in memories:
        uid = mem.get("uid") or "mem"
        cat = mem.get("category") or "general"
        domain = classify_domain(cat, str(mem.get("text") or ""))
        origin = mem.get("owner") or "memory"
        ts = mem.get("timestamp") or 0
        date_str = time.strftime("%Y-%m-%d", time.gmtime(ts)) if ts else ""
        add_node(
            f"memory:{uid}",
            "Memory",
            content=str(mem.get("text") or "")[:140],
            category=cat,
            domain=domain,
            origin=origin,
            owner=origin,
            session=mem.get("session_id") or "",
            date=date_str,
        )

    # 3. Skills
    for skill in skills:
        sname = skill.get("name") or "skill"
        domain = classify_domain(sname, skill.get("description") or "")
        mtime = skill.get("updated_at") or 0
        date_str = time.strftime("%Y-%m-%d", time.gmtime(mtime)) if mtime else ""
        add_node(
            f"skill:{sname}",
            "Skill",
            content=sname,
            domain=domain,
            origin="skills",
            description=skill.get("description") or "",
            path=skill.get("path") or "",
            date=date_str,
        )

    # 4. Tasks
    for task in tasks:
        tid = task.get("task_id") or "task"
        ts = task.get("timestamp") or 0
        date_str = time.strftime("%Y-%m-%d", time.gmtime(ts)) if ts else ""
        add_node(
            f"task:{tid}",
            "Task",
            content=str(task.get("prompt") or tid)[:140],
            status=task.get("status") or "pending",
            target_node=task.get("target_node") or "amdy",
            domain="System Logs, Tasks & Telemetry",
            origin=task.get("target_node") or "amdy",
            date=date_str,
        )

    # 5. Models
    model_names = {m.get("name", "").lower() for m in models} | {m.get("id", "").lower() for m in models}
    for model in models:
        mname = model.get("name") or model.get("id")
        if mname:
            add_node(
                f"model:{mname}",
                "Model",
                content=mname,
                provider=model.get("provider") or "",
                origin="model_registry",
                domain="Fleet Models & Hardware",
            )

    # 6. Kùzu Chunks & Rel edges
    kuzu_nodes, kuzu_edges = _load_kuzu_graph_elements(paths.kuzu_db_dir())
    for kn in kuzu_nodes:
        nodes_map[kn["id"]] = kn
    for ke in kuzu_edges:
        if ke["id"] not in edge_ids:
            edge_ids.add(ke["id"])
            edges_list.append(ke)

    # 7. Semantic & Structural Relationships
    # Task edges
    for task in tasks:
        tid = task.get("task_id") or "task"
        node = f"task:{tid}"
        target = task.get("target_node") or "amdy"
        if target:
            add_edge(node, ensure_hub("Agent", target), "executed_by")
        owner = str(task.get("task_type", "generic")).split(":", 1)[0]
        if owner:
            add_edge(node, ensure_hub("Owner", owner), "belongs_to")
        add_edge(node, ensure_hub("Domain", "System Logs, Tasks & Telemetry"), "in_domain")

    # Memory edges
    for mem in memories:
        uid = mem.get("uid") or "mem"
        node = f"memory:{uid}"
        src = str(mem.get("source") or "").split("/")[-1].lower()
        target_slug = page_by_source.get(src) if src else None
        if target_slug:
            add_edge(node, f"page:{target_slug}", "derived_from")
        cat = mem.get("category") or "general"
        if cat:
            add_edge(node, ensure_hub("Category", cat), "in_category")
        owner = mem.get("owner") or "unknown"
        if owner:
            add_edge(node, ensure_hub("Owner", owner), "authored_by")
        session = mem.get("session_id")
        if session:
            add_edge(node, ensure_hub("Session", session), "in_session")
        text = str(mem.get("text") or "").lower()
        for mname in model_names:
            if mname and mname in text:
                add_edge(node, f"model:{mname}", "about_model")
                break

    # Page edges
    for page in pages:
        slug = page.get("slug") or page.get("title") or "page"
        node = f"page:{slug}"
        cat = page.get("category") or "general"
        if cat:
            add_edge(node, ensure_hub("Category", cat), "in_category")
        owner = page.get("owner") or "unknown"
        if owner:
            add_edge(node, ensure_hub("Owner", owner), "authored_by")
        domain = classify_domain(cat, page.get("title") or "")
        if domain:
            add_edge(node, ensure_hub("Domain", domain), "in_domain")

    # Skill edges
    for skill in skills:
        sname = skill.get("name") or "skill"
        node = f"skill:{sname}"
        domain = classify_domain(sname, skill.get("description") or "")
        if domain:
            add_edge(node, ensure_hub("Domain", domain), "in_domain")
        add_edge(node, ensure_hub("Owner", "skills"), "authored_by")

    # Compute graph statistics
    nodes_final = list(nodes_map.values())
    node_types: dict[str, int] = {}
    for n in nodes_final:
        t = n.get("type", "unknown")
        node_types[t] = node_types.get(t, 0) + 1

    edge_types: dict[str, int] = {}
    for e in edges_list:
        et = e.get("type", "unknown")
        edge_types[et] = edge_types.get(et, 0) + 1

    node_count = len(nodes_final)
    edge_count = len(edges_list)
    density = round((2.0 * edge_count) / (node_count * (node_count - 1)), 4) if node_count > 1 else 0.0

    stats = {
        "node_count": node_count,
        "edge_count": edge_count,
        "node_types": node_types,
        "edge_types": edge_types,
        "density": density,
    }

    payload = {
        "degraded": False,
        "stats": stats,
        "graph": {
            "nodes": nodes_final,
            "edges": edges_list,
        },
        "built_at": now,
        "ttl": _GRAPH_TTL,
        "notes": {
            "pages": len(pages),
            "memories": len(memories),
            "skills": len(skills),
            "tasks": len(tasks),
            "models": len(models),
            "chunks": len(kuzu_nodes),
            "engine": "kuzu_native",
        },
    }
    _cache["at"] = now
    _cache["payload"] = payload
    return payload


def invalidate() -> None:
    _cache["at"] = 0.0
    _cache["payload"] = None
