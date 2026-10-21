import requests
from bs4 import BeautifulSoup
import csv
import json
from urllib.parse import urljoin

# Step 1: Set the website URL
BASE_URL = "https://books.toscrape.com/"
MAX_PAGES = 6

# Store all collected book details
books = []

# Step 2: Visit multiple pages
for page_number in range(1, MAX_PAGES + 1):

    page_url = urljoin(
        BASE_URL,
        f"catalogue/page-{page_number}.html"
    )

    print(f"Scraping page {page_number}...")

    try:
        # Step 3: Download the webpage
        response = requests.get(
            page_url,
            timeout=20
        )
        response.raise_for_status()

        # Step 4: Parse the HTML content
        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # Step 5: Find all book items
        book_items = soup.select("article.product_pod")

        # Step 6: Extract details from each book
        for item in book_items:

            title = item.h3.a["title"]

            price = item.select_one(
                ".price_color"
            ).get_text(strip=True)

            availability = item.select_one(
                ".availability"
            ).get_text(strip=True)

            rating_classes = item.select_one(
                ".star-rating"
            )["class"]

            rating = next(
                (
                    word for word in rating_classes
                    if word != "star-rating"
                ),
                "Unknown"
            )

            product_url = urljoin(
                page_url,
                item.h3.a["href"]
            )

            # Step 7: Store details in a dictionary
            book = {
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "product_url": product_url,
                "page_number": page_number
            }

            books.append(book)

    except requests.RequestException as error:
        print(
            f"Error on page {page_number}: {error}"
        )
        break

# Step 8: Save data to CSV and JSON
if books:

    # Create CSV file
    with open(
        "books_data.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as csv_file:

        writer = csv.DictWriter(
            csv_file,
            fieldnames=books[0].keys()
        )

        writer.writeheader()
        writer.writerows(books)

    # Create JSON file
    with open(
        "books_data.json",
        "w",
        encoding="utf-8"
    ) as json_file:

        json.dump(
            books,
            json_file,
            indent=4,
            ensure_ascii=False
        )

    print("\nScraping completed!")
    print(f"Total books collected: {len(books)}")
    print("CSV saved: books_data.csv")
    print("JSON saved: books_data.json")

else:
    print("No books collected. Please check your connection.")