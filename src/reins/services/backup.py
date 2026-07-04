"""
Unified backup + shutdown guard for the data_rein / omarchy workstation.

This replaces the three fragmented legacy pieces (omarchy-backup.sh, the
Portuguese PON `pon_bak_system.py`, and the orphaned `pon_shutdown_trigger.py`)
with one coherent, config-driven, testable service.

What it does, in order, when a shutdown/reboot is intercepted (`guard`):
  1. Run a local HEALTH SUITE — omarchy/Hyprland config integrity, Waybar JSONC,
     Arch/pacman consistency, essential packages, and AI-workspace reachability.
  2. If every check PASSES: refresh the portable single-file emergency rescue
     script + push the dotfiles repo, then let the power action proceed.
  3. If anything is BROKEN: BLOCK the shutdown (unless --force), drop an isolated
     failsafe backup, and tell the user exactly what failed and how to recover
     (local rescue script, or the GitHub / cloud copy).

Design guarantees:
  * Broker-independent: the guard runs everything synchronously in-process, so it
    works even when the MQTT broker is down (the legacy design's fatal flaw).
  * PON-friendly: it never polls; MQTT is an optional notification, not a dependency.
  * Failsafe: the emergency script NEVER deletes the workspace — it moves any
    existing target aside to a timestamped `.bak` before restoring.
  * Nix-ready: everything (config paths, packages, harness files) is declared in
    config/backup_config.json so a future flake can consume the same manifest.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tarfile
import base64
import io
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, List, Optional

from reins.services.logger import get_logger
from reins.harness import paths

logger = get_logger("backup")

# Only *text* config is embedded in the portable rescue script — assets (wallpapers,
# fonts, caches) would bloat it and are recoverable from the omarchy install / git.
_MAX_FILE_BYTES = 512 * 1024          # skip any single file larger than this
_MAX_EMBED_BYTES = 25 * 1024 * 1024   # hard cap on total embedded payload
_SKIP_EXT = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg", ".ico",
    ".mp4", ".mkv", ".webm", ".mp3", ".wav", ".ttf", ".otf", ".woff", ".woff2",
    ".tar", ".gz", ".zip", ".xz", ".zst", ".7z", ".pdf", ".bin", ".so",
}
_SKIP_DIRS = {".git", ".cache", "cache", "backgrounds", "wallpapers", "node_modules", "__pycache__"}


def _make_config_filter(counter: dict):
    """A tarfile filter that keeps small text config and skips assets/caches.

    `counter` accumulates {'bytes': int, 'truncated': bool} across the archive.
    """
    def _f(tarinfo):
        parts = set(tarinfo.name.split("/"))
        if parts & _SKIP_DIRS:
            return None
        if tarinfo.isreg():
            if os.path.splitext(tarinfo.name)[1].lower() in _SKIP_EXT:
                return None
            if tarinfo.size > _MAX_FILE_BYTES:
                return None
            if counter["bytes"] + tarinfo.size > _MAX_EMBED_BYTES:
                counter["truncated"] = True
                return None
            counter["bytes"] += tarinfo.size
        return tarinfo
    return _f


# --------------------------------------------------------------------------- #
# Health model
# --------------------------------------------------------------------------- #
@dataclass
class HealthResult:
    name: str
    ok: bool
    detail: str = ""


@dataclass
class HealthReport:
    results: List[HealthResult] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(r.ok for r in self.results)

    @property
    def failures(self) -> List[HealthResult]:
        return [r for r in self.results if not r.ok]

    def add(self, name: str, ok: bool, detail: str = "") -> None:
        self.results.append(HealthResult(name, ok, detail))


def _expand(p: str) -> Path:
    return Path(os.path.expanduser(p))


def _now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


# --------------------------------------------------------------------------- #
# Service
# --------------------------------------------------------------------------- #
class BackupService:
    """Config-driven backup + health + shutdown guard."""

    def __init__(self, config: Optional[dict] = None, config_path: Optional[Path] = None):
        self.config_path = config_path or paths.backup_config()
        self.config = config if config is not None else self._load_config()

    def _load_config(self) -> dict:
        try:
            return json.loads(Path(self.config_path).read_text())
        except Exception as e:  # graceful degradation -> minimal safe defaults
            logger.error(f"Could not read backup config ({e}); using minimal defaults.")
            return {"health": {}, "dotfiles": {}, "harness": {}}

    # ----------------------------------------------------------------- health
    def health_check(self) -> HealthReport:
        """Run every local integrity check. Never raises; each check is isolated."""
        h = self.config.get("health", {})
        report = HealthReport()
        for name, fn, arg in (
            ("hypr_configs", self._check_files_nonempty, h.get("hypr_critical_files", [])),
            ("waybar_jsonc", self._check_waybar, h.get("waybar_config")),
            ("omarchy_theme", self._check_dir_exists, h.get("omarchy_theme_dir")),
            ("hypr_syntax", self._check_hypr_syntax, h.get("hypr_syntax_dirs", [])),
            ("pacman_db", self._check_pacman, None),
            ("essential_packages", self._check_packages, h.get("essential_packages", [])),
            ("ai_workspace", self._check_files_nonempty, h.get("workspace_paths", [])),
        ):
            try:
                ok, detail = fn(arg)
            except Exception as e:  # a broken check must not crash the guard
                ok, detail = False, f"check error: {e}"
            report.add(name, ok, detail)
        return report

    def _check_files_nonempty(self, files) -> tuple:
        missing = []
        for f in files or []:
            p = _expand(f)
            # a directory counts as present if it exists and is non-empty
            if p.is_dir():
                if not any(p.iterdir()):
                    missing.append(f"{f} (empty dir)")
            elif not (p.exists() and p.stat().st_size > 0):
                missing.append(f)
        return (not missing, "OK" if not missing else f"missing/empty: {', '.join(missing)}")

    def _check_waybar(self, conf) -> tuple:
        if not conf:
            return True, "no waybar config configured (skipped)"
        p = _expand(conf)
        if not p.exists() or p.stat().st_size == 0:
            return True, "waybar config absent (skipped)"
        # strip // comments then parse as JSON
        stripped = "\n".join(ln for ln in p.read_text().splitlines() if not ln.strip().startswith("//"))
        try:
            json.loads(stripped)
            return True, "valid JSONC"
        except json.JSONDecodeError as e:
            return False, f"invalid JSONC: {e}"

    def _check_dir_exists(self, d) -> tuple:
        if not d:
            return True, "not configured (skipped)"
        return (_expand(d).is_dir(), "OK" if _expand(d).is_dir() else f"missing dir: {d}")

    def _check_hypr_syntax(self, dirs) -> tuple:
        """Catch deprecated/malformed Hyprland rules that silently break the session."""
        bad = []
        for base in dirs or []:
            root = _expand(base)
            if not root.exists():
                continue
            for conf in root.rglob("*.conf"):
                try:
                    content = conf.read_text(errors="replace")
                except Exception:
                    continue
                if "windowrulev2" in content:
                    bad.append(f"{conf}: deprecated windowrulev2")
                if re.search(r"windowrule\s*=\s*match:", content):
                    bad.append(f"{conf}: malformed 'match:' rule")
        return (not bad, "OK" if not bad else "; ".join(bad[:4]))

    def _check_pacman(self, _arg) -> tuple:
        """Arch consistency: the DB must not be locked and must be queryable."""
        if not shutil.which("pacman"):
            return True, "pacman not present (skipped)"
        if _expand("/var/lib/pacman/db.lck").exists() or Path("/var/lib/pacman/db.lck").exists():
            return False, "pacman db is LOCKED (/var/lib/pacman/db.lck) — an update may be mid-flight"
        try:
            r = subprocess.run(["pacman", "-Qq"], capture_output=True, text=True, timeout=15)
            return (r.returncode == 0, "OK" if r.returncode == 0 else "pacman -Qq failed")
        except Exception as e:
            return False, f"pacman query failed: {e}"

    def _check_packages(self, pkgs) -> tuple:
        if not pkgs or not shutil.which("pacman"):
            return True, "no essential packages configured (skipped)"
        missing = []
        for pkg in pkgs:
            r = subprocess.run(["pacman", "-Q", pkg], capture_output=True, text=True)
            if r.returncode != 0:
                missing.append(pkg)
        return (not missing, "OK" if not missing else f"NOT installed: {', '.join(missing)}")

    # ------------------------------------------------------------- emergency
    def generate_emergency_script(self, dest: Optional[str] = None) -> Path:
        """Produce ONE self-contained bash rescue script (portable to a live USB).

        The critical *config* dirs are embedded as a base64 tarball inside the
        script (so it restores offline); the large harness is restored from GitHub
        by the script (the repo is the portable source). The script NEVER deletes
        anything — it moves existing targets to timestamped `.bak` first.
        """
        out = _expand(dest or self.config.get("emergency_script", "~/.cache/data_rein/backup/omarchy_rescue.sh"))
        out.parent.mkdir(parents=True, exist_ok=True)

        # Tar the configured dotfiles paths (whatever exists) in-memory -> base64.
        df = self.config.get("dotfiles", {})
        buf = io.BytesIO()
        included: List[str] = []
        counter = {"bytes": 0, "truncated": False}
        cfilter = _make_config_filter(counter)
        with tarfile.open(fileobj=buf, mode="w:gz") as tar:
            for rel in df.get("paths", []):
                p = _expand(rel)
                if p.exists():
                    # store relative to $HOME so the script can extract into ~
                    arcname = str(p).replace(str(Path.home()) + "/", "")
                    tar.add(str(p), arcname=arcname, filter=cfilter)
                    included.append(arcname)
        if counter["truncated"]:
            logger.warning(f"Emergency payload hit the {_MAX_EMBED_BYTES // (1024*1024)}MB cap; "
                           "large assets omitted (restored from git instead).")
        payload_b64 = base64.b64encode(buf.getvalue()).decode()

        harness = self.config.get("harness", {})
        repo = harness.get("repo", "")
        branch = harness.get("branch", "main")
        script = _EMERGENCY_TEMPLATE.format(
            stamp=_now_stamp(),
            included=" ".join(included) or "(none found)",
            repo=repo,
            branch=branch,
            harness_root=harness.get("root", "~/data_rein"),
            payload_b64=payload_b64,
        )
        out.write_text(script)
        out.chmod(0o755)
        logger.info(f"Emergency rescue script written -> {out} ({len(included)} config paths embedded)")
        return out

    def failsafe_backup(self) -> Optional[Path]:
        """Isolated local snapshot of the critical configs, used when health FAILS.

        Stored under a durable cache dir (never /tmp) so a broken shutdown can't
        lose it. Best effort — returns the archive path or None.
        """
        dest_dir = _expand(self.config.get("failsafe_backup_dir", "~/.cache/data_rein/backup/failsafe"))
        dest_dir.mkdir(parents=True, exist_ok=True)
        archive = dest_dir / f"failsafe_{_now_stamp()}.tar.gz"
        df = self.config.get("dotfiles", {})
        cfilter = _make_config_filter({"bytes": 0, "truncated": False})
        try:
            with tarfile.open(archive, "w:gz") as tar:
                for rel in df.get("paths", []):
                    p = _expand(rel)
                    if p.exists():
                        tar.add(str(p), arcname=str(p).replace(str(Path.home()) + "/", ""), filter=cfilter)
            logger.info(f"Failsafe backup -> {archive}")
            return archive
        except Exception as e:
            logger.error(f"Failsafe backup failed: {e}")
            return None

    # ------------------------------------------------------------------ push
    def _dotfiles_git(self) -> List[str]:
        df = self.config.get("dotfiles", {})
        return ["git", f"--git-dir={_expand(df.get('git_dir', '~/.dotfiles'))}",
                f"--work-tree={_expand(df.get('work_tree', '~'))}"]

    def push_dotfiles(self) -> bool:
        """Commit + push the dotfiles bare repo. Best effort, never raises."""
        df = self.config.get("dotfiles", {})
        git = self._dotfiles_git()
        if not _expand(df.get("git_dir", "~/.dotfiles")).exists():
            logger.info("Dotfiles repo absent; skipping push.")
            return False
        try:
            for rel in df.get("paths", []):
                subprocess.run(git + ["add", str(_expand(rel))], check=False,
                               capture_output=True)
            staged = subprocess.run(git + ["diff", "--staged", "--quiet"])
            if staged.returncode == 0:
                logger.info("Dotfiles unchanged; nothing to push.")
                return True
            subprocess.run(git + ["commit", "-m", f"data_rein backup {_now_stamp()}"],
                           check=False, capture_output=True)
            r = subprocess.run(git + ["push", df.get("remote", "origin"), df.get("branch", "main")],
                               capture_output=True, text=True)
            ok = r.returncode == 0
            logger.info("Dotfiles pushed." if ok else f"Dotfiles push failed: {r.stderr.strip()}")
            return ok
        except Exception as e:
            logger.error(f"Dotfiles push errored: {e}")
            return False

    def backup_now(self) -> dict:
        """Refresh the emergency script + push dotfiles. Assumes health already OK."""
        script = self.generate_emergency_script()
        pushed = self.push_dotfiles()
        return {"emergency_script": str(script), "dotfiles_pushed": pushed}

    # ----------------------------------------------------------------- guard
    def _execute_power(self, action: str) -> int:
        """Run the real power action. Isolated so tests can stub it."""
        cmd = {"reboot": ["systemctl", "reboot"],
               "poweroff": ["systemctl", "poweroff"],
               "shutdown": ["systemctl", "poweroff"]}.get(action)
        if not cmd:
            logger.error(f"Unknown power action: {action}")
            return 2
        logger.info(f"Executing power action: {' '.join(cmd)}")
        return subprocess.run(cmd).returncode

    def guard(self, action: str, *, force: bool = False, dry_run: bool = False,
              execute: Optional[Callable[[str], int]] = None) -> int:
        """Intercept a shutdown/reboot: health-gate it, back up, then allow or block.

        Returns 0 if the action was (or would be) allowed, non-zero if blocked.
        Blocking on failure is the configured policy; `force` overrides it. The user
        is never permanently trapped — `reboot --force` (or `reins backup guard
        <action> --force`) always proceeds.
        """
        report = self.health_check()
        executor = execute or self._execute_power

        if report.passed:
            logger.info("Health OK — backing up, then allowing power action.")
            self.backup_now()
            if dry_run:
                print(f"[bak] health OK; would {action} (dry-run).")
                return 0
            return executor(action)

        # --- broken ---
        detail = "; ".join(f"{r.name}: {r.detail}" for r in report.failures)
        archive = self.failsafe_backup()
        if force:
            logger.warning(f"Health FAILED but --force set; proceeding. Failures: {detail}")
            print(f"[bak] ⚠ health FAILED ({len(report.failures)}) — forced. Failsafe: {archive}")
            if dry_run:
                return 0
            return executor(action)

        # blocked
        print("\n\033[1;31m[BAK] SHUTDOWN BLOCKED — omarchy/workspace health check failed:\033[0m")
        for r in report.failures:
            print(f"  \033[31m✗\033[0m {r.name}: {r.detail}")
        print(f"\n  Failsafe snapshot saved: {archive}")
        print(f"  Recover from the rescue script, GitHub, or fix the issues above.")
        print(f"  To override anyway:  {action} --force\n")
        self._notify_blocked(report)
        return 1

    def _notify_blocked(self, report: HealthReport) -> None:
        if not shutil.which("notify-send"):
            return
        msg = f"{len(report.failures)} check(s) failed. Shutdown blocked to protect the workspace."
        try:
            subprocess.run(["notify-send", "-u", "critical", "data_rein BAK — shutdown blocked", msg],
                           check=False, capture_output=True, timeout=5)
        except Exception:
            pass

    # ---------------------------------------------------------------- install
    # Sentinel-delimited block so (un)install is idempotent and reversible.
    _MARK = "data_rein backup guard"

    def render_hooks(self) -> dict:
        """Pure render of every artifact `install` writes (handy for tests)."""
        venv_py = _expand(self.config.get("harness", {}).get("root", "~/data_rein")) / ".venv/bin/python"
        wrapper = _expand("~/.local/bin/omarchy-safe-power.sh")
        wrapper_body = _POWER_WRAPPER.format(python=venv_py)
        alias_block = _ALIAS_BLOCK.format(mark=self._MARK, wrapper=wrapper)
        user_unit = _USER_SHUTDOWN_UNIT.format(python=venv_py)
        system_unit = _SYSTEM_SHUTDOWN_UNIT.format(python=venv_py)
        return {
            "wrapper_path": wrapper,
            "wrapper_body": wrapper_body,
            "alias_block": alias_block,
            "user_unit": user_unit,
            "system_unit": system_unit,
        }

    @staticmethod
    def _splice_block(text: str, mark: str, block: str) -> str:
        """Replace an existing >>> mark >>> ... <<< mark <<< block, or append it."""
        start, end = f"# >>> {mark} >>>", f"# <<< {mark} <<<"
        pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
        wrapped = f"{start}\n{block}\n{end}"
        if pattern.search(text):
            return pattern.sub(wrapped, text)
        return text.rstrip() + "\n\n" + wrapped + "\n"

    def install_hooks(self) -> List[str]:
        """Wire the guard into the live system (user-space; system unit needs sudo).

        Returns human-readable notes about what was done / what needs root.
        """
        art = self.render_hooks()
        notes: List[str] = []

        # 1. power-guard wrapper
        art["wrapper_path"].parent.mkdir(parents=True, exist_ok=True)
        art["wrapper_path"].write_text(art["wrapper_body"])
        art["wrapper_path"].chmod(0o755)
        notes.append(f"wrote power wrapper -> {art['wrapper_path']}")

        # 2. bash + zsh alias blocks (idempotent)
        for rc in ("~/.bashrc", "~/.zshrc"):
            p = _expand(rc)
            if p.exists():
                p.write_text(self._splice_block(p.read_text(), self._MARK, art["alias_block"]))
                notes.append(f"spliced guard aliases into {rc}")

        # 3. user systemd unit (best-effort backup on session shutdown, no root)
        udir = _expand("~/.config/systemd/user")
        udir.mkdir(parents=True, exist_ok=True)
        (udir / "data-rein-backup.service").write_text(art["user_unit"])
        notes.append("wrote ~/.config/systemd/user/data-rein-backup.service "
                     "(enable: systemctl --user enable data-rein-backup.service)")

        # 4. system unit -> repo only; enabling it (to catch system-initiated
        #    shutdowns) needs root, so we print the commands instead of sudo-ing.
        repo_unit = _expand(self.config.get("harness", {}).get("root", "~/data_rein")) / "systemd" / "data-rein-backup.service"
        repo_unit.parent.mkdir(parents=True, exist_ok=True)
        repo_unit.write_text(art["system_unit"])
        notes.append(f"wrote system unit -> {repo_unit}")
        notes.append("to catch SYSTEM-initiated shutdowns, run (root):")
        notes.append(f"  sudo cp {repo_unit} /etc/systemd/system/ && sudo systemctl enable data-rein-backup.service")
        return notes

    def uninstall_hooks(self) -> List[str]:
        notes = []
        for rc in ("~/.bashrc", "~/.zshrc"):
            p = _expand(rc)
            if p.exists():
                start, end = f"# >>> {self._MARK} >>>", f"# <<< {self._MARK} <<<"
                cleaned = re.sub(re.escape(start) + r".*?" + re.escape(end) + r"\n?", "", p.read_text(), flags=re.DOTALL)
                p.write_text(cleaned)
                notes.append(f"removed guard block from {rc}")
        uu = _expand("~/.config/systemd/user/data-rein-backup.service")
        if uu.exists():
            uu.unlink(); notes.append("removed user systemd unit")
        notes.append("if you enabled the system unit: sudo systemctl disable data-rein-backup.service "
                     "&& sudo rm /etc/systemd/system/data-rein-backup.service")
        return notes

    # --------------------------------------------------------------- restore
    def restore(self, source: str = "local") -> bool:
        """Restore the workspace. source: local | github | gcloud."""
        if source == "github":
            return self._restore_github()
        if source == "gcloud":
            return self._restore_gcloud()
        return self._restore_local()

    def _restore_local(self) -> bool:
        script = _expand(self.config.get("emergency_script", "~/.cache/data_rein/backup/omarchy_rescue.sh"))
        if not script.exists():
            logger.error(f"No local rescue script at {script}; run `reins backup emergency` first.")
            return False
        logger.info(f"Running local rescue script: {script}")
        return subprocess.run(["bash", str(script), "--restore"]).returncode == 0

    def _restore_github(self) -> bool:
        gh = self.config.get("remote_restore", {}).get("github", {})
        repo, branch = gh.get("repo"), gh.get("branch", "main")
        root = _expand(self.config.get("harness", {}).get("root", "~/data_rein"))
        if not repo:
            logger.error("No GitHub repo configured for restore.")
            return False
        if (root / ".git").exists():
            logger.info(f"Pulling latest {branch} into {root}")
            return subprocess.run(["git", "-C", str(root), "pull", "origin", branch]).returncode == 0
        logger.info(f"Cloning {repo} -> {root}")
        return subprocess.run(["git", "clone", "-b", branch, repo, str(root)]).returncode == 0

    def _restore_gcloud(self) -> bool:
        gc = self.config.get("remote_restore", {}).get("gcloud", {})
        if not gc.get("enabled") or not shutil.which("gcloud"):
            logger.error("gcloud restore not available (SDK missing or disabled in config).")
            return False
        bucket = gc.get("bucket")
        root = _expand(self.config.get("harness", {}).get("root", "~/data_rein"))
        return subprocess.run(["gcloud", "storage", "rsync", "-r", bucket, str(root)]).returncode == 0


# --------------------------------------------------------------------------- #
# Emergency rescue script template (self-contained, failsafe-first)
# --------------------------------------------------------------------------- #
_EMERGENCY_TEMPLATE = r"""#!/usr/bin/env bash
# data_rein / omarchy EMERGENCY RESCUE SCRIPT  (generated {stamp})
# Portable: copy to a live USB and run `bash omarchy_rescue.sh --restore`.
#
# FAILSAFE CONTRACT:
#   * Never deletes the workspace or your home. Existing targets are moved to a
#     timestamped .bak before anything is written.
#   * --check does a dry run; --restore performs the recovery.
#   * Embedded below (base64 tar.gz): {included}
set -uo pipefail

