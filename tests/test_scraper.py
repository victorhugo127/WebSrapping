import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.scraper import WebScraper


def test_scraper_initialization():
    url = "https://example.com"
    scraper = WebScraper(url)

    assert scraper.url == url
    assert scraper.driver is not None
