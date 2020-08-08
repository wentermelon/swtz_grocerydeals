import requests
import bs4
from bs4 import BeautifulSoup

# My cookie from my browser fml, you can comment this out if you don't need it or causes bugs
header = {  "cookie" : "hprl=en; JSESSIONID=C08FD2EACA51415CAB1742443D5EFA4F; NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei=ffffffff09023b1d45525d5f4f58455e445a4a423660;"
                }

URL = 'https://www.metro.ca/en/online-grocery/search?filter=apple&freeText=true'

# Also remove headers=header if you remove my cookie above
page = requests.get(URL, headers=header)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find("div", class_= 'layout--container')
results_2 = results.find("div", {"data-list-name": 'searchResultsList'})

#print(results_2)

#NTS: There can be a lot of pages of hits, what to do if there isn't a 'show all' filter?

# if results != None:
#     print("Results list is not empty!\n")
# else:
#     print("Results list is empty!\n")

#print(results.prettify())

#products = results.find_all('div', {"data-list-name": 'searchResultsList'})
products = results_2.find('div', {"class": 'products-tiles-list products-tiles-list--search searchOnlineResults'})
# if products != None:
#     print("Search results list is not empty!\n")
# else:
#     print("Search results list is empty!\n")

# print(type(products))

#print(products)

# number = 1

# for product in products:
#     #print(type(product))
#     #product.string
#     #unicode_product = unicode(product.string)
#     print("{}".format(number))
#     number+=1
#     # product_name = product.find('div', class_= 'pt-title')
#     # product_price = product.find('span', class_= 'pi-price price-update')
#     # product_unit = product.find('span', class_= 'pi-unit')
#     # #product_link = product.find('a', class_= 'pt-image- product-details-link')
#     # #print(product_link)
#     # if None in (product_name, product_price, product_unit):
#     #     continue
#     # print("{} at {} {}".format(product_name.text.strip(),product_price.text.strip(),product_unit.text.strip()))
#     # print("Buy at: {}".format(product_link.text.strip()))

products_list = []

for product in products:
    if isinstance(product, bs4.element.NavigableString):
        continue

    products_list.append(product)

for product in products_list:

    if product.find("div", {"class":"pt-title"}) == None:
        continue

    # print(product.find("div", {"class":"pt-title"}).text.strip())
    print(product.find("span", {"class":"pi-price"}).text.strip())
