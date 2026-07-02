class BaseExtractor:
    """FBE (Fact Base Element) for data extraction.
    Attributes: filepath, format, status, result, error
    """
    SUPPORTED_FORMATS: list[str] = []
    NODE: str = "amdy"

    def extract(self, filepath: str, output_dir: str) -> dict:
        """Extract data from file.
        Returns:
            dict: {
                "status": "success" | "error",
                "output_path": str,
                "metadata": dict,
                "error": str
            }
        """
        raise NotImplementedError
