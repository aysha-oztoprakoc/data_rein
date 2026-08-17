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
    try:
        with WikiDB() as db:
            res = db.search(q, limit=limit)
            return {
                "pages": [dict(r) for r in res.get("pages", [])],
                "memories": [dict(r) for r in res.get("memories", [])],
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
            if not page:
                raise HTTPException(status_code=404, detail="Page not found")
            return {"page": dict(page)}
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