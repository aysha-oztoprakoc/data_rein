from .extractors.base import BaseExtractor


class ExtractorRegistry:
    """FBE: Registry of all available extractors."""

    def __init__(self) -> None:
        self._registry: dict[str, type[BaseExtractor]] = {}

    def register(self, extractor_class: type[BaseExtractor]) -> None:
        for ext in extractor_class.SUPPORTED_FORMATS:
            self._registry[ext.lower()] = extractor_class

    def get_extractor(self, extension: str) -> BaseExtractor | None:
        cls = self._registry.get(extension.lower())
        if cls:
            return cls()
        return None

    def list_supported(self) -> list[str]:
        return list(self._registry.keys())


registry = ExtractorRegistry()
