#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://books.toscrape.com/"
response = requests.get(url)
text = response.text

soup = BeautifulSoup(text, "html.parser")
print(soup.prettify())