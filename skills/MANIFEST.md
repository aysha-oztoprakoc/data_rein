# // data_rein Harness Skills — Canonical Registry

This directory is the **single source of truth** for every skill available to
agents operating under the `data_rein` harness. It replaces the scattered,
duplicated copies that previously lived under `DATA/kad-1.0/odysseus/data/skills/`,
`odysseus/data/skills/`, and `DATA/kad-1.0/.agents/skills/`.

Each skill is a directory containing a `SKILL.md` with YAML frontmatter
(`name`, `description`, `tags`). Skills are lean: their deep knowledge lives in the
monolith wiki (`reins wiki search`) and `knowledge_base/**`, not embedded copies.

## Registered skills

| Skill | Purpose |
|-------|---------|
| `data_rein`          | Universal harness entry skill — mandatory memory sync, wiki DB, model routing. |
| `agy-pon-compliance` | The PON architectural law (zero polling, amdy/tell, FBE, graceful degradation). |
| `kad_pon`            | Concrete C++ PON engine patterns (SharedAttribute, Rules, inotify+MQTT flow). |
| `hermes-persona`     | Assume the Data-Hermes orchestrator persona + mission. |
| `omarchy-aesthetics` | Mandatory Omarchy Cyberpunk aesthetic for all generated output. |
| `pon_testing_suite`  | Security/stability/PON static-analysis gate; wired into `.git/hooks/pre-push`. |

## How each environment picks these up

All environments share these canonical skills via `scripts/install_skills.sh`
(or `reins skills install`), which links each skill into the location that
environment scans:

| Environment  | Skills location it scans                         |
|--------------|--------------------------------------------------|
| Odysseus     | `odysseus/data/skills/` (`SKILLS_DIR = DATA_DIR/skills`) |
| Claude Code  | `~/.claude/skills/`                              |
| Antigravity  | `.agents/skills/`                                |
| Codex        | `odysseus/integrations/codex/skills/`            |
| VS Code      | integrated terminal → `reins skills list`        |

The installer symlinks (never copies) so there is exactly one editable source:
this directory. Re-run it any time; it is idempotent and PON-compliant (runs
on demand, exits).

## Discover from any shell
```bash
reins skills list            # list registered skills
reins skills install         # link them into every environment
reins wiki search "<skill topic>"   # skills are also ingested into the wiki
```
