from __future__ import annotations

import re
import shutil
from pathlib import Path

def main() -> None:
    src_root = Path("/tmp/mattpocock_skills/skills")
    dst_root = Path("/home/amdy/data_rein/skills")

    # 1. Copy all skills from mattpocock if not already present
    for skill_file in src_root.glob("*/*/SKILL.md"):
        skill_dir = skill_file.parent
        name = skill_dir.name
        target_dir = dst_root / name
        if not target_dir.exists():
            shutil.copytree(skill_dir, target_dir)
            print(f"Copied new skill: {name}")
        else:
            print(f"Skill already exists: {name}")

    # 2. Extract description for each skill in dst_root
    entries: list[tuple[str, str]] = []
    for sdir in sorted(dst_root.iterdir()):
        if not sdir.is_dir() or sdir.is_symlink() or sdir.name.startswith("."):
            continue
        skill_md = sdir / "SKILL.md"
        if not skill_md.exists():
            print(f"WARNING: Missing SKILL.md in {sdir}")
            continue

        content = skill_md.read_text(encoding="utf-8", errors="replace")
        desc = ""
        m_desc = re.search(r"description:\s*([^\n]+)", content)
        if m_desc:
            desc = m_desc.group(1).strip().strip("'\"")
        else:
            for line in content.splitlines():
                line_s = line.strip()
                if line_s and not line_s.startswith("#") and not line_s.startswith("---"):
                    desc = line_s
                    break
        if not desc:
            desc = f"Skill for {sdir.name}"
        desc = desc.replace("|", "-").replace("\n", " ").strip()
        if len(desc) > 120:
            desc = desc[:117] + "..."
        entries.append((sdir.name, desc))

    print(f"Total canonical skills: {len(entries)}")

    # 3. Generate updated MANIFEST.md
    manifest_path = dst_root / "MANIFEST.md"
    lines = [
        "# // data_rein Harness Skills — Canonical Registry",
        "",
        "This directory is the **single source of truth** for every skill available to",
        "agents operating under the `data_rein` harness.",
        "",
        "**Prime Agent Philosophy (Skills are Executable):**",
        "Skills are not just passive Markdown files to stuff into context windows. Under the RLM paradigm, skills are executable Python modules, prompts, or REPL hooks that the agent invokes programmatically. The YAML frontmatter in `SKILL.md` provides discovery and routing context.",
        "",
        f"Exactly the {len(entries)} registered entries below are canonical. Each is a real,",
        "non-symlink directory containing a `SKILL.md` and their respective programmatic hooks.",
        "",
        "## Registered skills",
        "",
        "| Skill | Purpose |",
        "|---|---|",
    ]
    for name, desc in entries:
        lines.append(f"| `{name}` | {desc} |")

    lines.extend([
        "",
        "## How each environment picks these up",
        "",
        "All environments share these canonical skills via `scripts/install_skills.sh`",
        "(or `reins skills install`), which links each skill into the location that",
        "environment scans:",
        "",
        "| Environment | Skills location it scans |",
        "|---|---|",
        "| Odysseus | `odysseus/data/skills/` |",
        "| Claude Code | `~/.claude/skills/` |",
        "| Antigravity | `.agents/skills/` |",
        "| Codex | `~/.codex/skills/` |",
        "| Odysseus Codex plugin | `odysseus/integrations/codex/skills/` |",
        "| VS Code | integrated terminal -> `reins skills list` |",
        "",
        "The installer symlinks (never copies) so there is exactly one editable source:",
        "this directory. Re-run it any time; it is idempotent and PON-compliant.",
        "",
        "## Discover from any shell",
        "```bash",
        "reins skills list            # list registered skills",
        "reins skills install         # link them into every environment",
        "reins wiki search \"<topic>\"  # skills are also ingested into the wiki",
        "```",
        ""
    ])

    manifest_path.write_text("\n".join(lines), encoding="utf-8")
    print("Updated MANIFEST.md successfully.")

if __name__ == "__main__":
    main()
