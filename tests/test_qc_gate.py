from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

from reins.graph.fbe import FBEAttribute, FBEState
from reins.graph.qc_action import autonomous_merge
from reins.graph.qc_node import QualityControlNode
from reins.graph.qc_runner import QCReport, QCRunner


def test_qc_runner_evaluation(tmp_path: Path) -> None:
    empty_dir = tmp_path / "scan"
    empty_dir.mkdir()
    runner = QCRunner()
    report: QCReport = runner.evaluate_change(
        change_desc="Routine refactor of parser",
        target_path=str(empty_dir),
        baseline_coverage=82.0,
    )
    assert report.risk == "LOW"
    assert report.tests_passed is True
    assert report.recommendation == "AUTO_MERGE"
    assert report.coverage_delta > 0


def test_qc_runner_flags_high_risk_keywords() -> None:
    runner = QCRunner()
    report: QCReport = runner.evaluate_change(
        change_desc="Update cryptography auth and database_migration layer",
        baseline_coverage=80.0,
    )
    assert report.risk == "HIGH"
    assert report.recommendation == "HUMAN_REVIEW_REQUIRED"


def test_quality_control_node_produces_qc_report(tmp_path: Path) -> None:
    scan_dir = tmp_path / "scan"
    scan_dir.mkdir()
    qc_node = QualityControlNode(kuzu_db=None)
    attr = FBEAttribute(
        name=FBEState.QC_REQUEST.value,
        value={"description": "Refactor utility helpers", "target_path": str(scan_dir)},
        task_id="task-qc-01",
    )
    res = qc_node.handle_event(attr)
    assert res is not None
    assert res.name == FBEState.QC_REPORT.value
    assert res.value["tests_passed"] is True
    assert res.value["recommendation"] == "AUTO_MERGE"


def test_autonomous_merge_executes_only_on_low_risk_pass() -> None:
    report_low = QCReport(change_desc="docs update", risk="LOW", tests_passed=True)
    report_high = QCReport(change_desc="auth change", risk="HIGH", tests_passed=True)

    with patch("subprocess.run") as mock_run:
        mock_run.return_value.returncode = 0
        # High risk should NOT merge autonomously
        assert autonomous_merge("dummy.patch", report_high) is False
        mock_run.assert_not_called()

        # Low risk SHOULD merge autonomously
        assert autonomous_merge("dummy.patch", report_low) is True
        assert mock_run.call_count >= 3
