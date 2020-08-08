import requests
import pprint
import re
import bs4
from bs4 import BeautifulSoup

URL = "https://www.grocerygateway.com/store/groceryGateway/en/search/?text=apple"

page = requests.get(URL)
# print(page)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
# print(type(soup))

products = soup.find("ul", class_="products-gallery")

products_list = []

for product in products:
    if isinstance(product, bs4.element.NavigableString):
        continue

    products_list.append(product)

# RETRIEVES NAMES OF PRODUCTS ON PAGE

for product in products_list:
    print("---------------------------")
    print(product.find("a", {"class":"product-card__name"}).text.strip())
    print(product.find("span", {"class":"cart_reader"}).text.strip() + " " + products_list[0].find("span", {"class":""}).text.strip())
    # print(products_list[0].find("span", {"class":""}).text.strip())
    print("---------------------------")
    print()




