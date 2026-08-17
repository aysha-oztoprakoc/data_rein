"""Graph endpoints — unified knowledge graph (SOFIA³ Graph view).

Built through the vendored semantica ContextGraph (see graph_bridge.py).
Reactive invalidation: on trail/wiki change signals the bridge TTL cache is
busted so the next /api/graph call rebuilds on demand.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException

from sofia3.backend import graph_bridge

router = APIRouter(prefix="/api/graph", tags=["graph"])


@router.get("")
def graph_snapshot() -> dict[str, Any]:
    """Return the unified graph snapshot (nodes + edges + stats)."""
    payload = graph_bridge.build_graph()
    if payload.get("degraded"):
        raise HTTPException(
            status_code=503,
            detail={
                "degraded": True,
                "error": payload.get("error", "graph bridge unavailable"),
                "hint": "Install vendored semantica: see third_party/semantica/README.md",
            },
        )
    return payload


@router.get("/stats")
def graph_stats() -> dict[str, Any]:
    """Graph-level statistics (node/edge type distributions)."""
    payload = graph_bridge.build_graph()
    if payload.get("degraded"):
        raise HTTPException(status_code=503, detail={"degraded": True})
    return {"stats": payload.get("stats", {}), "notes": payload.get("notes", {})}


@router.post("/invalidate")
def invalidate_graph() -> dict[str, Any]:
    """Bust the graph TTL cache (called internally on trail/wiki events)."""
    graph_bridge.invalidate()
    return {"status": "invalidated"}
