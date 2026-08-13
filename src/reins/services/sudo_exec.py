"""
Shared privileged-command runner for the harness.
"""

from __future__ import annotations

import subprocess

from reins.harness import external_io


def run_sudo_cmd(
    cmd_list: list[str], *, input_text: str | None = None
) -> subprocess.CompletedProcess[str]:
    full_cmd = ["sudo", "--non-interactive", "--", *cmd_list]
    return external_io.run(full_cmd, input=input_text, capture_output=True, text=True)
