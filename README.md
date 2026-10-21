Datheon Python for Data Engineering

Task 1: Autonomous Web Scraper & Data Extractor

"Python" (https://img.shields.io/badge/Python-3.x-blue?logo=python)
"BeautifulSoup" (https://img.shields.io/badge/BeautifulSoup-Web_Scraping-green)
"Requests" (https://img.shields.io/badge/Requests-HTTP_Client-orange)
"Status" (https://img.shields.io/badge/Project-Completed-brightgreen)

📌 Project Overview

The Autonomous Web Scraper & Data Extractor is a Python-based project developed as part of the Datheon Python for Data Engineering program.

The project collects structured book information from "Books to Scrape" (https://books.toscrape.com/), a website designed for practicing web scraping. It automates data extraction across multiple pages and exports the collected information into CSV and JSON formats for further analysis.

🎯 Objectives

- Automate the collection of book information from a website.
- Extract structured data from HTML pages.
- Handle pagination to collect data from multiple pages.
- Store the extracted data in reusable file formats.
- Practice web scraping and basic data engineering concepts.

✨ Key Features

- Automated extraction: Collects book titles, prices, ratings, and availability.
- Pagination support: Navigates through multiple pages.
- Structured data: Organizes extracted information into consistent fields.
- CSV export: Saves records in "books_data.csv".
- JSON export: Saves records in "books_data.json".
- Reusable script: Runs from the command line using Python.

🛠️ Technologies Used

Technology| Purpose
Python| Core programming language
Requests| Sends HTTP requests to retrieve webpages
BeautifulSoup4| Parses HTML and extracts information
CSV| Stores data in tabular format
JSON| Stores structured data

📂 Project Structure

Datheon_Python_Projects/
│
├── README.md
│
└── Task1_Web_Scrapper/
    ├── web_scrapper.py
    ├── books_data.csv
    └── books_data.json

Note: The generated CSV and JSON files will appear after the script runs successfully. The filenames and folder structure above should match your actual project.

⚙️ Installation and Setup

Prerequisites

- Python 3 installed
- pip package manager
- Internet connection

Step 1: Clone the Repository

git clone https://github.com/pratikshaswami31/Datheon_Python_Projects.git

Step 2: Open the Project Folder

cd Datheon_Python_Projects

Step 3: Install Dependencies

python -m pip install requests beautifulsoup4

Step 4: Run the Web Scraper

python Task1_Web_Scrapper/web_scrapper.py

📊 Output Files

After successful execution, the program generates:

1. "books_data.csv"

Stores extracted book information in rows and columns, suitable for Excel and data analysis.

2. "books_data.json"

Stores extracted book information as structured JSON records, suitable for use in Python applications and data pipelines.

🔍 Data Fields

The scraper is designed to collect the following fields:

Field| Description
"title"| Name of the book
"price"| Listed book price
"availability"| Availability status
"rating"| Book rating
"product_url"| Link to the book's product page
"page_number"| Page from which the book was collected

🧠 What I Learned

- Sending HTTP requests with Python.
- Parsing HTML content using BeautifulSoup.
- Extracting structured information from webpages.
- Handling multi-page website navigation.
- Exporting data into CSV and JSON files.
- Organizing a Python project for version control with Git and GitHub.

🔐 Responsible Web Scraping

This project uses a practice website intended for learning web scraping. When scraping other websites, always review their terms of service, respect their access policies, and avoid sending excessive requests.

👩‍💻 Author

Pratiksha Swami

Datheon Python for Data Engineering Program

---

This project demonstrates practical Python web scraping, data extraction, and file-based data storage.