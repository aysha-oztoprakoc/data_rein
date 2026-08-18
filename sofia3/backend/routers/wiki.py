"""Read-only Wiki endpoints (SOFIA³ Wiki view).

Source of truth: `knowledge_base/wiki.db` (monolith, single store). Read-only —
the wiki is written by agents via reins CLI/MCP, never by the dashboard.
"""

from __future__ import annotations

from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Query

from reins.harness.wiki import WikiDB

router = APIRouter(prefix="/api/wiki", tags=["wiki"])


@router.get("/stats")
def wiki_stats() -> dict[str, Any]:
    try:
        with WikiDB() as db:
            return {"stats": db.stats(), "categories": db.categories()}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/search")
def wiki_search(q: str = Query(""), limit: int = Query(25, ge=1, le=100)) -> dict[str, Any]:
    if not q.strip():
        return {"pages": [], "memories": [], "chunks": []}
    try:
        from reins.harness import paths
        from reins.harness.embeddings import EmbeddingClient
        import chromadb

        pages_map: dict[str, dict[str, Any]] = {}
        memories_map: dict[str, dict[str, Any]] = {}
        chunks_list: list[dict[str, Any]] = []

        # 1. Semantic search over ChromaDB chunks
        try:
            chroma_dir = paths.chroma_db_dir()
            if chroma_dir.exists():
                client = chromadb.PersistentClient(path=str(chroma_dir))
                coll = client.get_or_create_collection(name="wiki_chunks", metadata={"hnsw:space": "cosine"})
                count = coll.count()
                if count > 0:
                    embedder = EmbeddingClient()
                    q_vec = embedder.embed_text(q)
                    results = coll.query(query_embeddings=[q_vec], n_results=min(limit, count))
                    if results and results.get("ids") and results["ids"][0]:
                        ids = results["ids"][0]
                        docs = results.get("documents", [[]])[0]
                        metas = results.get("metadatas", [[]])[0]
                        distances = results.get("distances", [[]])[0]

                        with WikiDB() as db:
                            for idx, cid in enumerate(ids):
                                doc = docs[idx] if idx < len(docs) else ""
                                meta = metas[idx] if idx < len(metas) else {}
                                dist = distances[idx] if idx < len(distances) else 0.0
                                sim = round(1.0 - dist, 4)
                                source_id = meta.get("source_id", "") if isinstance(meta, dict) else ""
                                source_type = meta.get("source_type", "") if isinstance(meta, dict) else ""
                                section = meta.get("section", "") if isinstance(meta, dict) else ""

                                chunks_list.append({
                                    "id": cid,
                                    "content": doc,
                                    "section": section,
                                    "source_id": source_id,
                                    "source_type": source_type,
                                    "similarity": sim,
                                })

                                if source_type == "page" and source_id and source_id not in pages_map:
                                    p = db.get_page(source_id)
                                    if p:
                                        pages_map[source_id] = dict(p)
                                elif source_type == "memory" and source_id and source_id not in memories_map:
                                    row = db.conn.execute("SELECT * FROM memories WHERE uid = ?", (source_id,)).fetchone()
                                    if row:
                                        memories_map[source_id] = dict(row)
        except Exception:
            pass

        # 2. Text search fallback / blend from SQLite WikiDB
        with WikiDB() as db:
            res = db.search(q, limit=limit)
            for p in res.get("pages", []):
                p_dict = dict(p)
                slug = p_dict.get("slug") or p_dict.get("title")
                if slug and slug not in pages_map:
                    pages_map[slug] = p_dict
            for m in res.get("memories", []):
                m_dict = dict(m)
                uid = m_dict.get("uid")
                if uid and uid not in memories_map:
                    memories_map[uid] = m_dict

        return {
            "pages": list(pages_map.values()),
            "memories": list(memories_map.values()),
            "chunks": chunks_list,
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/pages")
def list_pages(
    category: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            cat = category if category and category != "all" else None
            total = db.count_pages(category=cat)
            pages = db.list_pages(category=cat, limit=limit, offset=offset, order="recent")
            return {"pages": [dict(p) for p in pages], "total": total}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/page/{slug}")
def get_page(slug: str) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            page = db.get_page(slug)
            if not page or dict(page).get("is_deleted", 0) == 1:
                raise HTTPException(status_code=404, detail="Page not found")
            return {"page": dict(page)}
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

from pydantic import BaseModel
class PageUpdate(BaseModel):
    category: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None

@router.patch("/page/{slug}")
def update_page(slug: str, updates: PageUpdate) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            page = db.get_page(slug)
            if not page or dict(page).get("is_deleted", 0) == 1:
                raise HTTPException(status_code=404, detail="Page not found")
            
            pdict = dict(page)
            db.upsert_page(
                title=updates.title if updates.title is not None else pdict["title"],
                content=updates.content if updates.content is not None else pdict["content"],
                slug=slug,
                category=updates.category if updates.category is not None else pdict["category"],
                source_path=pdict.get("source_path"),
                fmt=pdict.get("fmt", "md"),
                metadata_json=pdict.get("metadata_json", "{}"),
                owner="dashboard_user",
                trust_score=pdict.get("trust_score", 1.0)
            )
            return {"status": "updated"}
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@router.delete("/page/{slug}")
def delete_page(slug: str) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            page = db.get_page(slug)
            if not page or dict(page).get("is_deleted", 0) == 1:
                raise HTTPException(status_code=404, detail="Page not found or already deleted")
            
            pdict = dict(page)
            cat = (pdict.get("category") or "").strip().lower()
            if cat in ("sys", "core"):
                raise HTTPException(
                    status_code=403,
                    detail="Deletion of core system pages is prohibited via the dashboard.",
                )

            if db.soft_delete_page(slug, owner="dashboard_user"):
                return {"status": "deleted"}
            raise HTTPException(status_code=404, detail="Page not found or already deleted")
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/memory/{uid}")
def get_memory(uid: str) -> dict[str, Any]:
    """Fetch one full memory record by uid (Ticket 2: graph click detail)."""
    try:
        with WikiDB() as db:
            row = db.conn.execute(
                "SELECT * FROM memories WHERE uid = ?", (uid,)
            ).fetchone()
            if not row or dict(row).get("is_deleted", 0) == 1:
                raise HTTPException(status_code=404, detail="Memory not found")
            return {"memory": dict(row)}
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

class MemoryUpdate(BaseModel):
    category: Optional[str] = None
    text: Optional[str] = None

@router.patch("/memory/{uid}")
def update_memory(uid: str, updates: MemoryUpdate) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            row = db.conn.execute("SELECT * FROM memories WHERE uid = ?", (uid,)).fetchone()
            if not row or dict(row).get("is_deleted", 0) == 1:
                raise HTTPException(status_code=404, detail="Memory not found")
            
            mdict = dict(row)
            db.add_memory(
                text=updates.text if updates.text is not None else mdict["text"],
                category=updates.category if updates.category is not None else mdict["category"],
                source=mdict.get("source"),
                owner="dashboard_user",
                session_id=mdict.get("session_id"),
                uid=uid,
                trust_score=mdict.get("trust_score", 1.0)
            )
            return {"status": "updated"}
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@router.delete("/memory/{uid}")
def delete_memory(uid: str) -> dict[str, Any]:
    try:
        with WikiDB() as db:
            row = db.conn.execute("SELECT * FROM memories WHERE uid = ?", (uid,)).fetchone()
            if not row or dict(row).get("is_deleted", 0) == 1:
                raise HTTPException(status_code=404, detail="Memory not found or already deleted")
            
            mdict = dict(row)
            cat = (mdict.get("category") or "").strip().lower()
            if cat in ("sys", "core"):
                raise HTTPException(
                    status_code=403,
                    detail="Deletion of core system memories is prohibited via the dashboard.",
                )

            if db.soft_delete_memory(uid, owner="dashboard_user"):
                return {"status": "deleted"}
            raise HTTPException(status_code=404, detail="Memory not found or already deleted")
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/memories")
def list_memories(
    category: Optional[str] = Query(None),
    q: Optional[str] = Query(None),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
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
                like = f"%{q}%"
                params.extend([like, like, like])
            query += " ORDER BY timestamp DESC LIMIT ? OFFSET ?"
            params.extend([limit, offset])
            rows = db.conn.execute(query, params).fetchall()
            count = db.conn.execute(
                "SELECT COUNT(*) FROM memories WHERE 1=1"
                + (" AND category = ?" if category and category != "all" else "")
                + (" AND (text LIKE ? OR owner LIKE ? OR category LIKE ?)" if q else ""),
                [p for p in params[:3] if not isinstance(p, int)] or [],
            ).fetchone()[0]
            return {"memories": [dict(r) for r in rows], "total": count}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/skills")
def list_skills() -> dict[str, Any]:
    """List all canonical skills categorized by domain, origin, and date."""
    try:
        import time
        from reins.harness.skill_registry import canonical_skills
        from sofia3.backend.graph_bridge import classify_domain

        skills = canonical_skills()
        results = []
        for s in skills:
            mtime = s.path.stat().st_mtime if s.path.exists() else 0
            date_str = time.strftime("%Y-%m-%d", time.gmtime(mtime)) if mtime else ""
            domain = classify_domain(s.name, s.description)
            results.append(
                {
                    "name": s.name,
                    "description": s.description,
                    "domain": domain,
                    "origin": "skills",
                    "path": str(s.path),
                    "date": date_str,
                    "timestamp": mtime,
                }
            )
        return {"skills": results, "total": len(results)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/catalog")
def wiki_catalog() -> dict[str, Any]:
    """Return unified catalog grouped by origin, content domain, and date."""
    try:
        import time
        from reins.harness.skill_registry import canonical_skills
        from sofia3.backend.graph_bridge import classify_domain

        def format_date(val: Any) -> str:
            if not val:
                return "2026-08-17"
            if isinstance(val, (int, float)):
                ts = float(val)
                if ts > 1e11:
                    ts /= 1000.0
                return time.strftime("%Y-%m-%d", time.gmtime(ts))
            s = str(val).strip()
            if s.isdigit() or (s.replace(".", "", 1).isdigit() and len(s) >= 9):
                ts = float(s)
                if ts > 1e11:
                    ts /= 1000.0
                return time.strftime("%Y-%m-%d", time.gmtime(ts))
            if len(s) >= 10 and s[4] == "-" and s[7] == "-":
                return s[:10]
            return "2026-08-17"

        by_origin: dict[str, list[dict[str, Any]]] = {}
        by_domain: dict[str, list[dict[str, Any]]] = {}
        by_date: dict[str, list[dict[str, Any]]] = {}

        def record(item: dict[str, Any], origin: str, domain: str, raw_date: Any) -> None:
            date_str = format_date(raw_date)
            period = date_str[:7] if len(date_str) >= 7 else "historical"
            item["date"] = date_str
            item["period"] = period
            by_origin.setdefault(origin, []).append(item)
            by_domain.setdefault(domain, []).append(item)
            by_date.setdefault(period, []).append(item)

        # 1. Skills
        for s in canonical_skills():
            mtime = s.path.stat().st_mtime if s.path.exists() else 0
            domain = classify_domain(s.name, s.description)
            item = {
                "type": "Skill",
                "id": s.name,
                "title": s.name,
                "description": s.description,
                "origin": "skills",
                "domain": domain,
            }
            record(item, "skills", domain, mtime)

        # 2. Pages & Memories from WikiDB
        with WikiDB() as db:
            pages = db.list_pages(limit=5000, offset=0, order="recent")
            for p in pages:
                p_dict = dict(p)
                cat = p_dict.get("category") or "general"
                domain = classify_domain(cat, p_dict.get("title") or "")
                origin = p_dict.get("owner") or "knowledge_base"
                item = {
                    "type": "Page",
                    "id": p_dict.get("slug") or p_dict.get("title"),
                    "title": p_dict.get("title"),
                    "category": cat,
                    "origin": origin,
                    "domain": domain,
                }
                record(item, origin, domain, p_dict.get("updated_at") or p_dict.get("created_at"))

            memories = db.conn.execute(
                "SELECT uid, text, category, owner, timestamp FROM memories ORDER BY timestamp DESC"
            ).fetchall()
            for m in memories:
                m_dict = dict(m)
                cat = m_dict.get("category") or "general"
                domain = classify_domain(cat, str(m_dict.get("text") or ""))
                origin = m_dict.get("owner") or "memory"
                item = {
                    "type": "Memory",
                    "id": m_dict.get("uid"),
                    "title": str(m_dict.get("text") or "")[:80],
                    "category": cat,
                    "origin": origin,
                    "domain": domain,
                }
                record(item, origin, domain, m_dict.get("timestamp"))

        return {
            "by_origin": {k: len(v) for k, v in sorted(by_origin.items())},
            "by_domain": {k: len(v) for k, v in sorted(by_domain.items())},
            "by_date": {k: len(v) for k, v in sorted(by_date.items(), reverse=True)},
            "details": {
                "origins": by_origin,
                "domains": by_domain,
                "dates": by_date,
            },
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))