import yaml
import json
import csv
from src.scraper import WebScraper
from src.data_processor import save_csv, save_json
from datetime import datetime


def main():
    url = "https://webscraper.io/test-sites/e-commerce/allinone"

    scraper = WebScraper(url)
    scraper.open()

    products = scraper.scrape_products()
    scraper.close()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    save_csv(products, f"products_{timestamp}.csv")
    save_json(products, f"products_{timestamp}.json")

    print(f"Scraping finalizado com sucesso. {len(products)} produtos extraídos.")


if __name__ == "__main__":
    main()
