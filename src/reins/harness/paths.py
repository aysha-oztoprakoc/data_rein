"""
Canonical path resolution for the data_rein universal harness.

Every environment (Antigravity, Hermes, Odysseus, Claude Code, VS Code) resolves
the *same* locations through this module, so there is exactly one source of truth
regardless of which agent or machine is running.

Resolution order for the harness home:
    1. ``$DATA_REIN_HOME`` if set.
    2. The repository root inferred from this file's location.
    3. ``~/data_rein`` as a last resort.

Individual artifacts can be overridden with environment variables
(``$DATA_REIN_WIKI_DB``, ``$DATA_REIN_CONFIG_DIR``, ...) which lets the two
nodes (amdy / tell) point at node-local storage without any code change.
"""

from __future__ import annotations

import os
from pathlib import Path


def _infer_repo_root() -> Path:
    # src/reins/harness/paths.py -> repo root is 4 parents up.
    return Path(__file__).resolve().parents[3]


def home() -> Path:
    """Return the canonical harness home directory."""
    env = os.environ.get("DATA_REIN_HOME")
    if env:
        return Path(env).expanduser().resolve()

    inferred = _infer_repo_root()
    if (inferred / "knowledge_base").is_dir():
        return inferred

    return Path("~/data_rein").expanduser().resolve()


def _resolve(env_var: str, *relative: str) -> Path:
    override = os.environ.get(env_var)
    if override:
        return Path(override).expanduser().resolve()
    return home().joinpath(*relative)


# --- Canonical artifacts ---------------------------------------------------

def knowledge_base() -> Path:
    return _resolve("DATA_REIN_KB", "knowledge_base")


def prime_directive() -> Path:
    """The single master constitution loaded by every environment."""
    return _resolve("DATA_REIN_PRIME_DIRECTIVE", "knowledge_base", "PRIME_DIRECTIVE.md")


def aesthetic_directive() -> Path:
    return _resolve("DATA_REIN_AESTHETIC", "knowledge_base", "AESTHETIC_DIRECTIVE.md")


def shared_context() -> Path:
    return _resolve("DATA_REIN_SHARED_CONTEXT", "knowledge_base", "SHARED_CONTEXT.md")


def hardware_manifest() -> Path:
    """Canonical, live-refreshed hardware manifest (written by the getinfo scan)."""
    return _resolve("DATA_REIN_HARDWARE", "knowledge_base", "HARDWARE.md")


def wiki_db() -> Path:
    """The single shared monolith Wiki database (derived, rebuildable)."""
    return _resolve("DATA_REIN_WIKI_DB", "knowledge_base", "wiki.db")


def config_dir() -> Path:
    return _resolve("DATA_REIN_CONFIG_DIR", "config")


def model_router() -> Path:
    return config_dir() / "model_router.json"


def model_registry() -> Path:
    return config_dir() / "model_registry.json"


def backup_config() -> Path:
    """Config for the backup + shutdown-guard system (reins.services.backup)."""
    return config_dir() / "backup_config.json"


def obsidian_vault() -> Path:
    """The human-facing 'oby' Obsidian vault."""
    return _resolve("DATA_REIN_OBY", "data-oby")


def agy_brain_dir() -> Path:
    """Where Antigravity (data-agy) stores conversation brain artifacts (task.md)."""
    override = os.environ.get("DATA_REIN_AGY_BRAIN")
    if override:
        return Path(override).expanduser()
    return Path("~/.gemini/antigravity-cli/brain").expanduser()


def state_dir() -> Path:
    """Per-user runtime state (task trail, router state)."""
    override = os.environ.get("DATA_REIN_STATE_DIR")
    if override:
        return Path(override).expanduser().resolve()
    return Path("~/.config/data_nexus").expanduser()


def task_trail() -> Path:
    return state_dir() / "task_trail.json"


def token_usage() -> Path:
    """Self-tracked cloud-provider token/request usage ledger (see token_ledger.py)."""
    return state_dir() / "token_usage.json"


def token_budgets() -> Path:
    """User-editable known plan limits (5h/day/week/month) per cloud provider."""
    return config_dir() / "token_budgets.json"


def agent_budgets() -> Path:
    """Per-agent CPU cgroup quota / soft GPU-VRAM allocation (see resource_budgets.py)."""
    return config_dir() / "agent_budgets.json"


def ensure_state_dir() -> Path:
    d = state_dir()
    d.mkdir(parents=True, exist_ok=True)
    return d


def summary() -> dict[str, str]:
    """A flat dict of every canonical path - handy for CLI/diagnostics."""
    return {
        "home": str(home()),
        "knowledge_base": str(knowledge_base()),
        "prime_directive": str(prime_directive()),
        "aesthetic_directive": str(aesthetic_directive()),
        "shared_context": str(shared_context()),
        "hardware_manifest": str(hardware_manifest()),
        "wiki_db": str(wiki_db()),
        "config_dir": str(config_dir()),
        "model_router": str(model_router()),
        "obsidian_vault": str(obsidian_vault()),
        "task_trail": str(task_trail()),
        "token_usage": str(token_usage()),
        "token_budgets": str(token_budgets()),
        "agent_budgets": str(agent_budgets()),
    }
