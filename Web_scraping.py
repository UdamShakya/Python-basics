# web_scraping_advanced.py
pip install requests

import csv
import json
import time
import random
import argparse
from typing import List, Dict
import requests
from bs4 import BeautifulSoup

# Reuse a simple retry pattern — small, self-contained, good for examples
def retry_request(session, url, max_retries=3, timeout=10):
    wait = 1.0
    for attempt in range(1, max_retries + 1):
        try:
            resp = session.get(url, timeout=timeout)
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            print(f"[REQUEST] attempt {attempt} for {url} failed: {e}")
            if attempt == max_retries:
                raise
            time.sleep(wait)
            wait *= 1.5

def parse_quotes_from_page(html: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    quotes = []
    for q in soup.find_all("div", class_="quote"):
        text = q.find("span", class_="text").get_text(strip=True)
        author = q.find("small", class_="author").get_text(strip=True)
        tags = [t.get_text(strip=True) for t in q.find_all("a", class_="tag")]
        quotes.append({"text": text, "author": author, "tags": tags})
    return quotes

def scrape_quotes(base_url: str, pages: int = 1, rate_min: float = 0.5, rate_max: float = 1.5):
    session = requests.Session()
    session.headers.update({
        "User-Agent": "github-example-scraper/1.0 (+https://github.com/yourname)"
    })
    all_quotes = []
    for page in range(1, pages + 1):
        url = f"{base_url}/page/{page}/"
        print(f"[SCRAPE] fetching page {page}: {url}")
        resp = retry_request(session, url)
        page_quotes = parse_quotes_from_page(resp.text)
        if not page_quotes:
            print("[SCRAPE] no quotes found on page, stopping.")
            break
        all_quotes.extend(page_quotes)
        # polite sleep
        time.sleep(random.uniform(rate_min, rate_max))
    return all_quotes

def save_to_csv(data: List[Dict], path: str):
    if not data:
        print("[SAVE] no data to save")
        return
    keys = ["text", "author", "tags"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for item in data:
            # join tags as a single string
            item_row = item.copy()
            item_row["tags"] = ",".join(item_row.get("tags", []))
            writer.writerow(item_row)
    print(f"[SAVE] saved {len(data)} rows to {path}")

def save_to_json(data: List[Dict], path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[SAVE] saved {len(data)} objects to {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced scraping demo for quotes.toscrape.com")
    parser.add_argument("--pages", type=int, default=3, help="How many pages to scrape")
    parser.add_argument("--out-csv", default="quotes.csv", help="CSV output path")
    parser.add_argument("--out-json", default="quotes.json", help="JSON output path")
    args = parser.parse_args()

    base = "https://quotes.toscrape.com"
    try:
        quotes = scrape_quotes(base, pages=args.pages)
        save_to_csv(quotes, args.out_csv)
        save_to_json(quotes, args.out_json)
    except Exception as e:
        print("Scraping failed:", e)
