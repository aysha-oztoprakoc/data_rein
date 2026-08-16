## What does this PR do?
<!-- One paragraph describing the change and the problem it solves. -->

## Related issue(s)
Closes #<!-- issue number -->

## Type of change
- [ ] Bug fix
- [ ] New feature
- [ ] Refactor / cleanup (no behaviour change)
- [ ] CI / tooling / packaging
- [ ] Docs

## PON / local-first compliance
The harness mandates Notification-Oriented Paradigm (zero polling) and
local-first routing. If this PR touches runtime behaviour, address the law(s)
it implicates:
- [ ] No polling loops (`while True`, spin-wait `sleep`) added anywhere.
- [ ] Failures degrade gracefully (log to the task trail) rather than exposing
      secrets or crashing the caller.
- [ ] Any new model/provider path routes through `ModelRouter` and never
      silently falls back to a cloud provider unless explicitly authorized.
- [ ] Shared state still lives only in the single monolith Wiki DB + task trail.

## Install / packaging
- [ ] Any new runtime import is declared in `pyproject.toml` dependencies (or a
      relevant extra), not just present in the working venv.
- [ ] `uv lock --check` is clean (ran `uv lock` if dependencies changed).
- [ ] sdist/wheel remain lean (`uv build` — no vendored data trees).

## Verification
- [ ] `uv run ruff check src tests scripts` passes
- [ ] `uv run pytest tests/ -q` passes
- [ ] `uv run bandit -r src -q -ll` passes
- [ ] CI basedpyright ratchet stays green
      (`uv run basedpyright --baselinefile .basedpyright-baseline.txt`)
- [ ] If API/behaviour changed: documented in `README.md` / `AGENTS.md` / wiki

## Definition of done
- [ ] Tests added or updated for the change
- [ ] Reviewed against this checklist
- [ ] No unrelated files touched (unrelated dirty work left out of this PR)