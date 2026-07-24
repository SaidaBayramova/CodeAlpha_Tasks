"""
scraper.py
----------
Task 1: Web Data Collection

Scrapes book data (title, price, rating, availability, category) from
https://books.toscrape.com — a public sandbox site built specifically
for practicing web scraping, so it is safe and legal to use for this
project.

Usage:
    python scraper.py

Output:
    data/raw_data.csv
"""

import time
import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"
OUTPUT_PATH = "data/raw_data.csv"

# Star ratings on the site are written as CSS classes ("One", "Two", ...)
RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    )
}


def get_soup(url: str) -> BeautifulSoup:
    """Fetch a URL and return a parsed BeautifulSoup object."""
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def parse_book_card(card, category: str) -> dict:
    """Extract fields from a single book card on a listing page."""
    title = card.h3.a["title"].strip()

    price_text = card.select_one(".price_color").get_text(strip=True)
    price = price_text.replace("Â£", "").replace("£", "").strip()

    availability = card.select_one(".availability").get_text(strip=True)

    rating_class = card.select_one("p.star-rating")["class"]
    # class list looks like ["star-rating", "Three"]
    rating_word = [c for c in rating_class if c != "star-rating"][0]
    rating = RATING_MAP.get(rating_word, None)

    return {
        "title": title,
        "price": price,
        "rating": rating,
        "availability": availability,
        "category": category,
    }


def get_category(book_url: str) -> str:
    """Visit a book's product page to read its category from the breadcrumb."""
    soup = get_soup(book_url)
    breadcrumb = soup.select("ul.breadcrumb li a")
    # breadcrumb[0] = Home, breadcrumb[1] = category, breadcrumb[2] = book title link
    if len(breadcrumb) >= 2:
        return breadcrumb[1].get_text(strip=True)
    return "Unknown"


def scrape_all_pages(max_pages: int = 5) -> list:
    """
    Crawl the paginated book catalogue and collect structured records.

    max_pages limits how many listing pages are scraped, to keep the
    demo run quick. Set to None to scrape the entire catalogue.
    """
    records = []
    page_num = 1
    url = START_URL

    while url:
        print(f"Scraping listing page {page_num}: {url}")
        soup = get_soup(url)
        cards = soup.select("article.product_pod")

        for card in cards:
            relative_link = card.h3.a["href"]
            book_url = BASE_URL + relative_link.replace("catalogue/", "")
            category = get_category(book_url)
            record = parse_book_card(card, category)
            records.append(record)
            time.sleep(0.2)  # be polite to the server

        next_link = soup.select_one("li.next a")
        if next_link and (max_pages is None or page_num < max_pages):
            url = BASE_URL + next_link["href"]
            page_num += 1
        else:
            url = None

    return records


def save_to_csv(records: list, path: str) -> None:
    if not records:
        print("No records scraped, nothing to save.")
        return

    fieldnames = list(records[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"Saved {len(records)} records to {path}")


if __name__ == "__main__":
    data = scrape_all_pages(max_pages=5)
    save_to_csv(data, OUTPUT_PATH)
