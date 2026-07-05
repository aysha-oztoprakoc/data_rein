"""
Per-agent resource budgets for the data_rein harness fleet (data-agy, data-hermes,
data-ody, data-sofia): a CPU quota that is actually enforced via a cgroup v2
`cpu.max`, and a soft/advisory GPU-VRAM allocation.

There is no per-process GPU compute quota on this hardware (only a single global
power cap, already handled by the Sofia dashboard's Kernel Tuning panel), so the
GPU side of a budget here is an allocation number other harness code (ModelRouter,
`reins.harness.local`) can later consult before loading a model into an agent's
slot - not a kernel-enforced cap. The CPU side is real: each agent gets its own
cgroup under `CGROUP_ROOT` with a hard `cpu.max` quota, applied to whatever PIDs
are currently running under that agent's process signature.

Every public function degrades gracefully (returns ok/error, never raises) -
a missing cgroup mount, a permission error, or an agent with no running process
must never crash the dashboard or the harness.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from reins.harness import paths
from reins.harness.agents import KNOWN_AGENTS
from reins.services.sudo_exec import run_sudo_cmd

CGROUP_ROOT = Path("/sys/fs/cgroup/data_rein")
CPU_PERIOD_US = 100_000  # cgroup v2 cpu.max period, matches the kernel default

_DEFAULT_BUDGET = {"cpu_pct": 100, "gpu_vram_gb": 0.0}


def _defaults() -> dict:
    return {a["name"]: dict(_DEFAULT_BUDGET) for a in KNOWN_AGENTS}


def load_budgets() -> dict:
    """Every known agent's budget, defaulting unset agents to unrestricted (100% CPU, 0GB VRAM)."""
    budgets = _defaults()
    try:
        data = json.loads(paths.agent_budgets().read_text(encoding="utf-8"))
        for name, cfg in data.items():
            if name.startswith("_"):
                continue
            budgets.setdefault(name, dict(_DEFAULT_BUDGET))
            budgets[name].update({k: v for k, v in cfg.items() if k in _DEFAULT_BUDGET})
    except Exception:
        pass
    return budgets


def save_budget(agent_name: str, *, cpu_pct: Optional[int] = None, gpu_vram_gb: Optional[float] = None) -> dict:
    """Persist a partial update to one agent's budget. Returns the full budgets dict. Never raises."""
    budgets = load_budgets()
    entry = budgets.setdefault(agent_name, dict(_DEFAULT_BUDGET))
    if cpu_pct is not None:
        entry["cpu_pct"] = max(1, min(100, int(cpu_pct)))
    if gpu_vram_gb is not None:
        entry["gpu_vram_gb"] = max(0.0, float(gpu_vram_gb))
    try:
        path = paths.agent_budgets()
        path.parent.mkdir(parents=True, exist_ok=True)
        on_disk = {"_comment": (
            "Per-agent resource budgets, read/written by reins.services.resource_budgets "
            "and editable from the Sofia dashboard's Agent Center. cpu_pct is enforced via "
            "a cgroup v2 cpu.max quota; gpu_vram_gb is a soft/advisory allocation."
        ), **budgets}
        path.write_text(json.dumps(on_disk, indent=2), encoding="utf-8")
    except Exception:
        pass
    return budgets


def cgroup_available() -> bool:
    """Whether cgroup v2 with the cpu controller is present on this system."""
    try:
        controllers = Path("/sys/fs/cgroup/cgroup.controllers").read_text(encoding="utf-8")
        return "cpu" in controllers.split()
    except Exception:
        return False


def apply_cpu_budget(agent_name: str, cpu_pct: int, pids: list[int]) -> tuple[bool, str]:
    """
    Enforce ``cpu_pct``% of one core for ``agent_name`` via cgroup v2, moving every
    PID in ``pids`` into its cgroup. Newly-forked children inherit membership
    automatically; PIDs that appear later (e.g. a process restarted after this
    call) need a fresh apply. Degrades to (False, reason) instead of raising -
    a missing cgroup mount or a sudo failure must never crash the caller.
    """
    if not cgroup_available():
        return False, "cgroup v2 (cpu controller) not available on this system"

    quota = max(1, int(cpu_pct) * CPU_PERIOD_US // 100)
    group = CGROUP_ROOT / agent_name
    script_lines = [
        f"mkdir -p {group}",
        "echo '+cpu' > /sys/fs/cgroup/cgroup.subtree_control 2>/dev/null || true",
        f"echo '+cpu' > {CGROUP_ROOT}/cgroup.subtree_control 2>/dev/null || true",
        f"echo '{quota} {CPU_PERIOD_US}' > {group}/cpu.max",
    ]
    for pid in pids:
        script_lines.append(f"echo {int(pid)} > {group}/cgroup.procs 2>/dev/null || true")

    res = run_sudo_cmd(["bash", "-c", " && ".join(script_lines)])
    if res.returncode != 0:
        return False, res.stderr.strip() or "cgroup apply failed"
    return True, f"cpu.max set to {cpu_pct}% for {agent_name} ({len(pids)} pid(s) moved)"
