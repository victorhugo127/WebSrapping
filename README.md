# 🕷️ Web Scraping Project — Selenium & Python

## 📌 Overview

This project is a **web scraping application** built with **Python and Selenium** to extract structured data from a dynamically rendered website (JavaScript-based).

The scraper collects product information in an automated and reliable way, following best practices such as **rate limiting**, **error handling**, and **object-oriented design**.

---

## 🛠️ Technologies Used

- Python 3.12
- Selenium WebDriver
- Chromium / ChromeDriver
- Pandas
- Pytest
- Docker & Docker Compose
- YAML configuration

---

## 📂 Project Structure

```text
web_scraper/
│
├── src/
│   ├── __init__.py
│   ├── scraper.py          # Selenium scraper logic
│   └── data_processor.py   # CSV / JSON data handling
│
├── tests/
│   └── test_scraper.py     # Unit tests
│
├── config/
│   └── config.yaml         # Scraper configuration
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── web_scraper.py          # Main execution script
├── requirements.txt
└── README.md
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

The data is stored as:

CSV file with timestamp

JSON file with timestamp

---

## ▶️ How to Run the Project

### 1️⃣ Create and activate virtual environment

```text
python3 -m venv venv
source venv/bin/activate
```
### 2️⃣ Install dependencies

```text
pip install -r requirements.txt
```

### 3️⃣ Run the scraper

```text
python web_scraper.py
```

### 🐳 Run with Docker
Build and start container

```text
docker-compose up --build
```

The scraper will execute automatically and extract product data.

### 🧪 Running Tests

```text
pytest
```

### ⚠️ Error Handling & Rate Limiting

Missing elements are handled using NoSuchElementException

The scraper continues execution even if some product fields are not found

A configurable delay (rate_limit) prevents excessive requests

---

### 📈 Possible Enhancements

Export data to CSV or JSON

Pagination support

Database integration

Logging system

Proxy and user-agent rotation
