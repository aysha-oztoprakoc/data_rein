#!/bin/bash
# Helper script to cache sudo credentials in memory and launch commands as the current user
PASS=$(/home/amdy/data_rein/.venv/bin/python -c 'import sys; sys.path.append("/home/amdy/data_rein"); from scripts.get_secrets import get_secret; print(get_secret("SUDO_PASS"))')
echo "$PASS" | sudo -S -v
exec "$@"
