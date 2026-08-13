# QLoRA Llama Fine-Tuning & Inference Pipeline

This repository contains a modularized, command-line ready Python script for fine-tuning Large Language Models (like Meta's Llama-3) on consumer hardware using QLoRA (Quantized Low-Rank Adaptation).

## 📚 Libraries Used

This pipeline relies on the modern NLP stack provided primarily by Hugging Face:

* **`torch`**: The core deep learning framework underlying all the operations.
* **`transformers`**: Hugging Face's library for loading the base Llama model, tokenizers, and handling the core architecture.
* **`peft` (Parameter-Efficient Fine-Tuning)**: Used to freeze the base model and inject the trainable LoRA matrices into the attention layers, drastically reducing trainable parameters.
* **`accelerate`**: Automatically handles device placement and memory management, crucial for running massive models efficiently across available GPUs.
* **`bitsandbytes`**: The engine behind 4-bit quantization. It allows us to load a 7B/8B parameter model into a fraction of the VRAM it would normally require (e.g., fitting an 8B model into ~6-8GB VRAM).
* **`trl` (Transformer Reinforcement Learning)**: Provides the `SFTTrainer` (Supervised Fine-Tuning Trainer), which simplifies the complex padding, batching, and gradient accumulation required for causal language modeling.
* **`datasets`**: Efficiently loads and processes JSON training data.
* **`scipy` & `sentencepiece`**: Backend dependencies required by Llama tokenizers and specific quantization operations.

---

## ⚙️ Installation

1. Ensure you have Python 3.8+ installed.
2. It is highly recommended to use a Linux environment with an NVIDIA GPU, as `bitsandbytes` is highly optimized for Linux/CUDA.
3. Install the required dependencies using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use the Pipeline

The script (`lora_script.py`) uses command-line arguments to switch between training a new model and running inference on an existing adapter.

### 1. Training Mode

To train a new LoRA adapter, you must provide the path to your dataset. The dataset should be a JSON/JSONL file where each entry has a `text` field containing the formatted prompt/response pair.

**Command:**

```bash
python lora_script.py --mode train \
    --model_id "meta-llama/Meta-Llama-3-8B" \
    --dataset_path "my_custom_data.json" \
    --output_dir "./adapters" \
    --text_column "text"
```

**Arguments:**

* `--mode train`: Tells the script to execute the training loop.
* `--model_id`: The Hugging Face repo ID or local path to your base model.
* `--dataset_path`: Path to your JSON training data.
* `--output_dir`: Where the final LoRA adapter weights will be saved.
* `--text_column`: The key in your JSON dataset that contains the text to be trained on (default is `"text"`).

### 2. Inference Mode

Once you have trained an adapter, you can load it on top of the base model to generate text.

**Command:**

```bash
python lora_script.py --mode inference \
    --model_id "meta-llama/Meta-Llama-3-8B" \
    --adapter_path "./adapters/final_adapter" \
    --prompt "Explain the concept of LoRA in machine learning:"
```

**Arguments:**

* `--mode inference`: Tells the script to load the models and generate text.
* `--model_id`: Must be the EXACT same base model you used for training.
* `--adapter_path`: The directory containing the adapter you saved during the training phase.
* `--prompt`: The input text you want the model to complete.

---

## 📝 Data Formatting Note

For supervised fine-tuning to work well, ensure your JSON dataset is formatted to match the exact prompt template expected by the base model (e.g., ChatML, Alpaca format, or Llama-3 instruction format) within the column specified by `--text_column`.
