"""Sofia³ — greenfield SOFIA dashboard (FastAPI backend).

Replaces `dashboard/app.py`. Source of truth stays with reins (wiki + trail);
semantica is only a rendering/analytics layer (see `third_party/semantica/`).

PON compliance:
  * zero polling — live task data is pushed by inotify (trail DB) and MQTT
    events through `LiveBridge`; the wiki is consolidated by the reins
    `wiki_watcher` on file events;
  * graceful degradation — broker/DB/semantica absence degrades, never crashes.
"""

from __future__ import annotations

import logging
import os
import sys
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Import harness + vendored semantica off the project root (dashboard pattern).
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(ROOT_DIR / "src"))
sys.path.insert(0, str(ROOT_DIR / "third_party"))

from reins.services.wiki_watcher import start_wiki_watcher, stop_wiki_watcher  # noqa: E402

from sofia3.backend import config  # noqa: E402
from sofia3.backend.live import LiveBridge  # noqa: E402
from sofia3.backend.routers import graph, system, tasks, wiki  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger("sofia3")

bridge = LiveBridge()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Start event-driven watchers; stop them cleanly on shutdown."""
    logger.info("Sofia³ startup — binding %s:%s", config.HOST, config.PORT)
    try:
        start_wiki_watcher(debounce_seconds=2.0)
        logger.info("Wiki inotify watcher started")
    except Exception as exc:
        logger.warning("Wiki watcher unavailable: %s", exc)
    bridge.start()
    yield
    await bridge.stop()
    stop_wiki_watcher()
    logger.info("Sofia³ shutdown complete")


app = FastAPI(title="SOFIA³ // KERNEL DASHBOARD", version="3.0.0", lifespan=lifespan)

dev_origin = os.getenv("DEV_ORIGIN", "http://localhost:5173")
_allowed_origins = set(config.ALLOWED_ORIGINS)
if dev_origin:
    _allowed_origins.add(dev_origin)

app.add_middleware(
    CORSMiddleware,
    allow_origins=list(_allowed_origins),
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(tasks.router)
app.include_router(wiki.router)
app.include_router(graph.router)
app.include_router(system.router)


@app.get("/api/health")
def health() -> dict[str, Any]:
    """Liveness + basic connectivity probe."""
    return {
        "status": "SYS_OK",
        "service": "sofia3",
        "version": "3.0.0",
        "trail_db": str(Path(config.TRAIL_DB).resolve()),
        "degraded": False,
    }


def _origin_allowed(origin: str | None) -> bool:
    if not origin:
        return False
    dev_origin = os.getenv("DEV_ORIGIN", "http://localhost:5173")
    return (
        origin in config.ALLOWED_ORIGINS
        or origin == dev_origin
        or origin.startswith("http://127.0.0.1:")
    )


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    """Live task stream. Origin-guarded (semantica explorer pattern)."""
    if not _origin_allowed(websocket.headers.get("origin")):
        await websocket.close(code=4403)
        return
    await websocket.accept()
    try:
        async for payload in bridge.subscribe():
            await websocket.send_json(payload)
    except WebSocketDisconnect:
        pass
    except Exception as exc:
        logger.warning("WS client error: %s", exc)


# -----------------------------------------------------------------------------
# Static frontend (built Vite output; dev servers use their own Vite).
# -----------------------------------------------------------------------------
_DIST = config.FRONTEND_DIST


def _mount_frontend(app: FastAPI, dist: Path) -> None:
    if not dist.exists():
        logger.warning("Frontend dist not built (%s) — API-only mode", dist)
        return
    assets = dist / "assets"
    if assets.exists():
        app.mount("/assets", StaticFiles(directory=str(assets)), name="assets")

    @app.get("/{full_path:path}", include_in_schema=False)
    async def spa(full_path: str):
        candidate = (dist / full_path).resolve() if full_path else None
        if candidate and candidate.is_file() and dist in candidate.parents:
            return FileResponse(str(candidate))
        index = dist / "index.html"
        if index.is_file():
            return FileResponse(str(index))
        return {"detail": "frontend not built"}, 404


_mount_frontend(app, _DIST)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=config.HOST, port=config.PORT, reload=False)