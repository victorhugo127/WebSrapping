import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebScraper:
    def __init__(self, url: str):
        self.url = url
        self.driver = self._init_driver()

    def _init_driver(self):
        options = webdriver.ChromeOptions()

        # Chromium Snap
        options.binary_location = "/snap/bin/chromium"
        
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")

        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(30)
        return driver

    def open(self):
        self.driver.get(self.url)
        time.sleep(2)

    def scrape_products(self):
        products = []

        cards = self.driver.find_elements(By.CLASS_NAME, "thumbnail")

        for card in cards:
            try:
                products.append({
                    "name": card.find_element(By.CLASS_NAME, "title").text,
                    "price": card.find_element(By.CLASS_NAME, "price").text,
                    "description": card.find_element(By.CLASS_NAME, "description").text,
                    "rating": len(card.find_elements(By.CLASS_NAME, "glyphicon-star")),
                    "reviews": card.find_element(By.CLASS_NAME, "ratings").text
                })
            except NoSuchElementException:
                continue

        return products

    def close(self):
        self.driver.quit()



