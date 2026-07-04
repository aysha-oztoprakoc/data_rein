"""
Live omarchy/Hyprland environment sanity — the checks the shutdown guard runs.

Relocated into the repo from ~/.hermes so there is one source of truth. Like the
other environment tests, these `skip` gracefully when omarchy isn't the host (so
the suite stays green on a fresh checkout / CI) but verify a real workstation via
the same `reins.services.backup` health suite the guard uses at shutdown.
"""

import os

import pytest

from conftest import require
from reins.services.backup import BackupService


def _omarchy_present() -> bool:
    return os.path.isdir(os.path.expanduser("~/.config/hypr"))


def test_hypr_and_workspace_health():
    """On an omarchy host, the guard's core integrity checks must pass."""
    require("~/.config/hypr", "omarchy/Hyprland not present on this host")
    report = BackupService().health_check()
    # These structural checks must hold on a healthy workstation; report the exact
    # failure if not, since a fail here means the guard would block a shutdown.
    critical = {"hypr_configs", "waybar_jsonc", "hypr_syntax"}
    broken = [r for r in report.results if r.name in critical and not r.ok]
    assert not broken, "omarchy integrity failure(s): " + "; ".join(
        f"{r.name}: {r.detail}" for r in broken
    )


def test_no_deprecated_hyprland_syntax():
    """Deprecated windowrulev2 / malformed match rules break the session silently."""
    require("~/.config/hypr", "omarchy/Hyprland not present on this host")
    svc = BackupService()
    ok, detail = svc._check_hypr_syntax(svc.config.get("health", {}).get("hypr_syntax_dirs", []))
    assert ok, f"Hyprland syntax violation: {detail}"
