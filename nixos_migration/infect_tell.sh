#!/usr/bin/env bash
set -e

# This script runs ON THE TELL NODE to infect Debian 13 and replace it with NixOS

echo "[*] Downloading nixos-infect..."
curl https://raw.githubusercontent.com/elitak/nixos-infect/master/nixos-infect | PROVIDE_FSTAB=true NIX_CHANNEL=nixos-24.05 bash 2>&1 | tee /tmp/nixos-infect.log

# Note: nixos-infect replaces /etc/nixos/configuration.nix with its own generated one
# We will overwrite it with our custom one that we scp'd over before running this,
# OR we let nixos-infect run, and it uses the config we placed in /etc/nixos/configuration.nix
# if we place it there beforehand and modify the script to not overwrite it.
# Actually, the standard way is to just let nixos-infect run.
