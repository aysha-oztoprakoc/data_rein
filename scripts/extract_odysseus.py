import os
import logging
from reins.services.data_nexus.scraper import NexusScraper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("odysseus_extractor")

def main():
    logger.info("Initializing Nexus Scraper for Odysseus AI...")
    scraper = NexusScraper()
    
    # Target URLs from Google Search Results
    urls_to_scrape = [
        "https://raw.githubusercontent.com/pewdiepie-archdaemon/odysseus/main/README.md",
        "https://pewdiepie-archdaemon.github.io/odysseus/"
    ]
    
    logger.info(f"Scraping URLs: {urls_to_scrape}")
    extracted_data = scraper.scrape_urls(urls_to_scrape)
    
    # Save extracted content to Universal Knowledge Base
    kb_dir = os.path.expanduser("~/data_rein/knowledge_base/agents/odysseus")
    os.makedirs(kb_dir, exist_ok=True)
    
    merged_content = "# Odysseus AI Knowledge Documentation\n\n"
    
    for url, md_content in extracted_data.items():
        if "[Error]" in md_content:
            logger.warning(f"Skipping failed extraction for {url}: {md_content}")
            continue
        merged_content += f"## Source: {url}\n\n{md_content}\n\n---\n"
        
    filepath = os.path.join(kb_dir, "documentation.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(merged_content)
        
    logger.info(f"Universal Knowledge Database updated: {filepath}")

if __name__ == "__main__":
    main()
