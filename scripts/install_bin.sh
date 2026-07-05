#!/usr/bin/env bash
# Make every data_rein command runnable from any shell, without `cd`ing into
# the repo or typing `.venv/bin/<x>` — mirrors scripts/install_skills.sh's
# idempotent-symlink idiom (single editable source, re-run any time).
set -euo pipefail

HOME_DIR="${DATA_REIN_HOME:-$(cd "$(dirname "$0")/.." && pwd)}"
BIN_DIR="$HOME/.local/bin"
mkdir -p "$BIN_DIR"

link() {  # link <target> <name>
  rm -f "$BIN_DIR/$2"
  ln -s "$1" "$BIN_DIR/$2"
  echo "  // linked $2 -> $1"
}

wrapper() {  # wrapper <name> <repo-relative script path>
  cat > "$BIN_DIR/$1" <<EOF
#!/bin/bash
cd "$HOME_DIR" && uv run python "$2" "\$@"
EOF
  chmod +x "$BIN_DIR/$1"
  echo "  // wrote wrapper $1 -> $2"
}

echo "// data_rein bin installer  [home=$HOME_DIR]"

# 1. every real pyproject.toml [project.scripts] console-script the venv
#    installed for real (currently just `reins`) - symlinked directly since
#    its shebang already points at the venv's own python.
link "$HOME_DIR/.venv/bin/reins" "reins"

# 2. custom dashboard/TUI scripts that aren't packaged console-scripts.
#    Add a new `wrapper name path` line here any time a new one is written,
#    then re-run this installer (or `reins bin install`).
wrapper "sofia" "scripts/sofia_protocol.py"

echo "// [OK] bin commands linked into $BIN_DIR"
