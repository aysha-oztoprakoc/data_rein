from __future__ import annotations

import ast
import importlib
import sqlite3
from pathlib import Path

import pytest

from conftest import harness_source_files, SRC_ROOT


# ---------------------------------------------------------------------------
# LAW 1 — PON: no polling anywhere in harness source (AST-based, ignores
# strings/comments so docstrings mentioning the anti-pattern don't false-positive).
# ---------------------------------------------------------------------------


def _call_names(node: ast.AST) -> set[str]:
    names: set[str] = set()
    for child in ast.walk(node):
        if not isinstance(child, ast.Call):
            continue
        function = child.func
        if isinstance(function, ast.Name):
            names.add(function.id)
        if isinstance(function, ast.Attribute):
            names.add(function.attr)
    return names


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
            condition_calls = _call_names(node.test)
            body_calls = set().union(*(_call_names(statement) for statement in node.body))
            blocking_calls = {"read", "read_frame", "recv", "select"}
            test = node.test
            if isinstance(test, ast.Constant) and bool(test.value) is True:
                out.append(f"{path.name}:{node.lineno} while-True spin loop")
            elif condition_calls and not (condition_calls | body_calls).intersection(blocking_calls):
                out.append(f"{path.name}:{node.lineno} status/deadline polling loop")
        if isinstance(node, ast.Call):
            fn = node.func
            if (
                isinstance(fn, ast.Attribute)
                and fn.attr in {"sleep", "wait_for_timeout"}
                and not _allowed(node.lineno)
            ):
                out.append(f"{path.name}:{node.lineno} time-based polling wait")
    return out


def test_law_pon_no_polling_in_harness():
    violations: list[str] = []
    for src in harness_source_files():
        violations.extend(_polling_violations(src))
    assert not violations, "PON law broken (polling detected):\n  " + "\n  ".join(violations)


def test_law_pon_no_periodic_timers_in_active_scripts() -> None:
    # Given active service scripts are part of the event-driven harness surface.
    violations: list[str] = []

    # When their syntax trees are checked for timer-based state refresh.
    for path in (SRC_ROOT.parents[1] / "scripts").glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"), filename=str(path))
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "set_interval"
            ):
                violations.append(f"{path.name}:{node.lineno} periodic timer")

    # Then no service rechecks state on an elapsed-time schedule.
    assert not violations, "PON-1 broken in active scripts:\n  " + "\n  ".join(violations)


def test_single_wiki_active_scripts_do_not_write_legacy_database() -> None:
    # Given wiki.db is the sole writable knowledge store.
    violations: list[str] = []

    # When active scripts are inspected for direct legacy app.db connections.
    for path in (SRC_ROOT.parents[1] / "scripts").glob("*.py"):
        if path.name == "consolidate_wiki.py":
            continue
        source = path.read_text(encoding="utf-8", errors="replace")
        if "app.db" in source and "sqlite3.connect" in source:
            violations.append(path.name)

    # Then legacy databases remain read-only migration inputs, never writers.
    assert not violations, "single-wiki law broken: " + ", ".join(violations)


def test_law_gd_external_io_uses_circuit_breaker_adapter() -> None:
    # Given external transport calls can repeatedly fail and exhaust the harness.
    violations: list[str] = []
    roots = [SRC_ROOT, SRC_ROOT.parents[1] / "scripts"]

    # When active Python syntax is inspected for calls that bypass external_io.
    for root in roots:
        for path in root.rglob("*.py"):
            if "legacy" in path.parts or path.name in {"external_io.py", "consolidate_wiki.py"}:
                continue
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"), filename=str(path))
            parents = {
                child: parent for parent in ast.walk(tree) for child in ast.iter_child_nodes(parent)
            }
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                    continue
                owner = ast.unparse(node.func.value)
                call = node.func.attr
                raw_process = owner == "subprocess" and call in {
                    "run",
                    "Popen",
                    "check_call",
                    "check_output",
                }
                raw_url = owner == "urllib.request" and call == "urlopen"
                raw_socket = owner in {"socket", "sock"} and call in {
                    "connect",
                    "create_connection",
                }
                raw_browser = call in {"goto", "launch"} and owner in {"page", "p.chromium"}
                raw_search = call == "text" and owner.endswith(".ddgs")
                raw_mqtt = call in {"publish", "single", "subscribe"} or (
                    call == "connect"
                    and any(token in owner.lower() for token in ("mqtt", "client", " c"))
                )
                ancestor = parents.get(node)
                admitted = False
                while ancestor is not None:
                    if (
                        isinstance(ancestor, ast.Call)
                        and isinstance(ancestor.func, ast.Attribute)
                        and ast.unparse(ancestor.func.value) == "external_io"
                        and ancestor.func.attr == "call"
                    ):
                        admitted = True
                        break
                    ancestor = parents.get(ancestor)
                if (
                    raw_process or raw_url or raw_socket or raw_browser or raw_search or raw_mqtt
                ) and not admitted:
                    violations.append(
                        f"{path.relative_to(SRC_ROOT.parents[1])}:{node.lineno} {owner}.{call}"
                    )

    # Then every matching external call is admitted and observed by one breaker adapter.
    assert not violations, "GD-1 raw external calls:\n  " + "\n  ".join(violations)


