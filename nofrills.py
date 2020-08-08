import requests
import json

import bs4
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os

os.chdir(os.path.dirname(__file__))

DRIVER_PATH = "chromedriver.exe"
options = Options()
options.headless = True

driver = webdriver.Chrome(  executable_path=DRIVER_PATH, 
                            options=options
                            )

driver.get("https://google.com")
print("Successfully opened")
print(driver.page_source)
driver.quit()
print("sucessfuly closed")

# # Feel free to change this to user input
# search_term = "apple"

# # DEFAULT SEARCH TERM AS "apple"
# URL = "https://www.nofrills.ca/search?search-bar={}".format(search_term)

# # requests sends HTTP request to the URL above
# page = requests.get(URL)
# # print(page)

# # BeautifulSoup parses the HTML content
# soup = BeautifulSoup(page.content, "html.parser")

# print(soup)

# search_results = soup.find("div", {"class": "product-grid__results__products"})
# # print(type(search_results))


