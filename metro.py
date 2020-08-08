import requests
from bs4 import BeautifulSoup

URL = 'https://www.metro.ca/en/online-grocery/search?filter=apple&freeText=true'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find("div", class_= 'layout--container')

#NTS: There can be a lot of pages of hits, what to do if there isn't a 'show all' filter?

if results != None:
    print("Results list is not empty!\n")
else:
    print("Results list is empty!\n")

#print(results.prettify())

products = results.find_all('div', {"data-list-name": 'searchResultsList'})
#products = results.find_all('div', {"class": 'products-tiles-list  products-tiles-list--search searchOnlineResults'})
if products != None:
    print("Hi part 2!\n")
else:
    print("Hey part 2!\n")

print(type(products))

#print(products)

#number = 1

for product in products:
    #print("{}".format(number))
    #number+=1
    product_name = product.find('div', class_= 'pt-title')
    product_price = product.find('span', class_= 'pi-price price-update')
    product_unit = product.find('span', class_= 'pi-unit')
    #product_link = product.find('a', class_= 'pt-image- product-details-link')
    #print(product_link)
    if None in (product_name, product_price, product_unit):
        continue
    print("{} at {} {}".format(product_name.text.strip(),product_price.text.strip(),product_unit.text.strip()))
    #print("Buy at: {}".format(product_link.text.strip()))

