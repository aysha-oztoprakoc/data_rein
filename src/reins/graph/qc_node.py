"""
QualityControlNode: Reactive Quality Gate FBE Node.

Subscribes to QC_REQUEST (fbe/qc/request), runs deterministic analysis via QCRunner,
records reports and module baselines into KuzuDB, triggers autonomous merges
for LOW-risk changes, and publishes QC_REPORT.
"""
from __future__ import annotations

import json
import logging
import threading
import uuid
from typing import Any, Optional

from reins.graph.engine import GraphNode
from reins.graph.fbe import FBEAttribute, FBEState
from reins.graph.qc_action import autonomous_merge
from reins.graph.qc_runner import QCReport, QCRunner
from reins.graph.qc_schema import init_qc_schema
from reins.services.logger import log_degradation

logger = logging.getLogger("reins.graph.qc_node")


class QualityControlNode(GraphNode):
    """
    Reactive Quality Control Gate Node.
    """

    def __init__(self, kuzu_db: Optional[Any] = None) -> None:
        super().__init__(name="QualityControlNode")
        self.kuzu_db = kuzu_db
        self.runner = QCRunner()
        if self.kuzu_db:
            init_qc_schema(self.kuzu_db)

    def handle_event(self, attribute: FBEAttribute) -> Optional[FBEAttribute]:
        logger.info("QualityControlNode processing QC request for task %s", attribute.task_id)
        data = attribute.value
        if isinstance(data, dict):
            change_desc = data.get("description", "Routine code modification")
            patch_file = data.get("patch_file")
            target_path = data.get("target_path")
        else:
            change_desc = str(data)
            patch_file = None
            target_path = None

        # Fetch baseline coverage from KuzuDB if available
        baseline_cov = 80.0
        if self.kuzu_db:
            try:
                res = self.kuzu_db.execute("MATCH (m:ModuleHealth) RETURN avg(m.coverage) AS avg_cov;")
                if res.has_next():
                    row = res.get_next()
                    if row[0] is not None:
                        baseline_cov = float(row[0])
            except Exception as e:
                logger.debug("Baseline lookup fallback: %s", e, exc_info=True)
                log_degradation("reins.graph.qc_node.baseline")

        # Run deterministic quality analysis
        report: QCReport = self.runner.evaluate_change(
            change_desc=change_desc,
            patch_file=patch_file,
            target_path=target_path,
            baseline_coverage=baseline_cov,
        )

        merged = False
        if patch_file and report.recommendation == "AUTO_MERGE":
            merged = autonomous_merge(patch_file, report)

        # Persist report in KuzuDB
        if self.kuzu_db:
            try:
                self.kuzu_db.execute(
                    "CREATE (q:QualityReport {commit: $commit, risk: $risk, passed: $passed});",
                    {"commit": attribute.task_id, "risk": report.risk, "passed": report.tests_passed},
                )
            except Exception as e:
                logger.debug("Failed to store report in KuzuDB: %s", e, exc_info=True)
                log_degradation("reins.graph.qc_node.persist")

        report_dict = report.to_dict()
        report_dict["merged"] = merged

        return FBEAttribute(
            name=FBEState.QC_REPORT.value,
            value=report_dict,
            task_id=attribute.task_id,
            metadata={"source_node": self.name},
        )
