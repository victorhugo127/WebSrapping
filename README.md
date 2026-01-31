# 🕷️ Web Scraping Project — Selenium & Python

## 📌 Overview

This project is a **web scraping application** built with **Python and Selenium** to extract structured data from a dynamically rendered website (JavaScript-based).

The scraper collects product information in an automated and reliable way, following best practices such as **rate limiting**, **error handling**, and **object-oriented design**.

---

## 🛠️ Technologies Used

- Python 3  
- Selenium WebDriver  
- Google Chrome  
- ChromeDriver  
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```text
webscraper/
│
├── webscraper.py        # Main scraper implementation
├── requirements.txt    # Project dependencies
└── README.md            # Project documentation
```

## ⚙️ How the Scraper Works

The project is structured around a single reusable class called **`WebScraper`**, responsible for:

- Initializing the browser  
- Loading the target website  
- Extracting product data  
- Handling missing elements safely  
- Applying rate limiting  
- Closing the browser correctly  

This design allows easy configuration and future scalability.

---

## 🧠 Main Features

- Headless browser execution  
- Dynamic content handling  
- Structured data extraction  
- Graceful error handling  
- Configurable timeout and rate limit  

---

## 🧩 Extracted Data

For each product, the scraper collects:

- Name  
- Price  
- Description  
- Rating (based on star count)  
- Reviews text  

All data is stored as a **list of dictionaries**, ready for export or database integration.

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install selenium
```

### 2️⃣ Install ChromeDriver

Make sure `chromedriver` is installed and accessible at:

```text
/usr/bin/chromedriver
```

### 3️⃣ Example Usage

```text
from webscraper import WebScraper

scraper = WebScraper(
    base_url="https://example.com",
    timeout=10,
    rate_limit=2
)

scraper.open_site()
products = scraper.get_products()
scraper.close()

print(products)
```

### ⚠️ Error Handling & Rate Limiting

Missing elements are handled using NoSuchElementException

The scraper continues execution even if some product fields are not found

A configurable delay (rate_limit) prevents excessive requests

### 📈 Possible Enhancements

Export data to CSV or JSON

Pagination support

Database integration

Logging system

Proxy and user-agent rotation
