"""
Shared privileged-command runner for the harness.

Every place that needs a one-off root action (renice, cgroup writes, CPU
governor, GPU power cap) shells out through the same cached-credential
launcher (`scripts/launch_with_sudo.sh`) instead of each caller re-deriving
its own sudo invocation.
"""

from __future__ import annotations

import subprocess

from reins.harness import paths


def run_sudo_cmd(cmd_list: list[str]) -> subprocess.CompletedProcess:
    """Run ``cmd_list`` as root via the harness's cached-credential sudo launcher."""
    sudo_script = str(paths.home() / "scripts" / "launch_with_sudo.sh")
    full_cmd = ["bash", sudo_script, "sudo"] + cmd_list
    return subprocess.run(full_cmd, capture_output=True, text=True)
