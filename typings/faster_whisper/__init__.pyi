from collections.abc import Iterable

class Segment:
    text: str

class TranscriptionInfo: ...

class WhisperModel:
    def __init__(self, model_size_or_path: str, *, device: str, compute_type: str) -> None: ...
    def transcribe(
        self,
        audio: str,
        *,
        vad_filter: bool = False,
    ) -> tuple[Iterable[Segment], TranscriptionInfo]: ...
