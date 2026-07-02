#!/bin/bash
set -e

# Change to the directory containing pyproject.toml (one level up from this script)
cd "$(dirname "$0")/.."

echo "Setting up Data Harness..."

# 1. Ensure Python dependencies are installed using uv
echo "Installing dependencies via uv..."
if command -v uv &> /dev/null; then
    uv sync
else
    echo "Warning: uv not found. Please install uv (https://github.com/astral-sh/uv) or install dependencies manually."
fi

# 2. Check for local system tools
echo "Checking local system tools..."
if ! command -v inotifywait &> /dev/null; then
    echo "Warning: inotifywait not found. Install it for the sync daemon to work (e.g. pacman -S inotify-tools)."
fi
if ! command -v pdftotext &> /dev/null; then
    echo "Warning: pdftotext not found (poppler). Install it for PDF extraction."
fi

echo "Data Harness setup complete!"
