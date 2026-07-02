import re

class TokenCompressor:
    """Compresses prompts to save tokens while preserving meaning."""
    
    def compress(self, text: str) -> str:
        if not text:
            return ""
        # Remove consecutive empty lines
        text = re.sub(r'\n\s*\n', '\n', text)
        # Remove excess whitespace
        text = re.sub(r' {2,}', ' ', text)
        # Remove common filler phrases (this is a simplified example)
        filler_phrases = [
            "Please can you ", "I would like you to ", "Could you please ",
            "I want you to ", "Would it be possible to ", "If you don't mind, "
        ]
        for phrase in filler_phrases:
            text = text.replace(phrase, "")
            text = text.replace(phrase.capitalize(), "")
            
        return text.strip()
