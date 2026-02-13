import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.scraper import WebScraper

URL = "https://webscraper.io/test-sites/e-commerce/allinone"

@pytest.fixture
def scraper():
    scraper = WebScraper(URL)
    scraper.open()
    yield scraper
    scraper.close()

def test_scrape_products_returns_list(scraper):
    products = scraper.scrape_products()
    print(products[:3])
    assert isinstance(products, list)

def test_product_has_required_fields(scraper):
    products = scraper.scrape_products()

    assert len(products) > 0
    product = products[0]

    assert "name" in product
    assert "price" in product
    assert "description" in product
    assert "rating" in product
    assert "reviews" in product

def test_show_products(scraper):
    products = scraper.scrape_products()
    for p in products[:5]:
        print(p)
    assert len(products) > 0
