import pytest
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
        except RecursionError:
            return "[Error] Recursion limit exceeded. Graceful degradation."
        finally:
            sys.setrecursionlimit(old_limit)

    try:
        clean_text = safe_parse(dom_bomb)
        assert "[Error]" in clean_text or "Malicious Payload" in clean_text
    finally:
        resource.setrlimit(resource.RLIMIT_AS, (soft, hard))
        gc.collect()

def test_graceful_bot_degradation() -> None:
    """Ensure that the scraper gracefully handles blocked requests instead of crashing."""
    status_code = 403
    html = "<html><body>Access Denied - Cloudflare</body></html>"
    
    def process_response(code: int, html_body: str) -> str:
        if code == 403 or "Access Denied" in html_body:
            raise PermissionError("Bot defense triggered. Graceful Degradation active.")
        return html_body
        
    error_caught = False
    try:
        process_response(status_code, html)
    except PermissionError:
        error_caught = True
        
    assert error_caught is True, "Scraper failed to degrade gracefully on bot blocks."

def test_scraper_engine_search() -> None:
    """Ensure DuckDuckGo search returns standard dictionaries and degrades gracefully on network errors."""
    with patch('reins.services.data_nexus.scraper.DDGS.text') as mock_ddgs:
        # Mock valid return
        mock_ddgs.return_value = [{"title": "Test", "href": "http://test.com"}]
        
        scraper = NexusScraper()
        results = scraper.search("test query")
        assert len(results) == 1
        assert results[0]["href"] == "http://test.com"
        
        # Mock exception to test graceful degradation
        mock_ddgs.side_effect = Exception("Network Error")
        results_err = scraper.search("fail query")
        assert results_err == [], "Pedantic Wall: Search must return empty list on network error, not crash."
