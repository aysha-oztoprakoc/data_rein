#!/usr/bin/env python3
"""Vendor the Trail of Bits /skills repo into the canonical data_rein skill tree.

Flattens `plugins/<plugin>/skills/<skill>/` into `skills/<skill>/`, merges plugin-level
shared resources (agents/, prompts/, scripts/, hooks/, commands/, references/,
workflows/, evals/, tests/) into each skill so every skill is self-contained, patches
internal path references (`plugins/<plugin>/...` and `{baseDir}` -> local paths), and
registers every imported skill in `skills/MANIFEST.md` (sorted, header/footer preserved).

Preserves the original Trail of Bits language — this importer performs NO content
rewrite. Only path-reference metadata is adjusted.

Source of truth: third_party/skills/trailofbits-skills/ (provenance in SBOM.json).
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "third_party" / "skills" / "trailofbits-skills" / "plugins"
DST = REPO_ROOT / "skills"

# Plugin-level support dirs merged (union) into every skill of that plugin.
SHARED_DIRS = {
    "agents",
    "prompts",
    "scripts",
    "hooks",
    "commands",
    "references",
    "workflows",
    "evals",
    "tests",
    "resources",
    "assets",
    "ct_analyzer",
    "scanner",
}
# Plugin-level files also merged in (used by skills, e.g. README.md, scripts).
SHARED_FILES = {"README.md"}

_MANIFEST_ROW = re.compile(r"^(\|\s*`)(?P<name>[a-z0-9][a-z0-9_-]*)(`\s*\|)(?P<purpose>.*\|)?$")
_DESC_LINE = re.compile(r'^\s*description:\s*"?([^"\n]+)?"?$', re.MULTILINE)


def _parse_description(skill_md: str) -> str:
    """Extract a single-line description for a SKILL.md, handling YAML block scalars."""
    match = re.search(r"^description:\s*(>-?|)$.?", skill_md, re.MULTILINE)
    if match:
        # Block scalar: collect following indented lines up to the next key or `---`.
        body = skill_md[match.end():]
        lines: list[str] = []
        for line in body.splitlines():
            if not line.strip():
                continue
            if not line.startswith("  ") and not line.startswith("\t"):
                break
            stripped = line.strip()
            if stripped.startswith("---"):
                break
            lines.append(stripped)
            if len(lines) >= 6:
                break
        if lines:
            return " ".join(lines)
    match = _DESC_LINE.search(skill_md)
    if match:
        return match.group(1).strip().strip("'\"")
    return ""


def _patch_references(plugin: str, text: str) -> str:
    """Rewrite plugin-level and {baseDir} path references to flattened-local paths."""
    # Cross-skill references: plugins/<p>/skills/<sib>/ -> ../<sib>/  (sibling one level up).
    text = text.replace(f"plugins/{plugin}/skills/", "../")
    # Plugin-level resources are now merged into the skill dir.
    text = text.replace(f"plugins/{plugin}/", "")
    # {baseDir} resolves to the skill dir in Claude Code; point to local path directly.
    text = text.replace("{baseDir}/", "")
    text = text.replace("{baseDir}", "")
    return text


def _merge_shared(plugin_dir: Path, skill_dst: Path) -> None:
    """Union-copy plugin-level shared resources into a skill dir (never overwrites)."""
    skill_dst.mkdir(parents=True, exist_ok=True)
    for dirname in SHARED_DIRS:
        src = plugin_dir / dirname
        if src.is_dir():
            shutil.copytree(src, skill_dst / dirname, dirs_exist_ok=True)
    for fname in SHARED_FILES:
        src = plugin_dir / fname
        dst = skill_dst / fname
        if src.is_file() and not dst.exists():
            shutil.copy2(src, dst)


def _flatten_skill(plugin: str, skill_dir: Path, plugin_dir: Path) -> Path:
    """Copy one skill into the canonical tree and patch its references."""
    skill_name = skill_dir.name
    dst = DST / skill_name
    if dst.exists():
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)

    # 1. Copy the skill dir itself (its own subdirs/workflows/references).
    shutil.copytree(skill_dir, dst)

    # 2. Merge plugin-level shared resources so the skill is self-contained.
    _merge_shared(plugin_dir, dst)

    # 3. Patch path references in every text file under the skill dir.
    for f in dst.rglob("*"):
        if f.is_file() and f.suffix.lower() in {".md", ".markdown", ".txt", ".json", ".yaml", ".yml"}:
            try:
                data = f.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            patched = _patch_references(plugin, data)
            if patched != data:
                f.write_text(patched, encoding="utf-8")

    return dst


def _synthesize_insecure_defaults() -> Path:
    """insecure-defaults is command-based (no skills/). Wrap it as a skill."""
    plugin_dir = SRC / "insecure-defaults"
    dst = DST / "insecure-defaults"
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True, exist_ok=True)
    _merge_shared(plugin_dir, dst)
    audit = plugin_dir / "commands" / "audit.md"
    body = audit.read_text(encoding="utf-8") if audit.exists() else ""
    heading = "## Audit workflow"
    if body and not body.startswith("##"):
        # If audit.md already has its own heading, avoid duplicating.
        heading = "## Execution"
    frontmatter = (
        "---\n"
        "name: insecure-defaults\n"
        "description: >-\n"
        "  Audits a project for insecure default configurations (SAST/networking/cloud\n"
        "  defaults), driven by the upstream Trail of Bits audit workflow in commands/audit.md\n"
        "  with its references/ and workflows/ resources. Preserved verbatim from upstream.\n"
        "allowed-tools: Bash Read Write Grep Glob\n"
        "---\n\n"
        f"# insecure-defaults\n\n{heading}\n\n{body}\n"
    )
    (dst / "SKILL.md").write_text(frontmatter, encoding="utf-8")
    _patch_skill_files(dst, "insecure-defaults")
    return dst


def _patch_skill_files(dst: Path, plugin: str) -> None:
    for f in dst.rglob("*"):
        if f.is_file() and f.suffix.lower() in {".md", ".markdown", ".txt", ".json", ".yaml", ".yml"}:
            try:
                data = f.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            patched = _patch_references(plugin, data)
            if patched != data:
                f.write_text(patched, encoding="utf-8")


def _imported_skills() -> list[tuple[str, str]]:
    """Return (name, description) for every skill to import, in stable order."""
    entries: list[tuple[str, str]] = []
    for plugin_dir in sorted(SRC.iterdir()):
        if not plugin_dir.is_dir():
            continue
        plugin = plugin_dir.name
        skills_root = plugin_dir / "skills"
        if skills_root.is_dir():
            for skill_dir in sorted(skills_root.iterdir()):
                skill_md = skill_dir / "SKILL.md"
                if skill_dir.is_dir() and skill_md.is_file():
                    _ = _flatten_skill(plugin, skill_dir, plugin_dir)
                    entries.append((skill_dir.name, _parse_description(skill_md.read_text(encoding="utf-8"))))
    # insecure-defaults has no SKILL.md skills; synthesize it.
    synth_path = _synthesize_insecure_defaults()
    entries.append(("insecure-defaults", _parse_description(
        (synth_path / "SKILL.md").read_text(encoding="utf-8")
    )))
    return entries


def _manifest(name_to_purpose: dict[str, str]) -> str:
    """Rebuild MANIFEST.md preserving header/footer prose and existing rows, inserting new ones sorted."""
    manifest = DST / "MANIFEST.md"
    lines = manifest.read_text(encoding="utf-8").splitlines()

    header: list[str] = []
    rows: list[str] = []
    footer: list[str] = []
    section = "header"
    table_start = table_end = None
    for i, line in enumerate(lines):
        if line == "## Registered skills":
            section = "table"
            header.append(line)
            continue
        if section == "table":
            if line.startswith("## "):  # next section starts the footer
                table_end = i
                section = "footer"
            elif re.match(r"^\|\s*`", line):
                rows.append(line)
                continue
            else:
                rows.append(line)  # table header separator etc.
        if section == "header":
            header.append(line)
        if section == "footer":
            footer.append(line)

    # Parse existing name->row (keep the purpose text verbatim).
    by_name: dict[str, str] = {}
    for row in rows:
        m = _MANIFEST_ROW.match(row.strip())
        if m:
            by_name[m.group("name")] = row.strip()
    # Merge newly imported skills (only add, never overwrite existing curated rows).
    for name, purpose in name_to_purpose.items():
        if name in by_name:
            continue
        by_name[name] = f"| `{name}` | {purpose or 'Imported Trail of Bits security skill.'} |"

    # Rebuild the table (header separator + sorted rows).
    table = ["| Skill | Purpose |", "|---|---|"]
    for name in sorted(by_name):
        table.append(by_name[name])

    # Update the count line: "Exactly the N registered entries below are canonical."
    total = len(by_name)
    header = [re.sub(r"Exactly the \d+ registered entries", f"Exactly the {total} registered entries", h)
              for h in header]

    return "\n".join(header + [""] + table + [""] + footer)


def main() -> int:
    if not SRC.is_dir():
        print(f"error: source not found: {SRC}", file=sys.stderr)
        print("run once: git clone --depth 1 https://github.com/trailofbits/skills"
              " third_party/skills/trailofbits-skills", file=sys.stderr)
        return 1

    entries = _imported_skills()
    name_to_purpose = dict(entries)
    manifest_out = _manifest(name_to_purpose)
    (DST / "MANIFEST.md").write_text(manifest_out, encoding="utf-8")

    imported_in_purpose = sorted(n for n in name_to_purpose.keys())
    print(f"Imported {len(entries)} Trail of Bits skills into {DST}")
    for name in imported_in_purpose:
        print(f"  - {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())