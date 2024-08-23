from selenium import webdriver
from selenium.webdriver.common.by import By

import requests
import time
URL = "https://comic.naver.com/webtoon?tab=mon"

driver = webdriver.Chrome()


driver.get(URL)

ul_class = "ContentList__content_list--q5KXY"


ul = driver.find_element(By.CLASS_NAME, ul_class)
lis = ul.find_elements(By.TAG_NAME, 'li')

for li in lis:
    title, star = li.find_elements(By.CLASS_NAME, "text")
    print(title.text, star.text)

    # for text in texts:
    #     print(text.text)


time.sleep(5)
