#!/usr/bin/env bash
# scripts/nix_cache_service.sh
set -euo pipefail

# Directory for the binary cache
DATA_REIN_HOME="${DATA_REIN_HOME:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
CACHE_DIR="$DATA_REIN_HOME/nix-cache"
KEY_DIR="$DATA_REIN_HOME/config/keys"

# Ensure directories exist
mkdir -p "$CACHE_DIR"
mkdir -p "$KEY_DIR"

CACHE_NAME="data_rein-1"
PRIVATE_KEY="$KEY_DIR/cache-priv-key.pem"
PUBLIC_KEY="$KEY_DIR/cache-pub-key.pem"

if [ ! -f "$PRIVATE_KEY" ] || [ ! -f "$PUBLIC_KEY" ]; then
    echo "Generating new cache keys..."
    nix-store --generate-binary-cache-key "$CACHE_NAME" "$PRIVATE_KEY" "$PUBLIC_KEY"
fi

# Function to serve the cache locally
serve_cache() {
    PORT="${CACHE_PORT:-8080}"
    echo "Serving Nix binary cache on http://localhost:$PORT"
    echo "Public key is: $(cat "$PUBLIC_KEY")"
    cd "$CACHE_DIR"
    python3 -m http.server "$PORT"
}

# Function to publish (sign and copy) a store path to the cache
publish_path() {
    STORE_PATH="$1"
    echo "Publishing $STORE_PATH to cache..."
    # Sign the path
    nix --extra-experimental-features 'nix-command flakes' store sign --key-file "$PRIVATE_KEY" "$STORE_PATH"
    # Copy to local binary cache directory
    nix --extra-experimental-features 'nix-command flakes' copy --to "file://$CACHE_DIR" "$STORE_PATH"
}

if [ "$#" -eq 0 ]; then
    serve_cache
elif [ "$1" = "serve" ]; then
    serve_cache
elif [ "$1" = "publish" ]; then
    if [ -z "${2:-}" ]; then
        echo "Usage: $0 publish <store-path>"
        exit 1
    fi
    publish_path "$2"
else
    echo "Usage: $0 [serve | publish <store-path>]"
    exit 1
fi
