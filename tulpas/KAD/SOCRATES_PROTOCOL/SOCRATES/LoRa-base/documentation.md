# `lora_script.py` — Function-by-Function Documentation

This document walks through every function in the QLoRA fine-tuning and inference pipeline, explaining what it does, why it exists, and showing the corresponding code.

---

## 1. Configuration & Setup

### `get_quantization_config()`

**Purpose:** Builds the 4-bit quantization configuration that makes it possible to load large models (7B/8B parameters) into a fraction of the VRAM they'd normally require.

**How it works:**
- `load_in_4bit=True` — loads model weights in 4-bit precision instead of 16/32-bit.
- `bnb_4bit_use_double_quant=True` — applies a second round of quantization to the quantization constants themselves, squeezing out a bit more memory savings.
- `bnb_4bit_quant_type="nf4"` — uses the NormalFloat4 data type, which is optimized for the roughly-normal distribution of neural network weights (better accuracy than plain int4).
- `bnb_4bit_compute_dtype=torch.bfloat16` — while weights are stored in 4-bit, actual computation (matrix multiplications) happens in bfloat16 for numerical stability.

```python
def get_quantization_config() -> BitsAndBytesConfig:
    """Configures 4-bit quantization to fit LLMs on consumer GPUs."""
    return BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )
```

---

### `load_base_model_and_tokenizer(model_id, bnb_config)`

**Purpose:** Downloads/loads the tokenizer and the base language model, applying the quantization config from above.

**How it works:**
- Loads the tokenizer matching the given `model_id`.
- Sets the padding token to the end-of-sequence token, since many Llama-family tokenizers don't define a pad token by default — this is required for batched training.
- Loads the causal language model with the quantization config applied, and `device_map="auto"` lets `accelerate` automatically distribute the model across available GPU(s)/CPU.

```python
def load_base_model_and_tokenizer(model_id: str, bnb_config: BitsAndBytesConfig):
    """Loads the tokenizer and the quantized base model."""
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map="auto"
    )
    return model, tokenizer
```

---

### `apply_lora_to_model(model)`

**Purpose:** Converts the frozen, quantized base model into a trainable LoRA model.

**How it works:**
- `prepare_model_for_kbit_training(model)` — does housekeeping needed for training on top of a quantized model: casts certain layers to the right precision, enables gradient checkpointing compatibility, and freezes the base model's weights.
- `LoraConfig` defines the LoRA hyperparameters:
  - `r=16` — the rank of the low-rank matrices (higher = more trainable capacity, more memory).
  - `lora_alpha=32` — scaling factor applied to the LoRA updates (commonly set to 2x the rank).
  - `target_modules=[...]` — which attention projection layers (query, key, value, output) get LoRA adapters injected.
  - `lora_dropout=0.05` — dropout applied within the LoRA layers to reduce overfitting.
  - `bias="none"` — bias terms are not trained.
  - `task_type="CAUSAL_LM"` — tells PEFT this is a causal (autoregressive) language modeling task.
- `get_peft_model(model, lora_config)` wraps the base model, injecting the trainable LoRA matrices while keeping the original weights frozen.
- `print_trainable_parameters()` prints how few parameters actually need training (a small fraction of the full model), which is the core benefit of LoRA.

```python
def apply_lora_to_model(model) -> tuple:
    """Prepares the model for k-bit training and wraps it in the LoRA configuration."""
    model = prepare_model_for_kbit_training(model)
    
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )
    
    peft_model = get_peft_model(model, lora_config)
    peft_model.print_trainable_parameters()
    
    return peft_model, lora_config
```

---

### `load_training_data(dataset_path)`

**Purpose:** Loads the training dataset from a JSON/JSONL file into a Hugging Face `Dataset` object.

**How it works:** Uses the `datasets` library's generic `"json"` loader, pointing at the user-supplied file, and pulls out the `"train"` split (the default split name when loading a single file).

```python
def load_training_data(dataset_path: str):
    """Loads the dataset from a JSON file."""
    return load_dataset("json", data_files=dataset_path, split="train")
```

