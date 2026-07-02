#!/bin/bash
# pull_models_tell.sh

# Wait for ollama daemon
until curl -s http://localhost:11434/api/tags > /dev/null; do
  echo "Waiting for ollama daemon..."
  sleep 5
done

echo "Ollama is up! Starting TELL model pulls..."

# Default Chat
ollama pull llama3.1:8b-instruct-q4_K_M
ollama pull qwen2.5:3b
ollama pull gemma2:2b

# Utility
ollama pull qwen2.5-coder:7b
ollama pull qwen2.5-coder:3b
ollama pull smollm2:1.7b

# Vision
ollama pull qwen2.5-vl:7b
ollama pull minicpm-v:8b
ollama pull moondream:1.8b

# Research
ollama pull deepseek-r1:8b
ollama pull deepseek-r1:7b
ollama pull deepseek-r1:1.5b

echo "All TELL models pulled successfully!"
