# WebSrapping

📌 Project Overview

This project is a web scraping application developed in Python using Selenium WebDriver.
The goal is to automatically collect product data from a dynamic website, handling pages rendered with JavaScript.

The scraper extracts structured information such as:

Product name

Price

Description

Rating

Reviews

The project was built with code organization, scalability, and best practices in mind, simulating a real-world data collection scenario.

🛠️ Tech Stack

Python 3

Selenium

Chrome WebDriver

Object-Oriented Programming (OOP)

📂 Project Structure
webscraper/
│
├── webscraper.py        # Main scraper class
├── requirements.txt    # Project dependencies
└── README.md            # Project documentation

⚙️ How It Works

The scraper is implemented using a class-based architecture, allowing easy reuse and configuration.

🔹 Main Class: WebScraper

The WebScraper class is responsible for:

Initializing the browser

Opening the target website

Extracting product data

Applying rate limits

Closing the browser safely

🧠 Code Explanation
1️⃣ Initialization
def __init__(self, base_url: str, timeout: int, rate_limit: int):


base_url: Website URL to scrape

timeout: Maximum page load time

rate_limit: Delay between requests to avoid overload

This design makes the scraper configurable and reusable.

2️⃣ WebDriver Setup
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


Runs Chrome in headless mode

Optimized for Docker/Linux environments

Improves performance and stability

3️⃣ Opening the Website
def open_site(self):
    self.driver.get(self.base_url)


Loads the target page before data extraction.

4️⃣ Extracting Product Data
def get_products(self):


The scraper:

Locates product cards using CSS classes

Extracts text-based fields

Counts rating stars dynamically

Handles missing elements using exception handling

Extracted data is stored in a list of dictionaries, making it easy to export later (JSON, CSV, database, etc.).

5️⃣ Error Handling
except NoSuchElementException:
    continue


If a product card is missing an element, the scraper:

Skips the item

Continues execution safely

This prevents the scraper from crashing.

6️⃣ Rate Limiting
time.sleep(self.rate_limit)


Adds a delay between operations to:

Avoid server overload

Reduce detection/blocking risks

7️⃣ Closing the Browser
def close(self):
    self.driver.quit()


Ensures resources are released properly after execution.

▶️ How to Run
1. Install dependencies
pip install selenium

2. Ensure ChromeDriver is installed

Make sure chromedriver is available at:

/usr/bin/chromedriver


Or update the path in the code if necessary.

3. Example Usage
scraper = WebScraper(
    base_url="https://example.com",
    timeout=10,
    rate_limit=2
)

scraper.open_site()
products = scraper.get_products()
scraper.close()

print(products)

📈 Possible Improvements

Export data to CSV or JSON

Add pagination support

Integrate database storage

Add logging system

Implement proxy rotation
