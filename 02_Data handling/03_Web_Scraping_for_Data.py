
# What is Web Scraping?


# Web Scraping = extracting data from websites
# Used for:
# - Data collection
# - Price tracking
# - News/articles scraping



# Required Libraries


# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup



# 1. Get HTML from Website


url = "https://example.com"

headers = {"User-Agent": "Mozilla/5.0"}   # avoid blocking
res = requests.get(url, headers=headers)

html = res.text



# 2. Parse HTML


soup = BeautifulSoup(html, "html.parser")



# 3. Extract Data


# Get title
title = soup.title.text
print("Title:", title)

# Get all links
for link in soup.find_all("a"):
    print(link.get("href"))

# Get specific element
heading = soup.find("h1")
print(heading.text)



# 4. Extract by Class / ID


# By class
items = soup.find_all("div", class_="product")

# By id
main = soup.find("div", id="main")



# 5. Store Data in Pandas


import pandas as pd

data = []

for item in items:
    name = item.find("h2").text
    data.append({"name": name})

df = pd.DataFrame(data)
print(df.head())



# 6. Save Data


df.to_csv("output.csv", index=False)



# IMPORTANT NOTES


# - Always check website terms (legal)
# - Use headers to avoid blocking
# - Some sites need Selenium (JavaScript)
# - Use delay (time.sleep) for safety