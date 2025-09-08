#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
print(soup.prettify())
