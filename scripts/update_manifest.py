from pathlib import Path

skills_root = Path('/home/amdy/data_rein/skills')
manifest_file = skills_root / 'MANIFEST.md'

real_dirs = sorted([d.name for d in skills_root.iterdir() if d.is_dir() and not d.is_symlink()])

skills_info = []
for name in real_dirs:
    skill_md = skills_root / name / 'SKILL.md'
    desc = ''
    if skill_md.is_file():
        for line in skill_md.read_text(encoding='utf-8').splitlines():
            if line.strip().startswith('description:'):
                desc = line.split(':', 1)[1].strip().strip('\"\'')
                break
    skills_info.append((name, desc))

header = f"""# // data_rein Harness Skills — Canonical Registry

This directory is the **single source of truth** for every skill available to
agents operating under the `data_rein` harness.

**Prime Agent Philosophy (Skills are Executable):**
Skills are not just passive Markdown files to stuff into context windows. Under the RLM paradigm, skills are executable Python modules, prompts, or REPL hooks that the agent invokes programmatically. The YAML frontmatter in `SKILL.md` provides discovery and routing context.

Exactly the {len(skills_info)} registered entries below are canonical. Each is a real,
non-symlink directory containing a `SKILL.md` and their respective programmatic hooks.

## Registered skills

| Skill | Purpose |
|---|---|
"""

rows = []
for name, desc in skills_info:
    clean_desc = desc.replace('|', '/').replace('\n', ' ')
    rows.append(f"| `{name}` | {clean_desc} |")

footer = """

## How each environment picks these up

All environments share these canonical skills via `scripts/install_skills.sh`
(or `reins skills install`), which links each skill into the location that
environment scans:

| Environment | Skills location it scans |
|---|---|
| Odysseus | `odysseus/data/skills/` |
| Claude Code | `~/.claude/skills/` |
| Antigravity | `.agents/skills/` |
| Codex | `~/.codex/skills/` |
| Odysseus Codex plugin | `odysseus/integrations/codex/skills/` |
| VS Code | integrated terminal -> `reins skills list` |

The installer symlinks (never copies) so there is exactly one editable source:
this directory. Re-run it any time; it is idempotent and PON-compliant.

## Discover from any shell
```bash
reins skills list            # list registered skills
reins skills install         # link them into every environment
reins wiki search "<topic>"  # skills are also ingested into the wiki
```
"""

manifest_file.write_text(header + '\n'.join(rows) + footer, encoding='utf-8')
print(f"Successfully wrote {len(skills_info)} skills to {manifest_file}")
