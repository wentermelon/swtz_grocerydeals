import requests
import bs4
from bs4 import BeautifulSoup

# DEFAULT SEARCH TERM AS "apple"
URL = "https://www.grocerygateway.com/store/groceryGateway/en/search/?text=apple"

# requests sends HTTP request to the URL above
page = requests.get(URL)
# print(page)

# BeautifulSoup parses the HTML content
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
# print(type(soup))

# Finds the ul (unordered list) for the products on the page
products = soup.find("ul", class_="products-gallery")

# Create empty list to store relevant elements
products_list = []

# Longos specifically has NavigableString and Tag elements
# NavigableString are useless and we only need Tag elements
for product in products:
    if isinstance(product, bs4.element.NavigableString):
        continue

    products_list.append(product)

# Prints each product and their prices on the page
for product in products_list:
    print("---------------------------")
    print(product.find("a", {"class":"product-card__name"}).text.strip())
    print(product.find("span", {"class":"cart_reader"}).text.strip() + " " + products_list[0].find("span", {"class":""}).text.strip())
    # print(products_list[0].find("span", {"class":""}).text.strip())
    print("---------------------------")
    print()




