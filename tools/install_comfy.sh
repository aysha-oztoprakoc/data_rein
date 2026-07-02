#!/bin/bash
echo "Activating virtual environment..."
source /home/amdy/ComfyUI/venv/bin/activate
cd /home/amdy/ComfyUI

echo "Installing PyTorch for AMD ROCm..."
pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.0

echo "Installing ComfyUI requirements..."
pip install -r requirements.txt

echo "Downloading Stable Diffusion 1.5 Base Model..."
mkdir -p models/checkpoints
wget -nc -O models/checkpoints/v1-5-pruned-emaonly.safetensors "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors"

echo "Installation complete!"
