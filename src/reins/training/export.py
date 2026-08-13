"""
Export a fine-tuned LoRA run to a servable Ollama model: merge adapter into
the base model, convert to GGUF (via llama.cpp if available), quantize, and
`ollama create` - so the tuned model rejoins the existing Ollama plane.
Every step degrades to a printed manual instruction rather than raising.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from reins.harness import external_io
from reins.services.logger import log_degradation


def to_ollama(run_dir: str, tag: str, *, llama_cpp_dir: str | None = None) -> bool:
    run_path = Path(run_dir).expanduser()
    if not run_path.exists():
        print(f"// export failed: run_dir does not exist: {run_path}")
        return False

    merged_dir = run_path / "merged"
    if not _merge_adapter(run_path, merged_dir):
        return False

    gguf_path = run_path / "model.gguf"
    if not _convert_to_gguf(merged_dir, gguf_path, llama_cpp_dir):
        print("// GGUF conversion unavailable - manual step:")
        print(f"//   python convert_hf_to_gguf.py {merged_dir} --outfile {gguf_path} --outtype q8_0")
        print(f"//   llama-quantize {gguf_path} {run_path / 'model.q4_k_m.gguf'} q4_K_M")
        print(f"//   ollama create {tag} -f <Modelfile pointing at model.q4_k_m.gguf>")
        return False

    quantized = run_path / "model.q4_k_m.gguf"
    _ = _quantize(gguf_path, quantized, llama_cpp_dir)
    final_gguf = quantized if quantized.exists() else gguf_path

    modelfile = run_path / "Modelfile"
    _ = modelfile.write_text(f"FROM {final_gguf}\n")
    try:
        _ = external_io.run(["ollama", "create", tag, "-f", str(modelfile)], check=True)
        return True
    except Exception as e:
        log_degradation(__name__)
        print(f"// `ollama create {tag}` failed: {e}")
        print(f"//   Modelfile written at {modelfile} - run the command manually once ollama is reachable.")
        return False


def _merge_adapter(run_path: Path, merged_dir: Path) -> bool:
    try:
        from peft import AutoPeftModelForCausalLM
        from transformers import AutoTokenizer

        model = AutoPeftModelForCausalLM.from_pretrained(
            str(run_path),
            local_files_only=True,
        )
        merged = model.merge_and_unload()
        merged_dir.mkdir(parents=True, exist_ok=True)
        merged.save_pretrained(str(merged_dir))
        # The run path is local and local_files_only forbids a network download.
        AutoTokenizer.from_pretrained(  # nosec B615
            str(run_path),
            local_files_only=True,
        ).save_pretrained(str(merged_dir))
        return True
    except Exception as e:
        log_degradation(__name__)
        print(f"// adapter merge unavailable ({e}) - install the `train` extra: uv sync --extra train")
        return False


def _convert_to_gguf(merged_dir: Path, gguf_path: Path, llama_cpp_dir: str | None) -> bool:
    script = _find_llama_cpp_script(llama_cpp_dir)
    if script is None:
        return False
    try:
        _ = external_io.run(
            [
                "python3",
                str(script),
                str(merged_dir),
                "--outfile",
                str(gguf_path),
                "--outtype",
                "q8_0",
            ],
            check=True,
        )
        return gguf_path.exists()
    except Exception as e:
        log_degradation(__name__)
        print(f"// GGUF conversion failed: {e}")
        return False


def _quantize(gguf_path: Path, out_path: Path, llama_cpp_dir: str | None) -> bool:
    quantize_bin = shutil.which("llama-quantize")
    if quantize_bin is None and llama_cpp_dir:
        candidate = Path(llama_cpp_dir).expanduser() / "llama-quantize"
        quantize_bin = str(candidate) if candidate.exists() else None
    if quantize_bin is None:
        return False
    try:
        _ = external_io.run(
            [quantize_bin, str(gguf_path), str(out_path), "q4_K_M"],
            check=True,
        )
        return out_path.exists()
    except Exception as e:
        log_degradation(__name__)
        print(f"// quantization failed: {e}")
        return False


def _find_llama_cpp_script(llama_cpp_dir: str | None) -> Path | None:
    candidates: list[Path] = []
    if llama_cpp_dir:
        candidates.append(Path(llama_cpp_dir).expanduser() / "convert_hf_to_gguf.py")
    candidates.append(Path("/home/amdy/data_rein/llama.cpp/convert_hf_to_gguf.py"))
    for c in candidates:
        if c.exists():
            return c
    return None
