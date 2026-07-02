from typing import Any, Dict


class BaseExtractor:
    """FBE (Fact Base Element) for data extraction.
    Attributes: filepath, format, status, result, error
    """
    SUPPORTED_FORMATS: list[str] = []
    NODE: str = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        """Extract data from file.
        Returns:
            Dict[str, Any]: {
                "status": "success" | "error",
                "output_path": str,
                "metadata": Dict[str, Any],
                "error": str
            }
        """
        raise NotImplementedError
