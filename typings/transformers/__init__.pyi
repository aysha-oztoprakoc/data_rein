from datasets import Dataset
from torch import DType

class BitsAndBytesConfig:
    def __init__(
        self,
        *,
        load_in_4bit: bool,
        bnb_4bit_quant_type: str,
        bnb_4bit_use_double_quant: bool,
        bnb_4bit_compute_dtype: DType,
    ) -> None: ...

class PreTrainedModel:
    def gradient_checkpointing_enable(self) -> None: ...
    def save_pretrained(self, path: str) -> None: ...

class AutoModelForCausalLM:
    @classmethod
    def from_pretrained(
        cls,
        model: str,
        *,
        quantization_config: BitsAndBytesConfig | None = None,
        torch_dtype: DType | None = None,
        device_map: str | None = None,
        revision: str | None = None,
    ) -> PreTrainedModel: ...

class PreTrainedTokenizer:
    def __call__(
        self,
        text: list[str],
        *,
        truncation: bool,
        max_length: int,
    ) -> dict[str, list[list[int]]]: ...
    def save_pretrained(self, path: str) -> None: ...

class AutoTokenizer:
    @classmethod
    def from_pretrained(
        cls,
        model: str,
        *,
        revision: str | None = None,
        local_files_only: bool = False,
    ) -> PreTrainedTokenizer: ...

class TrainingArguments:
    def __init__(
        self,
        *,
        output_dir: str,
        per_device_train_batch_size: int,
        gradient_accumulation_steps: int,
        num_train_epochs: float,
        learning_rate: float,
        optim: str,
        gradient_checkpointing: bool,
        save_strategy: str,
        logging_steps: int,
        report_to: list[str],
    ) -> None: ...

class TrainOutput:
    global_step: int

class Trainer:
    def __init__(
        self,
        *,
        model: PreTrainedModel,
        args: TrainingArguments,
        train_dataset: Dataset,
    ) -> None: ...
    def train(self) -> TrainOutput: ...
