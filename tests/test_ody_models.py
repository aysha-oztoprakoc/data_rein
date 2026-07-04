"""
Odysseus deployment checks. Like test_health_sanity, these assert on live
artifacts produced by provisioning (auth, model registry, migrated memories) and
so degrade to `skip` when those are absent — the suite stays hermetic and green on
a fresh checkout, but still verifies a provisioned host.
"""

import json

from conftest import require


def test_ody_auth_config():
    """The default factory user must be deleted and data-ody made sole admin."""
    auth_file = require("~/data_rein/odysseus/data/auth.json", "Odysseus not provisioned")
    with open(auth_file, "r") as f:
        auth_data = json.load(f)
    users = auth_data.get("users", {})
    assert "data-ody" in users, "Admin user data-ody was not created"
    assert users["data-ody"]["is_admin"] is True, "data-ody is not an admin"
    assert len(users) == 1, "Factory defaults were not deleted"


def test_ody_dockerfile_python_version():
    """Odysseus must build on python:3.12-slim (3.14 base was broken)."""
    dockerfile = require("~/data_rein/odysseus/Dockerfile", "Odysseus clone not present")
    with open(dockerfile, "r") as f:
        content = f.read()
    assert "python:3.12-slim" in content, "Dockerfile is not using the patched python 3.12-slim"
    assert "python:3.14-slim" not in content, "Dockerfile still references the broken python 3.14"


def test_model_registry_populated():
    """When getinfo/sys_profiler has run, the registry maps VRAM-fitting local models for amdy."""
    from reins.harness import paths

    registry_file = require(
        str(paths.model_registry()),
        "model registry not generated (run `getinfo` / sys_profiler on this host)",
    )
    with open(registry_file, "r") as f:
        registry = json.load(f)
    assert "amdy" in registry, "Local node amdy missing from registry"
    amdy = registry["amdy"]
    # New getinfo format exposes `models_fit`; tolerate the legacy `models` key.
    fit = amdy.get("models_fit") or amdy.get("models") or []
    assert len(fit) > 0, "No VRAM-fitting models detected for amdy"


def test_memory_ingestion():
    """When memories were migrated to Odysseus, harness-specific ones must be present."""
    memory_file = require("~/data_rein/odysseus/data/memory.json", "Odysseus memories not migrated")
    with open(memory_file, "r") as f:
        memories = json.load(f)
    assert len(memories) > 0, "No memories were found"
    assert any(
        "data_rein" in m.get("text", "") or "PON" in m.get("text", "") for m in memories
    ), "Harness-specific memories were not found"
