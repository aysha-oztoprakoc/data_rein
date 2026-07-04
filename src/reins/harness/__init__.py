"""
data_rein Universal Harness core.

This package is the environment-agnostic spine shared by every agent that
operates under the ``data_rein`` harness: Antigravity (data-agy), Hermes
(data-hermes), Odysseus (data-ody), Claude Code, and the VS Code workspace.

It exposes three things that make the harness "universal":

* :mod:`reins.harness.paths`  - one canonical, machine-independent view of
  where everything lives (prime directive, the monolith wiki DB, config).
* :mod:`reins.harness.wiki`   - the single shared monolith Wiki database that
  every environment reads and writes.
* :mod:`reins.harness.models` - a model-agnostic provider router so the same
  task can run on Ollama, Gemini, Claude, or any OpenAI-compatible backend.
"""

from reins.harness import paths

__all__ = ["paths"]
