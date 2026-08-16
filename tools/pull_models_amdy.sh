#!/bin/bash
# pull_models_amdy.sh

# Wait for ollama daemon
until curl -s http://localhost:11434/api/tags > /dev/null; do
  echo "Waiting for ollama daemon..."
  sleep 5
done

echo "Ollama is up! Starting AMDY model pulls..."

# Default Chat
ollama pull qwen3.5:9b
ollama pull llama3.1:8b
ollama pull qwen2.5:7b
ollama pull llama3.2:3b
ollama pull phi4-mini

# Extraction and Training (SOTA mid-2026 for 8GB VRAM)
ollama pull llama3.3:8b
ollama pull gemma3:4b
ollama pull qwen3:8b

# Utility
ollama pull qwen2.5-coder:7b
ollama pull phi3.5:3.8b
ollama pull qwen2.5-coder:1.5b

# Vision
ollama pull llama3.2-vision:11b
ollama pull qwen2.5-vl:7b
ollama pull moondream:1.8b

# Research
ollama pull deepseek-r1:14b
ollama pull deepseek-r1:8b
ollama pull deepseek-r1:1.5b

echo "All AMDY models pulled successfully!"
