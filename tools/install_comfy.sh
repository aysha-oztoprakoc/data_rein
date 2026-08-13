#!/usr/bin/env bash
set -euo pipefail

REPOSITORY_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COMFY_ROOT="${COMFY_ROOT:-/home/amdy/ComfyUI}"
INTEGRITY_CONFIG="$REPOSITORY_ROOT/config/artifact_integrity.json"

mapfile -t ARTIFACT < <(
  python3 -c 'import json,sys
with open(sys.argv[1], encoding="utf-8") as stream:
    item = json.load(stream)["comfy_checkpoint"]
for key in ("repository", "revision", "file", "sha256"):
    print(item[key])' "$INTEGRITY_CONFIG"
)

if [[ ${#ARTIFACT[@]} -ne 4 ]]; then
  echo "Artifact integrity manifest is incomplete" >&2
  exit 1
fi

REPOSITORY="${ARTIFACT[0]}"
REVISION="${ARTIFACT[1]}"
MODEL_FILE="${ARTIFACT[2]}"
EXPECTED_SHA256="${ARTIFACT[3]}"
if [[ ! "$REVISION" =~ ^[0-9a-f]{40}$ || ! "$EXPECTED_SHA256" =~ ^[0-9a-f]{64}$ ]]; then
  echo "Artifact integrity manifest contains mutable or invalid identifiers" >&2
  exit 1
fi

cd "$COMFY_ROOT"
"$COMFY_ROOT/venv/bin/python" -m pip install --upgrade pip
"$COMFY_ROOT/venv/bin/python" -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.0
"$COMFY_ROOT/venv/bin/python" -m pip install -r requirements.txt

CHECKPOINT_DIR="$COMFY_ROOT/models/checkpoints"
mkdir -p "$CHECKPOINT_DIR"
TEMP_MODEL="$(mktemp "$CHECKPOINT_DIR/.${MODEL_FILE}.download.XXXXXX")"
trap 'rm -f "$TEMP_MODEL"' EXIT
curl --fail --location --proto '=https' \
  --output "$TEMP_MODEL" \
  "https://huggingface.co/$REPOSITORY/resolve/$REVISION/$MODEL_FILE?download=true"
printf '%s  %s\n' "$EXPECTED_SHA256" "$TEMP_MODEL" | sha256sum --check --status
chmod 0644 "$TEMP_MODEL"
mv -f "$TEMP_MODEL" "$CHECKPOINT_DIR/$MODEL_FILE"
trap - EXIT

echo "ComfyUI installation complete with verified checkpoint."
