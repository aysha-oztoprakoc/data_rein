from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from typing_extensions import override

_MANIFEST_ROW = re.compile(r"^\|\s*`(?P<name>[a-z0-9][a-z0-9_-]*)`\s*\|")


@dataclass(frozen=True, slots=True)
class SkillRegistryError(ValueError):
    message: str

    @override
    def __str__(self) -> str:
        return self.message


@dataclass(frozen=True, slots=True)
class CanonicalSkill:
    name: str
    path: Path
    description: str


def _default_skills_root() -> Path:
    return Path(__file__).resolve().parents[3] / "skills"


def _manifest_names(skills_root: Path) -> tuple[str, ...]:
    manifest = skills_root / "MANIFEST.md"
    lines = manifest.read_text(encoding="utf-8").splitlines()
    registered = False
    names: list[str] = []
    for line in lines:
        if line == "## Registered skills":
            registered = True
            continue
        if registered and line.startswith("## "):
            break
        match = _MANIFEST_ROW.match(line) if registered else None
        if match is not None:
            names.append(match.group("name"))
    if not names:
        raise SkillRegistryError(message=f"no registered skills in {manifest}")
    if len(names) != len(set(names)):
        raise SkillRegistryError(message=f"duplicate registered skill in {manifest}")
    return tuple(sorted(names))


def canonical_skill_names(skills_root: Path | None = None) -> tuple[str, ...]:
    root = (skills_root or _default_skills_root()).absolute()
    if root.is_symlink() or not root.is_dir():
        raise SkillRegistryError(message=f"canonical skills root must be a real directory: {root}")
    names = _manifest_names(root)
    for name in names:
        skill = root / name
        if skill.is_symlink() or not skill.is_dir():
            raise SkillRegistryError(message=f"canonical skill must be a real directory: {skill}")
        if not (skill / "SKILL.md").is_file():
            raise SkillRegistryError(message=f"canonical skill is missing SKILL.md: {skill}")
    real_directories = tuple(
        sorted(entry.name for entry in root.iterdir() if entry.is_dir() and not entry.is_symlink())
    )
    if real_directories != names:
        raise SkillRegistryError(
            message=(
                "manifest entries do not match canonical real directories: "
                f"{real_directories!r} != {names!r}"
            )
        )
    return names


def canonical_skills(skills_root: Path | None = None) -> tuple[CanonicalSkill, ...]:
    root = (skills_root or _default_skills_root()).absolute()
    skills: list[CanonicalSkill] = []
    for name in canonical_skill_names(root):
        path = root / name
        description = ""
        for line in (path / "SKILL.md").read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("description:"):
                description = line.split(":", 1)[1].strip().strip("'\"")
                break
        skills.append(CanonicalSkill(name=name, path=path, description=description))
    return tuple(skills)


def main(argv: list[str] | None = None) -> int:
    arguments = sys.argv[1:] if argv is None else argv
    root = Path(arguments[0]) if arguments else _default_skills_root()
    try:
        names = canonical_skill_names(root)
    except (OSError, SkillRegistryError) as error:
        print(f"skill registry error: {error}", file=sys.stderr)
        return 2
    print("\n".join(names))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
