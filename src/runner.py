thonimport asyncio
from extractors.instagram_parser import InstagramMentionsScraper
from outputs.exporter import Exporter
import json
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config", "settings.example.json")

def load_config(path):
    import json
    with open(path, "r") as f:
        return json.load(f)

async def main():
    config = load_config(CONFIG_PATH)
    usernames = config.get("usernames", [])
    output_format = config.get("output_format", "json")
    output_file = config.get("output_file", "data/output.json")

    scraper = InstagramMentionsScraper()
    all_results = []

    for username in usernames:
        logging.info(f"Scraping mentions for {username}")
        try:
            results = await scraper.scrape_mentions(username)
            all_results.extend(results)
        except Exception as e:
            logging.error(f"Error scraping {username}: {str(e)}")

    Exporter.export(all_results, output_file, output_format)
    logging.info(f"Data exported to {output_file}")

if __name__ == "__main__":
    asyncio.run(main())