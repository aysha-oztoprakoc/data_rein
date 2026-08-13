from __future__ import annotations

import importlib.util
import subprocess
from collections.abc import Sequence
from pathlib import Path
from typing import Protocol, runtime_checkable

import pytest


class _ExternalIO(Protocol):
    def run(
        self,
        command: Sequence[str],
        *,
        capture_output: bool,
        text: bool,
        check: bool,
    ) -> subprocess.CompletedProcess[str]: ...


@runtime_checkable
class _ReportModule(Protocol):
    external_io: _ExternalIO

    def run_probe(self, command: Sequence[str], *, contains: str | None = None) -> str: ...

    def generate(self, output: Path | None = None) -> str: ...


def _load_report_module() -> _ReportModule:
    path = Path(__file__).parents[1] / "scripts" / "gen_report.py"
    spec = importlib.util.spec_from_file_location("gen_report", path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert isinstance(module, _ReportModule)
    return module


gen_report = _load_report_module()


def test_run_probe_filters_in_python_and_uses_argv(monkeypatch: pytest.MonkeyPatch) -> None:
    # Given a successful probe containing relevant and irrelevant records.
    observed: list[list[str]] = []

    def fake_run(
        command: Sequence[str], *, capture_output: bool, text: bool, check: bool
    ) -> subprocess.CompletedProcess[str]:
        assert capture_output and text and not check
        observed.append(list(command))
        return subprocess.CompletedProcess(command, 0, "CPU: useful\nCache: omit\n", "")

    monkeypatch.setattr(gen_report.external_io, "run", fake_run)

    # When the probe is filtered, then no shell syntax is used and filtering is local.
    assert gen_report.run_probe(["lscpu"], contains="CPU:") == "CPU: useful"
    assert observed == [["lscpu"]]


def test_generate_degrades_each_failed_probe_and_writes_report(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    # Given every external executable is unavailable.
    def missing(
        _command: Sequence[str], *, capture_output: bool, text: bool, check: bool
    ) -> subprocess.CompletedProcess[str]:
        assert capture_output and text and not check
        raise FileNotFoundError("missing")

    monkeypatch.setattr(gen_report.external_io, "run", missing)

    # When a report is generated, then every section records degradation and output is written.
    output = tmp_path / "report.txt"
    content = gen_report.generate(output)
    assert content.count("probe unavailable: missing") == 6
    assert output.read_text(encoding="utf-8") == content
