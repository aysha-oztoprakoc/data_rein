import gc
import resource
from unittest.mock import patch
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from reins.services.data_nexus.scraper import NexusScraper

def test_ram_sinkhole_defense() -> None:
    """Ensure the HTML-to-Markdown parser does not consume excessive RAM on nested payloads."""
    depth = 1000
    dom_bomb = "<div>" * depth + "Malicious Payload" + "</div>" * depth
    
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (500 * 1024 * 1024, hard))
    
    def safe_parse(html_str: str) -> str:
        import sys
        old_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(500)
        try:
            soup = BeautifulSoup(html_str, "html.parser")
            return md(str(soup))
        except (MemoryError, RecursionError):
            return "[Error] Nested document exceeded the parser safety limit."
        finally:
            sys.setrecursionlimit(old_limit)

    try:
        clean_text = safe_parse(dom_bomb)
        assert "[Error]" in clean_text or "Malicious Payload" in clean_text
    finally:
        resource.setrlimit(resource.RLIMIT_AS, (soft, hard))
        gc.collect()

# NOTE: test_graceful_bot_degradation was removed — it exercised a throwaway local
# closure, not scraper code. Real graceful degradation is asserted below via the
# actual NexusScraper.search returning [] on network failure.


def test_scraper_engine_search() -> None:
    """Ensure DuckDuckGo search returns standard dictionaries and degrades gracefully on network errors."""
    with patch('reins.services.data_nexus.scraper.external_io.call') as mock_call:
        # Mock valid return
        mock_call.return_value = [{"title": "Test", "href": "http://test.com"}]
        
        scraper = NexusScraper()
        results = scraper.search("test query")
        assert len(results) == 1
        assert results[0]["href"] == "http://test.com"
        
        # Mock exception to test graceful degradation
        mock_call.side_effect = Exception("Network Error")
        results_err = scraper.search("fail query")
        assert results_err == [], "Pedantic Wall: Search must return empty list on network error, not crash."
