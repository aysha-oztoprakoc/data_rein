from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path

import pytest

from reins.harness import cli, external_io, paths
from reins.harness.skill_registry import SkillRegistryError, canonical_skill_names


REPO_ROOT = Path(__file__).parents[1]
INSTALLER = REPO_ROOT / "scripts" / "install_skills.sh"
SKILL_NAMES = (
    "agy-pon-compliance",
    "data_rein",
    "deep-research-paper",
    "hermes-persona",
    "kad_pon",
    "omarchy-aesthetics",
    "pon_testing_suite",
    "prompt-optimizer",
    "utfpr-tcc-abnt",
)


def _skill_tree(root: Path) -> None:
    skills = root / "skills"
    skills.mkdir(parents=True)
    manifest_rows = "\n".join(f"| `{name}` | test |" for name in SKILL_NAMES)
    _ = (skills / "MANIFEST.md").write_text(
        f"## Registered skills\n\n| Skill | Purpose |\n|---|---|\n{manifest_rows}\n\n## Install\n",
        encoding="utf-8",
    )
    for name in SKILL_NAMES:
        skill = skills / name
        skill.mkdir()
        _ = (skill / "SKILL.md").write_text(
            f"---\nname: {name}\n---\n", encoding="utf-8"
        )


def _run_installer(root: Path, home: Path) -> subprocess.CompletedProcess[str]:
    for parent in (home / ".claude", home / ".agents", home / ".codex"):
        parent.mkdir(parents=True, exist_ok=True)
    (root / ".agents").mkdir(exist_ok=True)
    env = os.environ | {"DATA_REIN_HOME": str(root), "HOME": str(home)}
    return subprocess.run(
        ["bash", str(INSTALLER)], capture_output=True, text=True, env=env, check=False
    )


def test_registry_lists_only_manifest_owned_real_directories(tmp_path: Path) -> None:
    # Given eight real canonical directories and an unrelated direct symlink.
    _skill_tree(tmp_path)
    (tmp_path / "skills" / "foreign").symlink_to(tmp_path / "outside")

    # When the public registry is read, then only the manifest-owned skills are listed.
    assert canonical_skill_names(tmp_path / "skills") == SKILL_NAMES


def test_registry_rejects_manifest_skill_symlink(tmp_path: Path) -> None:
    # Given a manifest entry has been replaced by a symlink outside the canonical tree.
    _skill_tree(tmp_path)
    skill = tmp_path / "skills" / SKILL_NAMES[0]
    (skill / "SKILL.md").unlink()
    skill.rmdir()
    skill.symlink_to(tmp_path / "outside")

    # When the registry is read, then the ownership boundary is rejected.
    with pytest.raises(SkillRegistryError, match="real directory"):
        _ = canonical_skill_names(tmp_path / "skills")


def test_installer_is_idempotent_and_atomically_replaces_wrong_symlink(tmp_path: Path) -> None:
    # Given a wrong symlink occupies one target entry.
    root, home = tmp_path / "repo", tmp_path / "home"
    _skill_tree(root)
    target = home / ".codex" / "skills"
    target.mkdir(parents=True)
    wrong = target / SKILL_NAMES[0]
    wrong.symlink_to(tmp_path / "wrong")

    # When the installer runs twice, then all links point to the canonical real directories.
    first = _run_installer(root, home)
    second = _run_installer(root, home)
    assert first.returncode == second.returncode == 0
    assert tuple(sorted(path.name for path in target.iterdir())) == SKILL_NAMES
    assert wrong.resolve() == (root / "skills" / SKILL_NAMES[0]).resolve()


def test_installer_refuses_real_collision_and_target_root_symlink(tmp_path: Path) -> None:
    # Given one target contains user data and another target root is itself a symlink.
    root, home = tmp_path / "repo", tmp_path / "home"
    _skill_tree(root)
    collision = home / ".codex" / "skills" / SKILL_NAMES[0]
    collision.mkdir(parents=True)
    marker = collision / "owned.txt"
    _ = marker.write_text("preserve", encoding="utf-8")
    (home / ".claude").mkdir(parents=True)
    (home / ".claude" / "skills").symlink_to(tmp_path / "escape")

    # When installation is attempted, then it fails without deleting either boundary.
    result = _run_installer(root, home)
    assert result.returncode != 0
    assert marker.read_text(encoding="utf-8") == "preserve"
    assert (home / ".claude" / "skills").is_symlink()


def test_cli_lists_only_canonical_registry_names(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    # Given
    _skill_tree(tmp_path)
    outside = tmp_path / "outside"
    outside.mkdir()
    _ = (outside / "SKILL.md").write_text("---\nname: foreign\n---\n", encoding="utf-8")
    (tmp_path / "skills" / "foreign").symlink_to(tmp_path / "outside")
    monkeypatch.setattr(paths, "home", lambda: tmp_path)

    # When
    handled = cli.handle(argparse.Namespace(command="skills", subcmd="list"))

    # Then
    assert handled is True
    output = capsys.readouterr().out
    assert tuple(line.strip() for line in output.splitlines()[1:]) == SKILL_NAMES
    assert "foreign" not in output


def test_cli_propagates_installer_nonzero(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    # Given
    monkeypatch.setattr(paths, "home", lambda: tmp_path)

    def fail_installer(
        _command: external_io.Command,
        *,
        check: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        _ = check
        return subprocess.CompletedProcess(["install_skills"], 7)

    monkeypatch.setattr(external_io, "run", fail_installer)

    # When
    handled = cli.handle(argparse.Namespace(command="skills", subcmd="install"))

    # Then
    assert handled is False
    diagnostic = capsys.readouterr().err
    assert diagnostic.startswith("// skill install failed")
    assert len(diagnostic) <= 160


def test_cli_propagates_installer_launch_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    # Given
    monkeypatch.setattr(paths, "home", lambda: tmp_path)

    def fail_installer(
        _command: external_io.Command,
        *,
        check: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        _ = check
        raise OSError("launch refused")

    monkeypatch.setattr(external_io, "run", fail_installer)

    # When
    handled = cli.handle(argparse.Namespace(command="skills", subcmd="install"))

    # Then
    assert handled is False
    diagnostic = capsys.readouterr().err
    assert diagnostic.startswith("// skill install failed")
    assert len(diagnostic) <= 160
