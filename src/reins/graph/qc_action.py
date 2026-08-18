from __future__ import annotations

import logging
import subprocess
from typing import Any

from reins.harness import external_io
from reins.services.logger import log_degradation

logger = logging.getLogger("reins.graph.qc_action")


def autonomous_merge(patch_file: str, report: Any) -> bool:
    """
    Applies a patch and commits it if the report classifies the change as LOW risk
    and passing all quality checks.
    """
    passed = getattr(report, "tests_passed", getattr(report, "passed", False))
    if report.risk == "LOW" and passed:
        logger.info("Applying autonomous merge for %s", patch_file)
        try:
            # Autonomous execution wrapped in external_io breaker
            external_io.call(
                "git:apply",
                lambda: subprocess.run(["git", "apply", patch_file], check=True, capture_output=True),
            )
            external_io.call(
                "git:add",
                lambda: subprocess.run(["git", "add", "."], check=True, capture_output=True),
            )
            external_io.call(
                "git:commit",
                lambda: subprocess.run(
                    ["git", "commit", "-m", f"Auto-merged: QC Passed\n\n{getattr(report, 'summary', getattr(report, 'reason', ''))}"],
                    check=True,
                    capture_output=True,
                ),
            )
            return True
        except Exception as e:
            logger.error("Failed to autonomously merge patch: %s", e, exc_info=True)
            log_degradation("reins.graph.qc_action")
            try:
                external_io.call(
                    "git:checkout",
                    lambda: subprocess.run(["git", "checkout", "."], check=False),
                )
            except Exception as checkout_err:
                logger.error("Failed to revert checkout on failure: %s", checkout_err, exc_info=True)
                log_degradation("reins.graph.qc_action.revert")
            return False
    return False
