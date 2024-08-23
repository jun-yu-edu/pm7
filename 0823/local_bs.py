# 뷰티풀숲

# html을 file 즉, text로 간주해서 parsing

# html ~ xml ~ json ~ dict

from bs4 import BeautifulSoup as bs

with open("simple.html", encoding="utf-8") as f:
    response = f.read()

    soup = bs(response, "html.parser")
    print(soup.find("h1"))
    print(soup.find("h1").text)

    print(soup.find("div"))