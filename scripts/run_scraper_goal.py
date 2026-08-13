import os
import logging

from reins.services.data_nexus.scraper import NexusScraper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("scraper_goal")

def main():
    logger.info("Initializing Nexus Scraper...")
    scraper = NexusScraper()
    
    urls_to_scrape = [
        "https://www.talkcody.com/?ref=taaft&utm_source=taaft&utm_medium=referral",
        "https://free.theresanaiforthat.com/ai/bugasura/",
        "https://free.theresanaiforthat.com/ai/adrian/",
        "https://free.theresanaiforthat.com/ai/bitdefender-ai-skills-checker/",
        "https://free.theresanaiforthat.com/ai/offsend/",
        "https://theresanaiforthat.com/ai/vidnix-ai-image-to-video-generator/?fid=6175",
        "https://free.theresanaiforthat.com/ai/docstoaudio/",
        "https://free.theresanaiforthat.com/@tusharford/leonardo-ai-image-generator-alt/",
        "https://free.theresanaiforthat.com/@upasna-mitra/lexica-art-generator/",
        "https://free.theresanaiforthat.com/@abanjali/famos-artists-generator/",
        "https://free.theresanaiforthat.com/ai/maskerade/?fid=5009",
        "https://free.theresanaiforthat.com/@will-cox-4m8pq/quantum-brain-storming-studio/",
        "https://free.theresanaiforthat.com/@gregoryingram/research-idea-generator/",
        "https://free.theresanaiforthat.com/ai/learn-your-way/"
    ]
    
    # Optional: Perform a DuckDuckGo search to fulfill "Google/YouTube/Scholar" 
    logger.info("Performing deep search for the prompt context...")
    search_results = scraper.search("talkcody theresanaiforthat autonomous agents", max_results=3)
    for res in search_results:
        logger.info(f"Search found: {res.get('title')} - {res.get('href')}")
        if res.get('href'):
            urls_to_scrape.append(res['href'])

    # Scrape the URLs
    logger.info(f"Beginning headless extraction of {len(urls_to_scrape)} URLs...")
    extracted_data = scraper.scrape_urls(urls_to_scrape)
    
    # Save extracted content to training_data and feed to local LLM for insight
    training_dir = os.path.expanduser("~/data_rein/training_data/web_scrapes")
    os.makedirs(training_dir, exist_ok=True)
    
    for url, md_content in extracted_data.items():
        if "[Error]" in md_content:
            logger.warning(f"Skipping failed extraction for {url}: {md_content}")
            continue
            
        # Save raw MD
        filename = f"scrape_{hash(url)}.md"
        filepath = os.path.join(training_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"Source URL: {url}\n\n{md_content}")
            
        logger.info(f"Saved extracted knowledge to {filepath}")
        
    logger.info("Deep search and extraction complete. Knowledge injected into RAG.")

if __name__ == "__main__":
    main()
