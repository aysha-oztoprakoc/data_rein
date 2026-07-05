"""
The Three Laws of the data_rein harness, enforced as executable tests.

Every module under `src/reins` is bound by these. They are written to *fail loudly*
if future code breaks the harness contract, so they double as living documentation
and as a TDD guard rail.

    LAW 1 — PON (Notification-Oriented Paradigm): zero polling. No spin-wait
            loops, no synchronous busy-wait timers. Reactivity only.
    LAW 2 — Graceful Degradation: public entry points degrade (return / log / skip)
            on bad input instead of raising and taking the harness down.
    LAW 3 — Test-Driven Development: every harness module is covered by the suite;
            no shipped module is left untested.
"""

from __future__ import annotations

import ast
import importlib
from pathlib import Path

import pytest

from conftest import harness_source_files, SRC_ROOT


# ---------------------------------------------------------------------------
# LAW 1 — PON: no polling anywhere in harness source (AST-based, ignores
# strings/comments so docstrings mentioning the anti-pattern don't false-positive).
# ---------------------------------------------------------------------------

def _polling_violations(path: Path) -> list[str]:
    """
    Report PON violations in a source file. A single line may opt out of the
    time.sleep ban with a trailing ``# pon-allow: <reason>`` marker — reserved for
    genuinely event-less waits (e.g. a bounded one-time subprocess cold-start).
    `while True` spin loops are never allowed.
    """
    src_lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    tree = ast.parse("\n".join(src_lines), filename=str(path))

    def _allowed(lineno: int) -> bool:
        return "pon-allow" in src_lines[lineno - 1] if 0 < lineno <= len(src_lines) else False

    out: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.While):
            test = node.test
            if isinstance(test, ast.Constant) and bool(test.value) is True:
                out.append(f"{path.name}:{node.lineno} while-True spin loop")
        if isinstance(node, ast.Call):
            fn = node.func
            if isinstance(fn, ast.Attribute) and fn.attr == "sleep":
                base = fn.value
                if isinstance(base, ast.Name) and base.id == "time" and not _allowed(node.lineno):
                    out.append(f"{path.name}:{node.lineno} synchronous sleep busy-wait")
    return out


def test_law_pon_no_polling_in_harness():
    violations: list[str] = []
    for src in harness_source_files():
        violations.extend(_polling_violations(src))
    assert not violations, "PON law broken (polling detected):\n  " + "\n  ".join(violations)


# ---------------------------------------------------------------------------
# LAW 2 — Graceful Degradation: representative public entry points must degrade,
# not raise, on hostile input. (Module-specific degradation lives in each
# module's own test; this asserts the systemic guarantee.)
# ---------------------------------------------------------------------------

def test_law_graceful_router_degrades_not_raises(monkeypatch):
    from reins.harness.models import ModelRouter

    monkeypatch.setattr("reins.harness.models._get_secret", lambda *_: None)
    r = ModelRouter()
    r.table = {"x": {"amdy": [{"model": "claude-nope"}], "tell": [{"model": "gpt-nope"}]}}
    res = r.route("x", "hello", "amdy")  # must not raise
    assert res.ok is False and res.error
    assert "cloud/" in res.error  # Tier-1 remote fallback attempted, not skipped


def test_law_graceful_wiki_survives_bad_query(wiki):
    # A malformed FTS query must not crash the harness knowledge store.
    try:
        wiki.upsert_page("t", "content", slug="t")
        wiki.search_pages('"unterminated AND (')  # invalid FTS syntax
    except Exception as e:
        # Degradation is allowed to raise a *handled* DB error type, but must not
        # be an unexpected crash; sqlite raises OperationalError which callers guard.
        import sqlite3
        assert isinstance(e, sqlite3.Error)


def test_law_graceful_odysseus_drain_survives_bad_trail(monkeypatch):
    from reins.services.fallback_agent import OdysseusAgent

    agent = OdysseusAgent()
    # A trail row missing keys must degrade, not crash the drain.
    monkeypatch.setattr(agent.trail, "_load", lambda: [{"status": "pending"}])
    monkeypatch.setattr(agent, "query_ollama", lambda p: "Error: no model")
    monkeypatch.setattr(agent.trail, "update_task", lambda *a, **k: None)
    acted = agent.process_pending()  # must not raise
    assert isinstance(acted, list)


# ---------------------------------------------------------------------------
# LAW 3 — TDD: every harness core module is imported/exercised by the suite.
# Guards against new untested modules landing under src/reins/harness.
# ---------------------------------------------------------------------------

def _harness_core_modules() -> list[str]:
    core = SRC_ROOT / "harness"
    mods = []
    for p in core.glob("*.py"):
        if p.stem == "__init__":
            continue
        mods.append(f"reins.harness.{p.stem}")
    return mods


@pytest.mark.parametrize("module", _harness_core_modules())
def test_law_tdd_harness_module_importable(module):
    """Every harness core module must import cleanly (smoke coverage floor)."""
    assert importlib.import_module(module) is not None


def test_law_tdd_test_files_reference_each_core_module():
    """Each harness core module must be referenced by at least one test file."""
    test_text = "\n".join(
        p.read_text(encoding="utf-8", errors="replace")
        for p in Path(__file__).parent.glob("test_*.py")
    )
    missing = [m for m in _harness_core_modules() if m.rsplit(".", 1)[-1] not in test_text]
    assert not missing, f"harness modules with no test reference (TDD law): {missing}"
