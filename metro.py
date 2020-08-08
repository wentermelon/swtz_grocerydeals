import requests
import bs4
from bs4 import BeautifulSoup
import json

URL = 'https://www.metro.ca/en/online-grocery/search?sortOrder=relevance&filter=apple&freeText=true'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

#Thinning out HTML content
results = soup.find("div", class_= 'layout--container')
results_2 = results.find("div", {"data-list-name": 'searchResultsList'})
products = results_2.find('div', {"class": 'products-tiles-list products-tiles-list--search searchOnlineResults'})

products_list = []
products_dict = {}
MetroURL = "https://metro.ca"

#If object is a bs4.NavigableString, skip it so that products_list will only include bs4.Tag objects
for product in products:
    if isinstance(product, bs4.element.NavigableString):
        continue

    products_list.append(product)

#For each object, if an attribute is missing, skip it
for product in products_list:
    if product.find("div", {"class":"pt-title"}) == None:
        continue
    product_name = product.find("div", {"class": 'pt-title'}).text.strip()

    if product.find("span", {"class": "pi-price price-update"}) == None:
        continue
    product_price = product.find("span", {"class": "pi-price price-update"}).text.strip()

    if product.find("span", {"class": "pi-unit"}) == None:
        continue
    product_unit = product.find("span", {"class": "pi-unit"}).text.strip()

    if product.find('a', {"class": "pt--image product-details-link"})['href'] == None:
        continue
    #NTS: Link is already a string
    product_link = product.find('a', {"class": "pt--image product-details-link"})['href'].strip()
    product_link = MetroURL + product_link

    print("{} at {} {}".format(product_name, product_price, product_unit))
    print("Buy at: {}".format(product_link))
    print()

    #Cleaning up output
    if "\xa0" in product_unit:
        print("TEST")
        product_unit = product_unit.replace("\xa0", "")

    #Add it to dictionary
    products_dict[product_name] = [product_price, product_unit, product_link]

#NTS: There is a SyntaxError: JSON.parse: but it doesn't actually interfere with anything
products_json = json.dumps(products_dict)
print(products_json)