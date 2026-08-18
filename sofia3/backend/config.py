"""Sofia³ backend configuration.

Central, PON-flavoured settings for the greenfield SOFIA dashboard. The DB / Trail
stay the source of truth (reins); semantica is only a rendering/analytics layer.
"""

from __future__ import annotations

from pathlib import Path

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------
BACKEND_DIR = Path(__file__).resolve().parent
SOFIA3_DIR = BACKEND_DIR.parent
ROOT_DIR = SOFIA3_DIR.parent                       # data_rein/
VENV_PYTHON = ROOT_DIR / ".venv" / "bin" / "python"

# Frontend build output is served statically (mirrors semantica.explorer layout).
FRONTEND_DIST = SOFIA3_DIR / "frontend" / "dist"
STATIC_DIR = BACKEND_DIR / "static"

# Source-of-truth locations (harness).
WIKI_DB = ROOT_DIR / "knowledge_base" / "wiki.db"
THIRD_PARTY = ROOT_DIR / "third_party"
SRC = ROOT_DIR / "src"

# Universal Task Trail (harness source of truth for task state).
TRAIL_DB = Path.home() / ".config" / "data_nexus" / "task_trail.sqlite3"

# -----------------------------------------------------------------------------
# Server
# -----------------------------------------------------------------------------
HOST = "127.0.0.1"
PORT = 8088

# -----------------------------------------------------------------------------
# MQTT (event-driven task/trail push; zero polling)
# -----------------------------------------------------------------------------
MQTT_HOST = "localhost"
MQTT_PORT = 1883
TRAIL_TOPICS = (
    "data_rein/trail/#",
    "data_rein/getinfo/#",
    "data_rein/coord/#",
    "data_rein/models/#",
    "data_rein/tokens/#",
    "data_rein/pon/#",
)

# WebSocket origin guard: only the served origin may connect (semantica pattern).
ALLOWED_ORIGINS = (f"http://{HOST}:{PORT}", f"http://localhost:{PORT}")