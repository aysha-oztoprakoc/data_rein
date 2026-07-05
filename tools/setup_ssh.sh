#!/bin/bash
set -e

# Generate SSH key if it doesn't exist
if [ ! -f ~/.ssh/id_ed25519 ]; then
    ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -q
fi

# Make sure sshpass is installed using our sudo executor
if ! command -v sshpass &> /dev/null; then
    ~/data_rein/scripts/sudo_executor.sh pacman -S --noconfirm sshpass
fi

# Copy key to tell (SUDO_PASS loaded from vault, never hard-coded)
SUDO_PASS=$(/home/amdy/data_rein/.venv/bin/python -c 'import sys; sys.path.append("/home/amdy/data_rein"); from scripts.get_secrets import get_secret; print(get_secret("SUDO_PASS"))')
sshpass -p "$SUDO_PASS" ssh-copy-id -o StrictHostKeyChecking=no -i ~/.ssh/id_ed25519.pub tell@192.168.0.2

echo "SSH setup to tell complete."
