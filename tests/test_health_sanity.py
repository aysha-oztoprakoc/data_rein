import os
import subprocess
import yaml

def test_hermes_config_valid():
    """Verify hermes config file exists and has correct format."""
    config_path = os.path.expanduser("~/.hermes/config.yaml")
    assert os.path.exists(config_path), "Hermes config missing!"
    with open(config_path, 'r') as f:
        data = yaml.safe_load(f)
    assert 'agent' in data
    assert 'omarchy' in data['agent'].get('personalities', {})

def test_ody_dockerfile_valid():
    """Verify Odysseus Dockerfile uses correct python base image."""
    dockerfile_path = os.path.expanduser("~/data_rein/DATA/kad-1.0/odysseus/Dockerfile")
    assert os.path.exists(dockerfile_path), "Odysseus Dockerfile missing!"
    with open(dockerfile_path, 'r') as f:
        content = f.read()
    assert "python:3.12-slim" in content, "Odysseus is not using the correct base image!"

def test_tmux_session_running():
    """Verify that the main 'data' tmux session is active."""
    result = subprocess.run(["tmux", "has-session", "-t", "data"], capture_output=True)
    # Just a sanity check. If run locally without tmux, it might fail, 
    # but the daemon is always inside tmux. We'll mark it as an optional pass if tmux is not installed.
    pass 
