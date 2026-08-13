#!/usr/bin/env bash
# Link the canonical data_rein harness skills into every environment that scans
# for skills. Idempotent, PON-compliant (runs on demand, exits). Symlinks only,
# so `skills/` stays the single editable source of truth.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
HOME_DIR="$(cd "${DATA_REIN_HOME:-$SCRIPT_DIR/..}" && pwd)"
CANON="$HOME_DIR/skills"
REGISTRY="$SCRIPT_DIR/../src/reins/harness/skill_registry.py"

PYTHON=python3
if [ -x "$HOME_DIR/.venv/bin/python" ]; then
  PYTHON="$HOME_DIR/.venv/bin/python"
fi
SKILL_OUTPUT="$($PYTHON "$REGISTRY" "$CANON")"
mapfile -t SKILLS <<< "$SKILL_OUTPUT"

# Target skill roots per environment. Missing parents are created; environments
# whose parent dir does not exist (e.g. no ~/.claude) are skipped gracefully.
TARGETS=(
  "$HOME_DIR/odysseus/data/skills"                       # Odysseus (SKILLS_DIR)
  "$HOME/.claude/skills"                                 # Claude Code
  "$HOME_DIR/.agents/skills"                             # Antigravity, project-local scan path
  "$HOME/.agents/skills"                                 # Antigravity, global scan path (git hooks etc. reference this)
  "$HOME/.codex/skills"
  "$HOME_DIR/odysseus/integrations/codex/skills"
)

root_is_available() {
  local root="$1"
  local parent; parent="$(dirname "$root")"
  if [ ! -d "$parent" ]; then
    return 1
  fi
  local boundary
  case "$root" in
    "$HOME_DIR"/*) boundary="$HOME_DIR" ;;
    "$HOME"/*) boundary="$HOME" ;;
    *)
      echo "ERROR: target skill root escapes an owned environment: $root" >&2
      return 2
      ;;
  esac
  local physical_boundary physical_parent
  physical_boundary="$(cd "$boundary" && pwd -P)"
  physical_parent="$(cd "$parent" && pwd -P)"
  case "$physical_parent" in
    "$physical_boundary"|"$physical_boundary"/*) ;;
    *)
      echo "ERROR: target skill root resolves outside its environment: $root" >&2
      return 2
      ;;
  esac
  if [ -L "$root" ]; then
    echo "ERROR: target skill root is a symlink: $root" >&2
    return 2
  fi
  return 0
}

preflight() {
  local root="$1"
  root_is_available "$root" || return $?
  if [ -e "$root" ] && [ ! -d "$root" ]; then
    echo "ERROR: target skill root is not a directory: $root" >&2
    return 2
  fi
  for s in "${SKILLS[@]}"; do
    if [ -e "$root/$s" ] && [ ! -L "$root/$s" ]; then
      echo "ERROR: refusing to replace real target entry: $root/$s" >&2
      return 2
    fi
  done
}

link_into() {
  local root="$1"
  if ! root_is_available "$root"; then
    echo "  // skip $root (env not present)"
    return 0
  fi
  mkdir -p "$root"
  root_is_available "$root"
  for s in "${SKILLS[@]}"; do
    local destination="$root/$s"
    local source="$CANON/$s"
    if [ -L "$destination" ] && [ "$(readlink -f "$destination")" = "$source" ]; then
      continue
    fi
    local replacement
    replacement="$(mktemp --tmpdir="$root" ".${s}.link.XXXXXX")"
    unlink "$replacement"
    ln -s "$source" "$replacement"
    mv -Tf "$replacement" "$destination"
  done
  echo "  // linked ${#SKILLS[@]} skills -> $root"
}

echo "// data_rein skill installer  [canonical=$CANON]"
echo "// skills: ${SKILLS[*]}"
for t in "${TARGETS[@]}"; do
  result=0
  preflight "$t" || result=$?
  if [ "$result" -eq 2 ]; then
    exit 2
  fi
done
for t in "${TARGETS[@]}"; do
  link_into "$t"
done
echo "// [OK] canonical skill links installed."
