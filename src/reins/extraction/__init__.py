from .extractors.base import BaseExtractor
from .registry import registry

# Import extractors to trigger auto-registration
from .extractors import text_extractors
from .extractors import media_extractors
from .extractors import archive_extractors

__all__ = ["BaseExtractor", "registry"]
