# Project Brief — 2026-08-13

`data_rein` is a local-first universal harness for shared knowledge, task state,
and model routing across Codex, Claude Code, OpenCode, Antigravity, Hermes, and
Odysseus.

## Architecture

```text
clients / CLI / MCP
        │
        ├── canonical skills/ + manifest registry
        ├── Task Trail (SQLite WAL)
        ├── WikiDB (knowledge_base/wiki.db)
        └── ModelRouter
               ├── local_text: Ollama, amdy ↔ tell
               ├── cloud_text: explicit gated request only
               └── image: ComfyUI, fail closed
```

The operating laws are: notification-oriented execution (no polling), strict
amdy execution/tell durable-state separation, graceful degradation, one canonical
Wiki DB, and explicit cloud authorization.

## Operator commands

```bash
reins wiki stats
reins trail list
reins skills list
reins skills install
reins local status
reins run <category> "<prompt>"
reins mcp
nix --extra-experimental-features "nix-command flakes" develop
```

Use `uv run` for Python commands. The bare system interpreter may not contain the
locked dependencies. Do not use `path:.` to evaluate an untracked flake from this
runtime-heavy checkout; it includes ignored model and virtual-environment trees.
Use the normal Git-backed flake after the Nix files are tracked.

## Canonical skills

Exactly these seven manifest-backed skills are canonical:

- `data_rein`
- `agy-pon-compliance`
- `kad_pon`
- `hermes-persona`
- `omarchy-aesthetics`
- `pon_testing_suite`
- `prompt-optimizer`

Edit only `skills/<name>/SKILL.md`. `reins skills install` creates environment
symlinks; it does not copy or generate skill content.

## Security posture

- Ordinary routing is local-only; a cloud provider requires an explicit
  `route_cloud` / `escalate_cloud` authorization path.
- HTTP MCP requires bearer authentication and defaults to loopback; non-loopback
  binding is rejected unless an operator explicitly selects remote mode. It serves
  24 tools after authentication.
- Secrets are handled through the encrypted vault; token material is not written
  as plaintext. A successful vault mutation retains the exact previous ciphertext
  as private `.secrets.enc.bak` and restores it automatically if active replacement
  fails; a dual failure reports that the encrypted backup was retained.
- Active Python sources are structurally barred from `os.system`, `shell=True`, and
  string subprocess commands. The legacy runtime dependency installer was removed;
  encryption uses the locked `cryptography` dependency directly.
- Backup/archive outputs use constrained permissions; Comfy/model installation
  fails closed.

The evidence-backed audit, caveats, and residual risk are in
`knowledge_base/SECURITY_AUDIT_2026_08_13.md`.
