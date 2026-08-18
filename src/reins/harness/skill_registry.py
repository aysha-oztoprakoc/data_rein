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


def _manifest_names(skills_root: Path) -> tuple[list[str], list[str]]:
    manifest = skills_root / "MANIFEST.md"
    lines = manifest.read_text(encoding="utf-8").splitlines()
    core_names: list[str] = []
    extended_names: list[str] = []
    
    has_subsections = any(line.startswith("## Core Skills") or line.startswith("## Extended Skills") for line in lines)
    current_section = None
    for line in lines:
        if line.startswith("## Core Skills"):
            current_section = "core"
            continue
        elif line.startswith("## Extended Skills"):
            current_section = "extended"
            continue
        elif line.startswith("## Registered skills") or (not has_subsections and line.startswith("## ")):
            current_section = "core"
            continue
        elif line.startswith("## "):
            current_section = None
            continue
            
        if current_section:
            match = _MANIFEST_ROW.match(line)
            if match:
                if current_section == "core":
                    core_names.append(match.group("name"))
                elif current_section == "extended":
                    extended_names.append(match.group("name"))
                    
    # 'extended-skills-index' is not in manifest explicitly as it's an auto index, 
    # but we must account for it if it exists.
    if (skills_root / "core" / "extended-skills-index").is_dir() and "extended-skills-index" not in core_names:
        core_names.append("extended-skills-index")

    return sorted(core_names), sorted(extended_names)


def canonical_skill_names(skills_root: Path | None = None, include_extended: bool = True) -> tuple[str, ...]:
    root = (skills_root or _default_skills_root()).absolute()
    if root.is_symlink() or not root.is_dir():
        raise SkillRegistryError(message=f"canonical skills root must be a real directory: {root}")
        
    core_names, ext_names = _manifest_names(root)
    
    def verify_skills(names: list[str], subdir: str):
        for name in names:
            if (root / subdir).is_dir():
                skill = root / subdir / name
            else:
                skill = root / name
            if skill.is_symlink() or not skill.is_dir():
                raise SkillRegistryError(message=f"canonical skill must be a real directory: {skill}")
            if not (skill / "SKILL.md").is_file():
                raise SkillRegistryError(message=f"canonical skill is missing SKILL.md: {skill}")

    verify_skills(core_names, "core")
    verify_skills(ext_names, "extended")

    if include_extended:
        return tuple(sorted(core_names + ext_names))
    return tuple(sorted(core_names))


def canonical_skills(skills_root: Path | None = None, include_extended: bool = True) -> tuple[CanonicalSkill, ...]:
    root = (skills_root or _default_skills_root()).absolute()
    core_names, ext_names = _manifest_names(root)
    
    skills: list[CanonicalSkill] = []
    
    def load_skills(names: list[str], subdir: str):
        for name in names:
            if (root / subdir).is_dir():
                path = root / subdir / name
            else:
                path = root / name
            description = ""
            for line in (path / "SKILL.md").read_text(encoding="utf-8").splitlines():
                if line.startswith("description:"):
                    description = line.split(":", 1)[1].strip().strip('"').strip("'")
                    break
            skills.append(CanonicalSkill(name=name, path=path, description=description))
            
    load_skills(core_names, "core")
    if include_extended:
        load_skills(ext_names, "extended")
        
    return tuple(sorted(skills, key=lambda s: s.name))


def main(argv: list[str] | None = None) -> int:
    arguments = sys.argv[1:] if argv is None else argv
    root = Path(arguments[0]) if arguments else _default_skills_root()
    # If the first arg after root is --core-only, we only return core
    include_extended = True
    if len(arguments) > 1 and arguments[1] == "--core-only":
        include_extended = False

    try:
        names = canonical_skill_names(root, include_extended=include_extended)
    except (OSError, SkillRegistryError) as error:
        print(f"skill registry error: {error}", file=sys.stderr)
        return 2
    print("\n".join(names))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