def test_law_pon_no_reach_through() -> None:
    violations: list[str] = []
    for path in harness_source_files():
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                continue
            if node.func.attr == "__new__":
                violations.append(f"{path.name}:{node.lineno} internal __new__ reach-through")
    assert not violations, "PON-2 broken:\n  " + "\n  ".join(violations)


def _is_broad_handler(handler: ast.ExceptHandler) -> bool:
    if handler.type is None:
        return True
    if isinstance(handler.type, ast.Name):
        return handler.type.id in {"BaseException", "Exception"}
    if isinstance(handler.type, ast.Tuple):
        return any(
            isinstance(item, ast.Name) and item.id in {"BaseException", "Exception"}
            for item in handler.type.elts
        )
    return False


def _has_failure_diagnostic(handler: ast.ExceptHandler) -> bool:
    if any(isinstance(node, ast.Raise) for node in ast.walk(handler)):
        return True
    log_methods = {"critical", "error", "exception", "info", "warning"}
    return any(
        isinstance(node, ast.Call)
        and (
            isinstance(node.func, ast.Attribute)
            and node.func.attr in log_methods
            or isinstance(node.func, ast.Name)
            and node.func.id == "log_degradation"
        )
        for node in ast.walk(handler)
    )


def test_law_honest_failure_broad_handlers_leave_diagnostics() -> None:
    # Given broad exception translation is allowed only with an honest trace.
    violations: list[str] = []

    # When every production handler is inspected structurally.
    for path in harness_source_files():
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"), filename=str(path))
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.ExceptHandler)
                and _is_broad_handler(node)
                and not _has_failure_diagnostic(node)
            ):
                violations.append(f"{path.name}:{node.lineno} broad failure without diagnostic")

    # Then no broad failure can disappear behind a sentinel, pass, or continue.
    assert not violations, "GD-3 broken:\n  " + "\n  ".join(violations)


# ---------------------------------------------------------------------------
# LAW 2 — Graceful Degradation: representative public entry points must degrade,
# not raise, on hostile input. (Module-specific degradation lives in each
# module's own test; this asserts the systemic guarantee.)
# ---------------------------------------------------------------------------


def test_law_graceful_router_degrades_not_raises(monkeypatch):
    from reins.harness.models import ModelRouter

    monkeypatch.setattr("reins.harness.models._get_secret", lambda *_: None)
    monkeypatch.setattr("reins.harness.local.list_models", lambda: [])
    r = ModelRouter()
    r.table = {"x": {"amdy": [{"model": "claude-nope"}], "tell": [{"model": "gpt-nope"}]}}
    res = r.route("x", "hello", "amdy")  # must not raise
    assert res.ok is False and res.error
    assert "explicit route_cloud authorization" in res.error
    assert "cloud/" not in res.error


def test_law_graceful_wiki_survives_bad_query(wiki):
    # A malformed FTS query must not crash the harness knowledge store.
    try:
        wiki.upsert_page("t", "content", slug="t")
        wiki.search_pages('"unterminated AND (')  # invalid FTS syntax
    except sqlite3.Error as error:
        assert str(error)


def test_law_graceful_odysseus_drain_survives_bad_trail(monkeypatch):
    from reins.services.fallback_agent import OdysseusAgent

    agent = OdysseusAgent()
    # A trail row missing keys must degrade, not crash the drain.
    monkeypatch.setattr(agent.trail, "_load", lambda: [{"status": "pending"}])
    monkeypatch.setattr(agent, "query_tiered_fallback", lambda p: "Error: no model")
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
