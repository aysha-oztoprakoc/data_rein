from .extractors.base import BaseExtractor
from .registry import registry

# Import extractors to trigger auto-registration
from .extractors import archive_extractors as archive_extractors
from .extractors import media_extractors as media_extractors
from .extractors import text_extractors as text_extractors

__all__ = ["BaseExtractor", "registry"]
