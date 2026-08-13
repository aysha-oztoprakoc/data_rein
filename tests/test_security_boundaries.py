from __future__ import annotations

import ast
import subprocess
from pathlib import Path

import pytest

from conftest import SRC_ROOT
from reins.harness.sofia_health import HealthController
from reins.services import sudo_exec


def test_law_process_execution_uses_argv_without_shell() -> None:
    # Given production process calls must preserve argument boundaries.
    violations: list[str] = []

    # When process adapters and callers are inspected structurally.
    for root in (SRC_ROOT, SRC_ROOT.parents[1] / "scripts"):
        for path in root.rglob("*.py"):
            if "legacy" in path.parts:
                continue
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"), filename=str(path))
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                if any(
                    keyword.arg == "shell"
                    and isinstance(keyword.value, ast.Constant)
                    and keyword.value.value is True
                    for keyword in node.keywords
                ):
                    violations.append(f"{path.relative_to(SRC_ROOT.parents[1])}:{node.lineno} shell=True")
                if not isinstance(node.func, ast.Attribute):
                    continue
                owner = ast.unparse(node.func.value)
                if owner == "os" and node.func.attr == "system":
                    violations.append(
                        f"{path.relative_to(SRC_ROOT.parents[1])}:{node.lineno} os.system shell invocation"
                    )
                    continue
                if owner not in {"external_io", "subprocess"} or node.func.attr not in {
                    "run",
                    "Popen",
                    "check_call",
                    "check_output",
                }:
                    continue
                if node.args and isinstance(node.args[0], (ast.Constant, ast.JoinedStr)):
                    violations.append(
                        f"{path.relative_to(SRC_ROOT.parents[1])}:{node.lineno} string subprocess command"
                    )

    # Then neither a shell nor a string command can cross the process boundary.
    assert not violations, "process argv law broken:\n  " + "\n  ".join(violations)


@pytest.mark.parametrize("input_text", [None, "bounded input"])
def test_run_sudo_cmd_uses_noninteractive_argv_and_optional_stdin(
    monkeypatch: pytest.MonkeyPatch,
    input_text: str | None,
) -> None:
    calls: list[tuple[list[str], str | None, bool, bool]] = []

    def fake_run(
        argv: list[str], *, input: str | None, capture_output: bool, text: bool
    ) -> subprocess.CompletedProcess[str]:
        calls.append((argv, input, capture_output, text))
        return subprocess.CompletedProcess(argv, 0, "", "")

    monkeypatch.setattr(sudo_exec.external_io, "run", fake_run)

    result = sudo_exec.run_sudo_cmd(["install", "source", "target"], input_text=input_text)

    assert result.returncode == 0
    assert calls == [
        (["sudo", "--non-interactive", "--", "install", "source", "target"], input_text, True, True)
    ]


@pytest.mark.parametrize("relative_path", ["scripts/launch_with_sudo.sh", "tools/sudo_executor.sh"])
def test_legacy_sudo_wrappers_use_no_password_source_and_noninteractive_argv(
    relative_path: str,
) -> None:
    source = (Path(__file__).parents[1] / relative_path).read_text(encoding="utf-8")

    assert "SUDO_PASS" not in source
    assert "source " not in source
    assert "sudo -S" not in source
    assert 'sudo --non-interactive -- "$@"' in source


def test_sofia_repair_launches_agy_as_current_user(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[list[str], str]] = []

    def fake_popen(
        argv: list[str],
        *,
        cwd: str,
        stdout: int,
        stderr: int,
    ) -> subprocess.Popen[bytes]:
        del stdout, stderr
        calls.append((argv, cwd))
        return subprocess.Popen(["true"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    monkeypatch.setattr("reins.harness.sofia_health.external_io.popen", fake_popen)
    controller = HealthController(lambda _message: None, lambda _agent: None)

    controller._dispatch_repair("repair prompt")

    assert calls == [
        (["agy", "--dangerously-skip-permissions", "-c", "repair prompt"], str(Path.cwd()))
    ]
