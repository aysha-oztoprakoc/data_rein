from abc import ABC, abstractmethod
from typing import ClassVar, Literal, NotRequired, TypeAlias, TypedDict


class ExtractionMetadata(TypedDict, total=False):
    """Machine-readable provenance produced with extracted knowledge."""

    format: str
    modality: str
    extractor: str
    node: str
    channels: list[str]
    frame_count: int
    duration_seconds: float
    warnings: list[str]


class ExtractionSuccess(TypedDict):
    """Successful plugin result with a durable output path."""

    status: Literal["success"]
    output_path: str
    metadata: ExtractionMetadata


class ExtractionFailure(TypedDict):
    """Failed plugin result with an actionable diagnostic."""

    status: Literal["error"]
    error: str
    metadata: NotRequired[ExtractionMetadata]


ExtractionResult: TypeAlias = ExtractionSuccess | ExtractionFailure


class BaseExtractor(ABC):
    """FBE (Fact Base Element) for data extraction.
    Attributes: filepath, format, status, result, error
    """
    SUPPORTED_FORMATS: ClassVar[list[str]] = []
    NODE: ClassVar[str] = "amdy"
    MODALITY: ClassVar[str] = "text"

    @abstractmethod
    def extract(self, _filepath: str, _output_dir: str) -> ExtractionResult:
        """Extract data from file.
        Returns:
            ExtractionResult: {
                "status": "success" | "error",
                "output_path": str,
                "metadata": ExtractionMetadata,
                "error": str
            }
        """
        raise NotImplementedError
