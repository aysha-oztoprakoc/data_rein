#!/bin/bash
set -e

SECRETS_FILE="$HOME/data_rein/config/.secrets.env"

if [ -f "$SECRETS_FILE" ]; then
    source "$SECRETS_FILE"
fi

if [ -z "$SUDO_PASS" ]; then
    echo "Error: SUDO_PASS not found in $SECRETS_FILE"
    exit 1
fi

echo "$SUDO_PASS" | sudo -S "$@"
