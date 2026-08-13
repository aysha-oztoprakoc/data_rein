"""
Tests for the unified backup + shutdown-guard (reins.services.backup).

Hermetic: every check runs against a tmp_path config, never the real ~/.config or
a real reboot. Enforces the load-bearing guarantees — health gating, block-on-fail
with a force override, and the emergency script's never-delete failsafe contract.
"""

import subprocess
from pathlib import Path


from reins.services.backup import BackupService, HealthReport, HealthResult


def _svc(tmp_path, monkeypatch=None) -> BackupService:
    if monkeypatch is not None:
        monkeypatch.setenv("DATA_REIN_HOME", str(tmp_path))
        monkeypatch.setenv("HOME", str(tmp_path))
    cfg = {
        "dotfiles": {
            "git_dir": str(tmp_path / ".dotfiles"),
            "work_tree": str(tmp_path),
            "paths": [str(tmp_path / ".config/hypr")],
        },
        "harness": {"repo": "", "branch": "main", "root": str(tmp_path / "data_rein")},
        "emergency_script": str(tmp_path / ".cache/data_rein/backup/rescue.sh"),
        "failsafe_backup_dir": str(tmp_path / ".cache/data_rein/backup/failsafe"),
        "health": {
            "hypr_critical_files": [str(tmp_path / ".config/hypr/hyprland.conf")],
            "waybar_config": str(tmp_path / ".config/waybar/config.jsonc"),
            "hypr_syntax_dirs": [str(tmp_path / ".config/hypr")],
            "essential_packages": [],
        },
    }
    return BackupService(config=cfg)


# ------------------------------------------------------------------- checks
def test_files_check_flags_missing_and_empty(tmp_path):
    svc = _svc(tmp_path)
    hypr = tmp_path / ".config/hypr"
    hypr.mkdir(parents=True)
    conf = hypr / "hyprland.conf"
    conf.write_text("")  # empty -> must fail
    ok, detail = svc._check_files_nonempty([str(conf)])
    assert not ok and "hyprland.conf" in detail
    conf.write_text("monitor=,preferred,auto,1")
    ok, _ = svc._check_files_nonempty([str(conf)])
    assert ok


def test_waybar_jsonc_validation(tmp_path):
    svc = _svc(tmp_path)
    w = tmp_path / "config.jsonc"
    w.write_text('// a comment\n{"height": 30}\n')
    assert svc._check_waybar(str(w))[0] is True
    w.write_text('{"height": 30,,}')
    assert svc._check_waybar(str(w))[0] is False


def test_hypr_syntax_detects_deprecated_rule(tmp_path):
    svc = _svc(tmp_path)
    d = tmp_path / ".config/hypr"
    d.mkdir(parents=True)
    (d / "rules.conf").write_text("windowrulev2 = float, class:foo\n")
    ok, detail = svc._check_hypr_syntax([str(d)])
    assert not ok and "windowrulev2" in detail


# -------------------------------------------------------------------- guard
def _report(ok: bool) -> HealthReport:
    return HealthReport([HealthResult("x", ok, "" if ok else "broken")])


def test_guard_allows_when_healthy(tmp_path, monkeypatch):
    svc = _svc(tmp_path)
    monkeypatch.setattr(svc, "health_check", lambda: _report(True))
    monkeypatch.setattr(svc, "backup_now", lambda: {"ok": True})
    calls = []
    rc = svc.guard("reboot", execute=lambda a: calls.append(a) or 0)
    assert rc == 0 and calls == ["reboot"]


def test_guard_blocks_when_broken(tmp_path, monkeypatch):
    svc = _svc(tmp_path)
    monkeypatch.setattr(svc, "health_check", lambda: _report(False))
    monkeypatch.setattr(svc, "failsafe_backup", lambda: tmp_path / "fs.tar.gz")
    calls = []
    rc = svc.guard("reboot", execute=lambda a: calls.append(a) or 0)
    assert rc == 1 and calls == []  # blocked, power action NEVER ran


def test_guard_force_overrides_block(tmp_path, monkeypatch):
    svc = _svc(tmp_path)
    monkeypatch.setattr(svc, "health_check", lambda: _report(False))
    monkeypatch.setattr(svc, "failsafe_backup", lambda: None)
    calls = []
    rc = svc.guard("reboot", force=True, execute=lambda a: calls.append(a) or 0)
    assert rc == 0 and calls == ["reboot"]


# -------------------------------------------------------- emergency script
def test_emergency_script_is_portable_and_failsafe(tmp_path, monkeypatch):
    svc = _svc(tmp_path, monkeypatch)
    hypr = tmp_path / ".config/hypr"
    hypr.mkdir(parents=True)
    (hypr / "hyprland.conf").write_text("monitor=,preferred,auto,1\n")

    out = svc.generate_emergency_script()
    assert out.exists() and out.stat().st_mode & 0o111  # executable
    body = out.read_text()
    # failsafe contract markers
    assert "--restore" in body and "backup_existing" in body
    assert "rm -rf \"$HOME" not in body  # never nukes home
    # valid bash
    assert subprocess.run(["bash", "-n", str(out)]).returncode == 0


def test_failsafe_backup_writes_archive(tmp_path, monkeypatch):
    svc = _svc(tmp_path, monkeypatch)
    hypr = tmp_path / ".config/hypr"
    hypr.mkdir(parents=True)
    (hypr / "hyprland.conf").write_text("data")
    archive = svc.failsafe_backup()
    assert archive and Path(archive).exists() and str(archive).endswith(".tar.gz")
    assert Path(archive).stat().st_mode & 0o777 == 0o600
    assert Path(archive).parent.stat().st_mode & 0o777 == 0o700


def test_backup_rejects_symlink_source_before_archive_write(tmp_path, monkeypatch) -> None:
    svc = _svc(tmp_path, monkeypatch)
    outside = tmp_path.parent / "outside-secret.txt"
    outside.write_text("secret", encoding="utf-8")
    source = tmp_path / ".config/hypr"
    source.mkdir(parents=True)
    (source / "escape.txt").symlink_to(outside)

    assert svc.failsafe_backup() is None
    assert list((tmp_path / ".cache/data_rein/backup/failsafe").glob("*.tar.gz")) == []


def test_backup_rejects_destination_outside_private_backup_root(
    tmp_path,
    monkeypatch,
) -> None:
    svc = _svc(tmp_path, monkeypatch)
    svc.config["emergency_script"] = str(tmp_path / "public" / "rescue.sh")

    assert svc.generate_emergency_script() is None
    assert not (tmp_path / "public").exists()


# ------------------------------------------------------------------ install
def test_splice_block_is_idempotent():
    text = "# rc\nexport A=1\n"
    once = BackupService._splice_block(text, "mark", "reboot() { :; }")
    twice = BackupService._splice_block(once, "mark", "reboot() { :; }")
    assert once == twice
    assert once.count("# >>> mark >>>") == 1
    assert "reboot() { :; }" in once