---

## 2. Execution Pipelines

### `run_training(model, tokenizer, dataset, lora_config, output_dir, text_column)`

**Purpose:** Configures the actual training loop hyperparameters and runs fine-tuning via `SFTTrainer`, then saves the resulting adapter.

**How it works:**
- `TrainingArguments` sets standard training knobs:
  - `per_device_train_batch_size=4` and `gradient_accumulation_steps=4` — effectively simulates a batch size of 16 without needing that much VRAM at once.
  - `optim="paged_adamw_32bit"` — a memory-efficient optimizer variant designed to work well with quantized models (pages optimizer states to CPU when needed).
  - `logging_steps=10` — how often training metrics are printed.
  - `learning_rate=2e-4` — a typical LoRA learning rate (higher than full fine-tuning since only a small number of parameters are updated).
  - `fp16=True` — mixed-precision training for speed/memory efficiency.
  - `max_steps=200` — caps training length regardless of dataset size (useful for quick experiments).
  - `save_strategy="steps"` / `save_steps=50` — checkpoints saved every 50 steps.
- `SFTTrainer` (from `trl`) wraps all the complexity of tokenization, padding, batching, and the training loop for causal language modeling, using `text_column` to know which dataset field holds the training text.
- After training, the trainer's model (the LoRA adapter weights) is saved to `output_dir/final_adapter`.

```python
def run_training(model, tokenizer, dataset, lora_config, output_dir: str, text_column: str):
    """Configures the training arguments and executes the SFTTrainer loop."""
    training_args = TrainingArguments(
        output_dir=output_dir,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        optim="paged_adamw_32bit",
        logging_steps=10,
        learning_rate=2e-4,
        fp16=True,
        max_steps=200,
        save_strategy="steps",
        save_steps=50,
    )

    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=lora_config,
        dataset_text_field=text_column,  # Passed dynamically via argparse
        max_seq_length=512,
        tokenizer=tokenizer,
        args=training_args,
    )
    
    trainer.train()
    
    final_path = f"{output_dir}/final_adapter"
    trainer.model.save_pretrained(final_path)
    print(f"Training complete. Adapter saved to {final_path}")
```

---

### `train_pipeline(model_id, dataset_path, output_dir, text_column)`

**Purpose:** The top-level orchestrator for the entire training flow — calls each setup function in the correct order.

**How it works:** Simply chains together, in sequence:
1. Build the quantization config.
2. Load the base model and tokenizer.
3. Apply LoRA to the model.
4. Load the training dataset.
5. Run the actual training loop.

Each step prints a status message so progress is visible in the console.

```python
def train_pipeline(model_id: str, dataset_path: str, output_dir: str, text_column: str):
    """Orchestrates the entire LoRA fine-tuning process."""
    print("1. Configuring quantization...")
    bnb_config = get_quantization_config()
    
    print(f"2. Loading model ({model_id}) and tokenizer...")
    base_model, tokenizer = load_base_model_and_tokenizer(model_id, bnb_config)
    
    print("3. Applying LoRA...")
    peft_model, lora_config = apply_lora_to_model(base_model)
    
    print(f"4. Loading dataset from {dataset_path}...")
    dataset = load_training_data(dataset_path)
    
    print("5. Starting training loop...")
    run_training(peft_model, tokenizer, dataset, lora_config, output_dir, text_column)
```

---

### `inference_pipeline(model_id, adapter_path, prompt)`

**Purpose:** Loads the base model plus a previously trained LoRA adapter, then generates text from a given prompt.

**How it works:**
1. Rebuilds the same quantization config and loads the base model/tokenizer — this must match what was used during training.
2. `PeftModel.from_pretrained(base_model, adapter_path)` attaches the trained LoRA weights on top of the frozen base model.
3. Tokenizes the prompt and moves it to the GPU (`"cuda"`).
4. Calls `.generate()` to produce up to 100 new tokens.
5. Decodes and prints the generated output, skipping special tokens (like `<eos>`) for readability.

