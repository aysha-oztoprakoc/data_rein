import argparse
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TrainingArguments
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training, PeftModel
from trl import SFTTrainer
from datasets import load_dataset

### 1. Configuration & Setup ###

def get_quantization_config() -> BitsAndBytesConfig:
    """Configures 4-bit quantization to fit LLMs on consumer GPUs."""
    return BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )

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

def load_training_data(dataset_path: str):
    """Loads the dataset from a JSON file."""
    return load_dataset("json", data_files=dataset_path, split="train")

### 2. Execution Pipelines ###

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

### 3. CLI Argument Parsing ###

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
