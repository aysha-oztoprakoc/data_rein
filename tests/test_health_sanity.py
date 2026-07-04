"""
Environment health checks. These validate the *live* deployment, so they degrade
to `skip` (not `fail`) when their artifact is absent — the suite stays green on a
fresh checkout while still catching regressions on a provisioned host.
(The Dockerfile python-version check lives in test_ody_models.py; not duplicated
here. The dead `test_tmux_session_running` — a bare `pass` — was removed.)
"""

import yaml

from conftest import require


def test_hermes_config_valid():
    """When the live Hermes config exists, it must declare the omarchy personality."""
    config_path = require("~/.hermes/config.yaml", "Hermes not provisioned on this host")
    with open(config_path, "r") as f:
        data = yaml.safe_load(f)
    assert "agent" in data
    assert "omarchy" in data["agent"].get("personalities", {})
