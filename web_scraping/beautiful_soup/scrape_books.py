#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://books.toscrape.com/"

def scrape_book_titles(url):
    page_url = "catalogue/page-1.html"

    # Iterating over the pages.
    num_pages = 0
    while page_url:
        response = requests.get(url + page_url)
        text = response.text
        soup = BeautifulSoup(text, "html.parser")

        a_tags = soup.find_all("a")
        for a_tag in a_tags:
            print(a_tag.get("title"))

        next_link = soup.find("a", href=True, string="next")
        if next_link:
            page_url = next_link["href"]
        else:
            page_url = None



if __name__ == "__main__":
    scrape_book_titles(url)