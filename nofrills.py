import requests
import json
import time

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

search_term = "apple"

driver.get("https://www.nofrills.ca/search?search-bar={}".format(search_term))

# Wait for driver to load the website and JS scripts before retrieving HTML
time.sleep(5)

# TODO: extend this functionality to select the correct province
# Click on "British Columbia" button 
driver.find_element_by_css_selector("#site-layout > div.modal-dialog.modal-dialog--region-selector > div.modal-dialog__content > div > div > ul > li:nth-child(2) > button").click()

# Wait for driver to load the website and JS scripts before retrieving HTML
time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

search_results = soup.find("ul", {"data-cruller":"product-tile-group"})

products_dict = {}

for result in search_results:

    product_name = result.find("span", {"class":"product-name__item"}).text.strip()
    product_price = result.find("span", {"class":"price__value"}).text.strip()
    product_unit = result.find("span", {"class":"price__unit"}).text.strip()
    product_link = "https://www.nofrills.ca" + result.find("a", {"class": "product-tile__details__info__name__link"})["href"]

    products_dict[product_name] = [ product_price, product_unit, product_link ]

products_json = json.dumps(products_dict)
print(products_json)

driver.quit()