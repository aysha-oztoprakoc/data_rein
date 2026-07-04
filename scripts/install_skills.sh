#!/usr/bin/env bash
# Link the canonical data_rein harness skills into every environment that scans
# for skills. Idempotent, PON-compliant (runs on demand, exits). Symlinks only,
# so `skills/` stays the single editable source of truth.
set -euo pipefail

HOME_DIR="${DATA_REIN_HOME:-$(cd "$(dirname "$0")/.." && pwd)}"
CANON="$HOME_DIR/skills"

# name -> absolute canonical skill dir (skip non-skill entries like MANIFEST.md)
mapfile -t SKILLS < <(find "$CANON" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort)

# Target skill roots per environment. Missing parents are created; environments
# whose parent dir does not exist (e.g. no ~/.claude) are skipped gracefully.
TARGETS=(
  "$HOME_DIR/odysseus/data/skills"                       # Odysseus (SKILLS_DIR)
  "$HOME/.claude/skills"                                 # Claude Code
  "$HOME_DIR/.agents/skills"                             # Antigravity
  "$HOME_DIR/odysseus/integrations/codex/skills"         # Codex
)

link_into() {
  local root="$1"
  local parent; parent="$(dirname "$root")"
  # Only install where the environment itself exists (parent present).
  if [ ! -d "$parent" ]; then
    echo "  // skip $root (env not present)"
    return 0
  fi
  mkdir -p "$root"
  for s in "${SKILLS[@]}"; do
    # Remove any pre-existing entry (real dir, file, or stale symlink) so we
    # never nest a link inside an old directory of the same name.
    rm -rf "$root/$s"
    ln -s "$CANON/$s" "$root/$s"
  done
  echo "  // linked ${#SKILLS[@]} skills -> $root"
}

echo "// data_rein skill installer  [canonical=$CANON]"
echo "// skills: ${SKILLS[*]}"
for t in "${TARGETS[@]}"; do
  link_into "$t"
done
echo "// [OK] skills reorganized under the harness."
