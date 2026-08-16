import asyncio
import itertools
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from contextlib import asynccontextmanager
from typing import Any, Optional

import psutil
from fastapi import FastAPI, HTTPException, Query, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Add harness src to path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "src"))

from reins.harness.wiki import WikiDB, slugify  # noqa: E402
from reins.services.task_trail import TaskTrail  # noqa: E402
from reins.services.wiki_watcher import start_wiki_watcher, stop_wiki_watcher  # noqa: E402


@asynccontextmanager
async def lifespan(app: FastAPI):
    # PON-compliant reactive inotify wiki watcher
    start_wiki_watcher(debounce_seconds=2.0)
    yield
    stop_wiki_watcher()


app = FastAPI(title="SOFIA // KERNEL DASHBOARD", version="2.5.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

connected_clients: set[WebSocket] = set()


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    metadata: dict[str, str] = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            body = parts[2].strip()
            for line in fm_text.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    metadata[k.strip()] = v.strip().strip('"').strip("'")
    return metadata, body


# -----------------------------------------------------------------------------
# System & Telemetry
# -----------------------------------------------------------------------------


@app.get("/api/telemetry")
def get_telemetry() -> dict[str, Any]:
    try:
        cpu_percent = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage(str(ROOT_DIR))

        trail = TaskTrail()
        all_tasks = trail.all_tasks()
        task_counts = {
            "total": len(all_tasks),
            "success": 0,
            "failed": 0,
            "running": 0,
            "pending": 0,
        }
        for t in all_tasks:
            st = str(t.get("status", "pending")).lower()
            task_counts[st] = task_counts.get(st, 0) + 1

        with WikiDB() as db:
            wiki_stats = db.stats()
            wiki_cats = db.categories()
            model_mem_count = db.conn.execute(
                "SELECT COUNT(*) FROM memories WHERE category IN ('models', 'agents')"
            ).fetchone()[0]

        hw_file = ROOT_DIR / "knowledge_base" / "HARDWARE.md"
        hw_summary = hw_file.read_text() if hw_file.exists() else "No manifest found."

        from reins.services.token_ledger import TokenLedger

        ledger = TokenLedger()
        usage_24h = ledger.usage_in(24 * 3600)

        return {
            "system": {
                "cpu_percent": cpu_percent,
                "memory_used_gb": round((mem.total - mem.available) / (1024**3), 2),
                "memory_total_gb": round(mem.total / (1024**3), 2),
                "memory_percent": mem.percent,
                "disk_percent": disk.percent,
                "uptime_seconds": int(time.time() - psutil.boot_time()),
                "status": "SYS_OK",
                "timestamp": time.time(),
            },
            "tasks": task_counts,
            "recent_tasks": all_tasks[:30],
            "cloud_usage_24h": usage_24h,
            "wiki": {
                "pages": wiki_stats.get("pages", 0),
                "memories": wiki_stats.get("memories", 0),
                "model_memories": model_mem_count,
                "categories": wiki_cats,
            },
            "hardware": hw_summary,
        }
    except Exception as e:
        return {"error": str(e), "system": {"status": "SYS_DEGRADED"}}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        data = get_telemetry()
        await websocket.send_text(json.dumps(data))
        # PON: periodic push driven by a cooperative asyncio timer over an
        # infinite iterator — never an active-polling `while True` / sync sleep.
        for _ in itertools.count():
            await asyncio.sleep(1.5)
            data = get_telemetry()
            await websocket.send_text(json.dumps(data))
    except (WebSocketDisconnect, asyncio.CancelledError):
        connected_clients.discard(websocket)
    except Exception:
        connected_clients.discard(websocket)


# -----------------------------------------------------------------------------
# Model Memories & Personas Endpoints
# -----------------------------------------------------------------------------


@app.get("/api/model-memories")
def get_model_memories(category: Optional[str] = None, q: Optional[str] = None) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            query = "SELECT * FROM memories WHERE category IN ('models', 'agents')"
            params: list[Any] = []
            if category and category != "all":
                query = "SELECT * FROM memories WHERE category = ?"
                params = [category]

            if q:
                query += " AND (text LIKE ? OR owner LIKE ?)"
                like_q = f"%{q}%"
                params.extend([like_q, like_q])

            query += " ORDER BY timestamp DESC"
            rows = db.conn.execute(query, params).fetchall()
            return {"memories": [dict(r) for r in rows], "total": len(rows)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class ModelMemoryPayload(BaseModel):
    text: str
    category: str = "models"
    owner: str = "omnirouter"
    source: Optional[str] = "dashboard:manual_injection"


@app.post("/api/model-memories")
def inject_model_memory(payload: ModelMemoryPayload) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            uid = db.add_memory(
                text=payload.text,
                category=payload.category,
                owner=payload.owner,
                source=payload.source,
            )
            return {"status": "success", "uid": uid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------------------------------------------------------
# Task Trail Endpoints
# -----------------------------------------------------------------------------


@app.get("/api/tasks")
def get_all_tasks(status: Optional[str] = None, limit: int = 100) -> dict[str, Any]:
    try:
        trail = TaskTrail()
        tasks = trail.all_tasks()
        if status and status.lower() != "all":
            tasks = [t for t in tasks if str(t.get("status", "")).lower() == status.lower()]
        return {"tasks": tasks[:limit], "total": len(tasks)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/task/{task_id}")
def get_task_detail(task_id: str) -> dict[str, Any]:
    try:
        trail = TaskTrail()
        task = trail.get_task(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"task": task}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------------------------------------------------------
# Wiki DB Endpoints (CRUD)
# -----------------------------------------------------------------------------


@app.get("/api/wiki/stats")
def get_wiki_stats() -> dict[str, Any]:
    try:
        with WikiDB() as db:
            return {"stats": db.stats(), "categories": db.categories()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/wiki/search")
def search_wiki(q: str = Query(""), limit: int = Query(25)) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            res = db.search(q, limit=limit)
            return {
                "pages": [dict(r) for r in res.get("pages", [])],
                "memories": [dict(r) for r in res.get("memories", [])],
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/wiki/pages")
def list_wiki_pages(
    category: Optional[str] = None, limit: int = 50, offset: int = 0
) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            cat = category if category and category != "all" else None
            total = db.count_pages(category=cat)
            pages = db.list_pages(
                category=cat,
                limit=limit,
                offset=offset,
                order="recent",
            )
            return {"pages": [dict(p) for p in pages], "total": total}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/wiki/page/{slug}")
def get_wiki_page(slug: str) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            page = db.get_page(slug)
            if not page:
                raise HTTPException(status_code=404, detail="Page not found")
            return {"page": dict(page)}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class PagePayload(BaseModel):
    title: str
    content: str
    category: str = "general"
    slug: Optional[str] = None
    source_path: Optional[str] = None
    owner: str = "sofia-ui"
    metadata_json: str = "{}"


@app.post("/api/wiki/page")
@app.put("/api/wiki/page/{slug}")
def upsert_wiki_page(payload: PagePayload, slug: Optional[str] = None) -> dict[str, Any]:
    try:
        target_slug = slug or payload.slug or slugify(payload.title)
        with WikiDB() as db:
            saved_slug = db.upsert_page(
                title=payload.title,
                content=payload.content,
                slug=target_slug,
                category=payload.category,
                source_path=payload.source_path,
                owner=payload.owner,
                metadata_json=payload.metadata_json,
            )
            return {"status": "success", "slug": saved_slug}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/wiki/page/{slug}")
def delete_wiki_page(slug: str) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            cur = db.conn.execute("DELETE FROM pages WHERE slug = ?", (slug,))
            db.conn.commit()
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Page not found")
            return {"status": "deleted", "slug": slug}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/wiki/memories")
def list_wiki_memories(
    category: Optional[str] = None, q: Optional[str] = None, limit: int = 100, offset: int = 0
) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            query = "SELECT * FROM memories WHERE 1=1"
            params: list[Any] = []
            if category and category != "all":
                query += " AND category = ?"
                params.append(category)
            if q:
                query += " AND (text LIKE ? OR owner LIKE ? OR category LIKE ?)"
                like_q = f"%{q}%"
                params.extend([like_q, like_q, like_q])

            query += " ORDER BY timestamp DESC LIMIT ? OFFSET ?"
            params.extend([limit, offset])
            rows = db.conn.execute(query, params).fetchall()

            count_query = "SELECT COUNT(*) FROM memories WHERE 1=1"
            count_params: list[Any] = []
            if category and category != "all":
                count_query += " AND category = ?"
                count_params.append(category)
            if q:
                count_query += " AND (text LIKE ? OR owner LIKE ? OR category LIKE ?)"
                like_q = f"%{q}%"
                count_params.extend([like_q, like_q, like_q])

            total = db.conn.execute(count_query, count_params).fetchone()[0]
            return {"memories": [dict(r) for r in rows], "total": total}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class MemoryPayload(BaseModel):
    text: str
    category: str = "general"
    source: Optional[str] = None
    owner: str = "sofia-ui"


@app.post("/api/wiki/memory")
def add_wiki_memory(payload: MemoryPayload) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            uid = db.add_memory(
                text=payload.text,
                category=payload.category,
                source=payload.source,
                owner=payload.owner,
            )
            return {"status": "success", "uid": uid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/wiki/memory/{uid}")
def delete_wiki_memory(uid: str) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            cur = db.conn.execute("DELETE FROM memories WHERE uid = ?", (uid,))
            db.conn.commit()
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Memory not found")
            return {"status": "deleted", "uid": uid}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------------------------------------------------------
# Skills Endpoints (CRUD)
# -----------------------------------------------------------------------------


@app.get("/api/skills")
def list_skills() -> dict[str, Any]:
    try:
        skills_dir = ROOT_DIR / "skills"
        skills = []
        if skills_dir.exists():
            for d in sorted(skills_dir.iterdir()):
                if d.is_dir() and (d / "SKILL.md").exists():
                    skill_file = d / "SKILL.md"
                    raw_content = skill_file.read_text(encoding="utf-8", errors="replace")
                    meta, body = parse_frontmatter(raw_content)
                    skills.append(
                        {
                            "name": meta.get("name", d.name),
                            "slug": d.name,
                            "description": meta.get("description", "No description provided."),
                            "tags": meta.get("tags", ""),
                            "path": str(skill_file.relative_to(ROOT_DIR)),
                            "content": raw_content,
                            "body": body,
                        }
                    )
        return {"skills": skills, "total": len(skills)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/skill/{name}")
def get_skill_detail(name: str) -> dict[str, Any]:
    try:
        skill_file = ROOT_DIR / "skills" / name / "SKILL.md"
        if not skill_file.exists():
            raise HTTPException(status_code=404, detail="Skill not found")
        raw_content = skill_file.read_text(encoding="utf-8", errors="replace")
        meta, body = parse_frontmatter(raw_content)
        return {
            "name": meta.get("name", name),
            "slug": name,
            "description": meta.get("description", ""),
            "tags": meta.get("tags", ""),
            "content": raw_content,
            "body": body,
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SkillSavePayload(BaseModel):
    content: str


@app.put("/api/skill/{name}")
def save_skill(name: str, payload: SkillSavePayload) -> dict[str, Any]:
    try:
        skill_dir = ROOT_DIR / "skills" / name
        skill_dir.mkdir(parents=True, exist_ok=True)
        skill_file = skill_dir / "SKILL.md"
        skill_file.write_text(payload.content, encoding="utf-8")
        return {"status": "saved", "name": name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class NewSkillPayload(BaseModel):
    name: str
    description: str
    tags: str = "custom, harness"
    starter_content: str = ""


@app.post("/api/skill")
def create_skill(payload: NewSkillPayload) -> dict[str, Any]:
    try:
        slug = slugify(payload.name)
        skill_dir = ROOT_DIR / "skills" / slug
        if skill_dir.exists():
            raise HTTPException(status_code=400, detail="Skill already exists")
        skill_dir.mkdir(parents=True, exist_ok=True)
        content = f"""---
name: {slug}
description: "{payload.description}"
tags: "{payload.tags}"
---

# {payload.name}

{payload.starter_content or payload.description}
"""
        (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
        return {"status": "created", "name": slug}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------------------------------------------------------
# Models, Archetypes, Combos & Testbed
# -----------------------------------------------------------------------------


@app.get("/api/models")
def get_models_overview() -> dict[str, Any]:
    try:
        model_router_path = ROOT_DIR / "config" / "model_router.json"
        archetypes = {}
        if model_router_path.exists():
            with open(model_router_path, "r", encoding="utf-8") as f:
                mr = json.load(f)
                archetypes = mr.get("categories", {})

        omnirouter_path = ROOT_DIR / "config" / "omnirouter.json"
        combos = []
        if omnirouter_path.exists():
            with open(omnirouter_path, "r", encoding="utf-8") as f:
                om = json.load(f)
                combos = om.get("combos", [])

        safe_combos = []
        for c in combos:
            safe = dict(c)
            if safe.get("secret_key"):
                safe["secret_key"] = "•••••••• (" + str(safe["secret_key"]) + ")"
            safe_combos.append(safe)

        return {"archetypes": archetypes, "combos": safe_combos}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class TestPromptPayload(BaseModel):
    category: str = "rlm-worker-fast"
    prompt: str = "Hello, identify yourself and state your model configuration."


@app.post("/api/models/test-prompt")
def test_model_prompt(payload: TestPromptPayload) -> dict[str, Any]:
    try:
        start_t = time.time()
        cmd = ["reins", "run", payload.category, payload.prompt]
        res = subprocess.run(cmd, cwd=str(ROOT_DIR), capture_output=True, text=True, timeout=30)
        duration = round(time.time() - start_t, 3)
        return {
            "status": "success" if res.returncode == 0 else "error",
            "output": res.stdout or res.stderr,
            "exit_code": res.returncode,
            "duration_seconds": duration,
        }
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "output": "Model execution timed out after 30s."}
    except Exception as e:
        return {"status": "error", "output": str(e)}


# -----------------------------------------------------------------------------
# Harness System Controls
# -----------------------------------------------------------------------------


@app.post("/api/control/{action}")
def execute_harness_action(action: str) -> dict[str, Any]:
    try:
        if action == "consolidate":
            cmd = ["reins", "wiki", "consolidate"]
        elif action == "sync-skills":
            cmd = ["reins", "skills", "install"]
        elif action == "resilience-scan":
            cmd = ["reins", "trail", "list"]
        else:
            raise HTTPException(status_code=400, detail="Unknown action")

        res = subprocess.run(cmd, cwd=str(ROOT_DIR), capture_output=True, text=True, timeout=60)
        return {
            "action": action,
            "returncode": res.returncode,
            "stdout": res.stdout,
            "stderr": res.stderr,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------------------------------------------------------
# Static Files
# -----------------------------------------------------------------------------

app.mount(
    "/",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static"), html=True),
    name="static",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8088, reload=True)