```python
def inference_pipeline(model_id: str, adapter_path: str, prompt: str):
    """Loads the base model, applies the adapter, and generates text."""
    print(f"1. Loading base model ({model_id}) and tokenizer...")
    bnb_config = get_quantization_config()
    base_model, tokenizer = load_base_model_and_tokenizer(model_id, bnb_config)
    
    print(f"2. Merging LoRA adapter from {adapter_path}...")
    fine_tuned_model = PeftModel.from_pretrained(base_model, adapter_path)
    
    print("3. Generating text...")
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = fine_tuned_model.generate(**inputs, max_new_tokens=100)
    
    print("\n--- Output ---")
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

> **Note:** Despite the print statement saying "Merging," this function actually *attaches* the adapter (via `PeftModel.from_pretrained`) rather than merging its weights into the base model (which would require calling `.merge_and_unload()` separately).

---

## 3. CLI Argument Parsing (`__main__` block)

**Purpose:** Defines the command-line interface, validates required arguments based on the selected mode, and dispatches to the correct pipeline.

**How it works:**
- `--mode` is required and must be either `"train"` or `"inference"` — this is the main switch controlling program behavior.
- `--model_id` is shared by both modes and defaults to `meta-llama/Meta-Llama-3-8B`.
- Training-specific arguments: `--dataset_path`, `--output_dir` (default `./llama-lora-outputs`), `--text_column` (default `"text"`).
- Inference-specific arguments: `--adapter_path`, `--prompt`.
- After parsing, the script manually enforces conditional requirements that `argparse` can't express natively:
  - In `train` mode, `--dataset_path` must be provided, or the script exits with an error.
  - In `inference` mode, both `--adapter_path` and `--prompt` must be provided.
- Finally, it calls either `train_pipeline(...)` or `inference_pipeline(...)` with the parsed arguments.

```python
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QLoRA Fine-Tuning and Inference Pipeline for LLMs.")
    
    # Required Mode
    parser.add_argument("--mode", type=str, choices=["train", "inference"], required=True, 
                        help="Choose whether to train a new adapter or run inference.")
    
    # Common Arguments
    parser.add_argument("--model_id", type=str, default="meta-llama/Meta-Llama-3-8B", 
                        help="The Hugging Face model ID or local path to the base model.")
    
    # Training Arguments
    parser.add_argument("--dataset_path", type=str, 
                        help="Path to the JSON dataset (Required for training).")
    parser.add_argument("--output_dir", type=str, default="./llama-lora-outputs", 
                        help="Directory to save the trained adapter.")
    parser.add_argument("--text_column", type=str, default="text", 
                        help="The column name in your dataset containing the text to train on.")
    
    # Inference Arguments
    parser.add_argument("--adapter_path", type=str, 
                        help="Path to the saved LoRA adapter (Required for inference).")
    parser.add_argument("--prompt", type=str, 
                        help="The text prompt to feed the model (Required for inference).")

    args = parser.parse_args()

    # Route logic based on mode and enforce required arguments dynamically
    if args.mode == "train":
        if not args.dataset_path:
            parser.error("--dataset_path is required when --mode is 'train'")
        
        train_pipeline(args.model_id, args.dataset_path, args.output_dir, args.text_column)
        
    elif args.mode == "inference":
        if not args.adapter_path:
            parser.error("--adapter_path is required when --mode is 'inference'")
        if not args.prompt:
            parser.error("--prompt is required when --mode is 'inference'")
            
        inference_pipeline(args.model_id, args.adapter_path, args.prompt)
```

---

## Summary of Call Flow

```
train mode:
  train_pipeline
    ├── get_quantization_config
    ├── load_base_model_and_tokenizer
    ├── apply_lora_to_model
    ├── load_training_data
    └── run_training

inference mode:
  inference_pipeline
    ├── get_quantization_config
    ├── load_base_model_and_tokenizer
    └── PeftModel.from_pretrained (attach adapter) → generate
```
