import sys
import logging
from typing import List, Dict, Optional
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from duckduckgo_search import DDGS
from playwright.sync_api import sync_playwright, TimeoutError

logger = logging.getLogger("nexus_scraper")

def safe_parse(html_str: str) -> str:
    """PON Compliant Safe Parser: Protects against Recursion/RAM sinkholes."""
    old_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(500)
    try:
        soup = BeautifulSoup(html_str, "html.parser")
        return md(str(soup))
    except RecursionError:
        logger.error("Recursion limit exceeded during parsing. Gracefully degrading.")
        return "[Error] Content too deeply nested to parse safely."
    except Exception as e:
        logger.error(f"Unexpected parsing error: {e}")
        return ""
    finally:
        sys.setrecursionlimit(old_limit)

class NexusScraper:
    def __init__(self) -> None:
        self.ddgs = DDGS()

    def search(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """Searches the web securely without API keys."""
        logger.info(f"Searching web for: {query}")
        results = []
        try:
            for r in self.ddgs.text(query, max_results=max_results):
                results.append(r)
        except Exception as e:
            logger.error(f"Search failed: {e}")
        return results

    def scrape_urls(self, urls: List[str]) -> Dict[str, str]:
        """Scrapes multiple URLs headlessly, bypassing simple bot blocks."""
        extracted_data = {}
        with sync_playwright() as p:
            # Launch chromium headlessly. 
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            for url in urls:
                logger.info(f"Scraping {url}...")
                try:
                    # PON Rule: Passive wait with timeout
                    page.goto(url, timeout=15000, wait_until="domcontentloaded")
                    # Wait for network idle or 3 seconds to let JS execute
                    page.wait_for_timeout(3000)
                    html = page.content()
                    
                    # Graceful Degradation check
                    if "Cloudflare" in html and "Access Denied" in html:
                        logger.warning(f"Bot defense detected at {url}. Degrading gracefully.")
                        extracted_data[url] = "[Error] Bot defense prevented access."
                        continue
                        
                    clean_md = safe_parse(html)
                    extracted_data[url] = clean_md
                except TimeoutError:
                    logger.error(f"Timeout scraping {url}")
                    extracted_data[url] = "[Error] Timeout."
                except Exception as e:
                    logger.error(f"Failed to scrape {url}: {e}")
                    extracted_data[url] = f"[Error] {str(e)}"
                    
            browser.close()
            
        return extracted_data
