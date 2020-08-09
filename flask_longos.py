import requests
import json

import bs4
from bs4 import BeautifulSoup

import googlemaps
import datetime

def flask_longos(user_search_term):
    # DEFAULT SEARCH TERM AS "apple"
    URL = "https://www.grocerygateway.com/store/groceryGateway/en/search/?text={}".format(user_search_term)

    # requests sends HTTP request to the URL above
    page = requests.get(URL)

    # BeautifulSoup parses the HTML content
    soup = BeautifulSoup(page.content, "html.parser")

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

    # Setting up the dictionary to convert to JSON later
    products_dict = {}

    # Cycles through all products on page
    # Retrieves name, price, per unit, and link. Stores it in the products dictionary.
    for product in products_list:

        product_name = product.find("a", {"class":"product-card__name"}).text.strip()
        product_price = product.find("span", {"class":"cart_reader"}).text.strip()
        product_unit = products_list[0].find("span", {"class":""}).text.strip()
        product_link = "https://www.grocerygateway.com/" + products_list[0].find("a", {"class":"product-card__name"})['href']

        products_dict[product_name] = [ product_price, product_unit, product_link ]

    # The JSON object containing the search results
    products_json = json.dumps(products_dict)
    return products_dict

