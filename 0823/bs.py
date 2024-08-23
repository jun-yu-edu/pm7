# 구글 뉴스에 있는 정보를 긁어올 것.

import requests
from bs4 import BeautifulSoup as bs

URL = "https://news.google.com/home?hl=ko&gl=KR&ceid=KR:ko"

response = requests.get(URL)

soup = bs(response.text, "html.parser")

print(soup.find("h1"))


articles = soup.find_all("article")


for article in articles:

    links = article.find_all("a")
    links = article.find_all("a", class_="gPFEn")

    for link in links:
        print(link.text)
