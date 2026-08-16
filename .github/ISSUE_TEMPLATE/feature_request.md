---
name: Feature request
about: Propose a new capability or improvement for the data_rein harness
title: "[feature] "
labels: enhancement
assignees: ""
---

## What & why
<!-- What should the harness be able to do, and why does it matter? -->

## Proposed surface
<!-- Sketch the user-facing and/or Python surface. Prefer concrete shapes: -->
- CLI command / flag: `reins ...`
- Python API / module:
- Config file / wiki page:

## PON / local-first fit
The harness is PON (zero polling, event-driven, strict amdy(exec)/tell(state)
split) and local-first. Address the relevant laws explicitly:
- How does this stay **event-driven** (no `while True`, no polling `sleep`)?
- Where does it degrade **gracefully** instead of crashing?
- Does it touch shared state (wiki / task trail), and does it route through the
  existing model router rather than hard-coding a provider?

## Alternatives considered
<!-- What else satisfied the need, and why is this the better path? -->

## Effort guess (optional)
<!-- M = days, L = weeks. Just a heuristic, not a commitment. -->

## Definition of done
- [ ] Behaviour is documented in `README.md` / `AGENTS.md` and the wiki.
- [ ] Uses the single monolith Wiki DB and the shared task trail.
- [ ] `uv run ruff check src tests scripts`, `uv run pytest tests/ -q` and the CI gate stay green.