STAMP="$(date -u +%Y%m%d-%H%M%S)"
HOME_DIR="${{HOME:-/root}}"
REPO="{repo}"
BRANCH="{branch}"
HARNESS_ROOT="${{HARNESS_ROOT:-{harness_root}}}"
HARNESS_ROOT="${{HARNESS_ROOT/#\~/$HOME_DIR}}"
MODE="${{1:---check}}"

say()  {{ printf '\033[1;36m[rescue]\033[0m %s\n' "$*"; }}
warn() {{ printf '\033[1;33m[rescue]\033[0m %s\n' "$*"; }}
die()  {{ printf '\033[1;31m[rescue] FATAL:\033[0m %s\n' "$*"; exit 1; }}

backup_existing() {{  # move a path aside, never delete
  local target="$1"
  if [ -e "$target" ]; then
    warn "preserving existing $target -> $target.bak-$STAMP"
    mv "$target" "$target.bak-$STAMP" || die "could not preserve $target"
  fi
}}

PAYLOAD_B64='{payload_b64}'

restore_configs() {{
  say "restoring embedded omarchy/hypr configs into $HOME_DIR ..."
  local tmp; tmp="$(mktemp -d)"
  echo "$PAYLOAD_B64" | base64 -d > "$tmp/configs.tar.gz" || die "payload decode failed"
  # Preserve only the specific subtrees we restore (e.g. .config/hypr), never all
  # of ~/.config — the user's other apps stay untouched.
  local members; members="$(tar -tzf "$tmp/configs.tar.gz" 2>/dev/null \
    | awk -F/ '{{ if ($1==".config" && NF>=2) print $1"/"$2; else print $1 }}' | sort -u)"
  for top in $members; do
    [ -n "$top" ] && backup_existing "$HOME_DIR/$top"
  done
  tar -xzf "$tmp/configs.tar.gz" -C "$HOME_DIR" || die "config extract failed"
  rm -rf "$tmp"
  say "configs restored."
}}

