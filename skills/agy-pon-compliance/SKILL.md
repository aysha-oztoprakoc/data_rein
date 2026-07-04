---
name: agy-pon-compliance
description: "Notification-Oriented Paradigm (PON) architectural law — zero polling, amdy/tell split, FBE, graceful degradation. Load before writing any harness code."
tags: "architecture, pon, compliance, rules, harness"
---

# AGY-PON Compliance

Any code or script you write under the `data_rein` harness MUST obey the
Notification-Oriented Paradigm. This skill is the enforcement checklist; the full
law is section 4 of `knowledge_base/PRIME_DIRECTIVE.md`.

## The four rules
1. **Zero polling.** No `while True`, no `time.sleep()` spin-waits, no active
   status checks. Wait via blocking I/O, reactive pipes, or MQTT subscription.
   Idle CPU must be ~0%.
2. **Strict amdy/tell split.** `amdy` executes (Methods); durable state lives on
   `tell`. Execution nodes hold no local state and wake only when notified.
3. **FBE abstraction.** Model data/logic as Fact Base Elements. Entities never
   chain-call each other — they change Attributes, which fire notifications to
   Rules and Methods reactively.
4. **Graceful degradation.** Wrap every execution frame so failure degrades (to a
   lesser model/node) instead of crashing, and log the failure to the Task Trail.

## Deeper knowledge (in the monolith wiki)
```bash
reins wiki search "PON notification oriented paradigm"
reins wiki search "FBE fact base element"
```
Source docs: `knowledge_base/architecture/agy-pon.xml`, `knowledge_base/pon/**`.

## Before commit / deploy
Run the harness tests (`.venv/bin/pytest -q`). Code that does not pass PON and
safety checks must not be versioned or deployed.
