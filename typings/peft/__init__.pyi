from transformers import PreTrainedModel

class AutoPeftModelForCausalLM(PreTrainedModel):
    @classmethod
    def from_pretrained(
        cls,
        model: str,
        *,
        local_files_only: bool = False,
    ) -> AutoPeftModelForCausalLM: ...
    def merge_and_unload(self) -> PreTrainedModel: ...

class LoraConfig:
    def __init__(
        self,
        *,
        r: int,
        lora_alpha: int,
        lora_dropout: float,
        target_modules: list[str],
        task_type: str,
    ) -> None: ...

def get_peft_model(model: PreTrainedModel, config: LoraConfig) -> PreTrainedModel: ...