restore_harness() {{
  [ -z "$REPO" ] && {{ warn "no harness repo configured; skipping harness restore"; return 0; }}
  if [ -d "$HARNESS_ROOT/.git" ]; then
    say "updating harness at $HARNESS_ROOT ($BRANCH) ..."
    git -C "$HARNESS_ROOT" pull origin "$BRANCH" || warn "harness pull failed (network?)"
  else
    backup_existing "$HARNESS_ROOT"
    say "cloning harness $REPO -> $HARNESS_ROOT ..."
    git clone -b "$BRANCH" "$REPO" "$HARNESS_ROOT" || warn "harness clone failed (network?)"
  fi
}}

case "$MODE" in
  --check)
    say "DRY RUN. Would restore embedded configs and (re)clone the harness."
    say "  home         : $HOME_DIR"
    say "  harness root : $HARNESS_ROOT"
    say "  harness repo : ${{REPO:-<none>}} ($BRANCH)"
    echo "$PAYLOAD_B64" | base64 -d 2>/dev/null | tar -tzf - 2>/dev/null | sed 's/^/    embed: /' || warn "payload unreadable"
    say "Run with --restore to apply."
    ;;
  --restore)
    command -v tar >/dev/null || die "tar is required"
    restore_configs
    restore_harness
    say "DONE. Nothing was deleted; previous files are *.bak-$STAMP. Log back into Hyprland to verify."
    ;;
  *) die "usage: $0 [--check|--restore]";;
