#!/usr/bin/env bash
set -euo pipefail

SSH_HOST="${SSH_HOST:-192.168.0.2}"
SSH_USER="${SSH_USER:-tell}"
SSH_FINGERPRINT="${SSH_FINGERPRINT:-}"
SSH_DIR="${SSH_DIR:-$HOME/.ssh}"
PRIVATE_KEY="$SSH_DIR/id_ed25519"
KNOWN_HOSTS="$SSH_DIR/known_hosts"

if [[ ! "$SSH_FINGERPRINT" =~ ^SHA256:[A-Za-z0-9+/]+={0,2}$ ]]; then
  echo "ERROR: SSH_FINGERPRINT must be the trusted SHA256 Ed25519 host fingerprint." >&2
  exit 2
fi

mkdir -p "$SSH_DIR"
chmod 700 "$SSH_DIR"
if [ ! -f "$PRIVATE_KEY" ]; then
  ssh-keygen -t ed25519 -f "$PRIVATE_KEY" -N "" -q
fi

scan="$(mktemp --tmpdir="$SSH_DIR" .known_hosts.scan.XXXXXX)"
candidate="$(mktemp --tmpdir="$SSH_DIR" .known_hosts.next.XXXXXX)"
cleanup() {
  [ ! -e "$scan" ] || unlink "$scan"
  [ ! -e "$candidate" ] || unlink "$candidate"
}
trap cleanup EXIT

ssh-keyscan -T 5 -t ed25519 "$SSH_HOST" > "$scan" 2>/dev/null
actual="$(ssh-keygen -lf "$scan" -E sha256 | awk 'NR == 1 {print $2}')"
if [ "$actual" != "$SSH_FINGERPRINT" ]; then
  echo "ERROR: SSH host fingerprint mismatch for $SSH_HOST (got ${actual:-none})." >&2
  exit 2
fi

if [ -f "$KNOWN_HOSTS" ]; then
  cp "$KNOWN_HOSTS" "$candidate"
fi
ssh-keygen -R "$SSH_HOST" -f "$candidate" >/dev/null 2>&1 || true
cat "$scan" >> "$candidate"
chmod 600 "$candidate"
mv -f "$candidate" "$KNOWN_HOSTS"

destination="$SSH_USER@$SSH_HOST"
ssh_options=(-o BatchMode=yes -o StrictHostKeyChecking=yes -o "UserKnownHostsFile=$KNOWN_HOSTS")
if ssh "${ssh_options[@]}" -i "$PRIVATE_KEY" "$destination" true; then
  echo "SSH setup to $destination complete."
  exit 0
fi

if [ ! -t 0 ]; then
  echo "ERROR: SSH key enrollment required; rerun tools/setup_ssh.sh in an interactive TTY." >&2
  exit 2
fi

ssh-copy-id -i "$PRIVATE_KEY.pub" -o StrictHostKeyChecking=yes \
  -o "UserKnownHostsFile=$KNOWN_HOSTS" "$destination"
ssh "${ssh_options[@]}" -i "$PRIVATE_KEY" "$destination" true
echo "SSH setup to $destination complete."