esac
"""


# --------------------------------------------------------------------------- #
# Live-wiring templates (written by `reins backup install`)
# --------------------------------------------------------------------------- #
# Power wrapper: the shell aliases call this; it runs the guard synchronously
# (no broker dependency) and only reaches the real power action if allowed.
_POWER_WRAPPER = r"""#!/usr/bin/env bash
# data_rein safe power guard — health-gates shutdown/reboot then backs up.
# Installed by `reins backup install`. Override a block with:  <action> --force
export DBUS_SESSION_BUS_ADDRESS="${{DBUS_SESSION_BUS_ADDRESS:-unix:path=/run/user/$(id -u)/bus}}"
ACTION="${{1:-poweroff}}"; shift || true
exec {python} -m reins.cli backup guard "$ACTION" "$@"
"""

# Shell block spliced into ~/.bashrc and ~/.zshrc (idempotent, sentinel-delimited).
_ALIAS_BLOCK = r"""# {mark}: intercept power commands + `bak` helper (edit via `reins backup install`)
reboot()   {{ "{wrapper}" reboot "$@"; }}
poweroff() {{ "{wrapper}" poweroff "$@"; }}
shutdown() {{ "{wrapper}" poweroff "$@"; }}
bak()      {{ ( cd ~/data_rein && .venv/bin/python -m reins.cli backup "$@" ); }}"""

# User-session unit: best-effort backup when the user session goes down (no root).
_USER_SHUTDOWN_UNIT = """[Unit]
Description=data_rein pre-shutdown backup (best effort)
DefaultDependencies=no
Before=shutdown.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/bin/true
# On stop (shutdown), run a bounded backup. Never blocks the machine: hard timeout.
ExecStop={python} -m reins.cli backup now
TimeoutStopSec=90

[Install]
WantedBy=default.target
"""

# System unit: catches SYSTEM-initiated shutdowns (GUI button, `systemctl reboot`,
# updates). Best-effort backup with a hard timeout so it can NEVER hang the machine.
_SYSTEM_SHUTDOWN_UNIT = """[Unit]
Description=data_rein pre-shutdown backup guard (system)
DefaultDependencies=no
Before=shutdown.target reboot.target halt.target
Requires=network-online.target
After=network-online.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/bin/true
ExecStop={python} -m reins.cli backup now
TimeoutStopSec=90

[Install]
WantedBy=multi-user.target
"""
