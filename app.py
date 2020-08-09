from flask import Flask, render_template, request
import flask_metro
import flask_longos
import flask_zehrs
import flask_nofrills
import flask_googlemapsearch
import sys

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("landingPage.html")


@app.route("/results", methods=['POST'])
def data():
    productName = request.form['product']
    userAddress = request.form['address']
    userRadius = request.form['radius']
    # The function returns a python dictionary
    productInfoMetro = flask_metro.flask_metro(productName)
    productInfoLongos = flask_longos.flask_longos(productName)
    # productInfoZehrs = flask_zehrs.flask_zehrs(productName)
<<<<<<< HEAD
    productInfoNofrills = flask_nofrills.flask_nofrills(productName)
=======
    # productInfoNofrills = flask_nofrills.flask_nofrills(productName)

>>>>>>> 2476d1bce5840e10000c55345e58c2299f01d210
    nearbyStores = flask_googlemapsearch.flask_googlemapsearch(
        userAddress, userRadius)
    # Metro Product Info
    productNameMetro = []
    productPriceMetro = []
    productUnitMetro = []

    # Longo's Product Info
    productNameLongos = []
    productPriceLongos = []
    productUnitLongos = []

    # Zehr's Product Info
    # productNameZehrs = []
    # productPriceZehrs = []
    # productUnitZehrs = []

    #Nofrill's Product Info
    # productNameNofrills = []
    # productPriceNofrills = []
    # productUnitNofrills = []

    for key, value in productInfoMetro.items():
        # print(key, file=sys.stdout)
        # print(value[0], file=sys.stdout)
        productNameMetro.append(key)
        productPriceMetro.append(value[0])
        productUnitMetro.append(value[1])

    for key, value in productInfoLongos.items():
        productNameLongos.append(key)
        productPriceLongos.append(value[0])
        productUnitLongos.append(value[1])

    for key, value in nearbyStores:
        if (key.startswith('Metro' or 'metro')):
            nearbyMetro = value
        if (key.startswith('Longo' or 'longo')):
            nearbyLongo = value

    # for key, value in productInfoZehrs.items():
    #     productNameZehrs.append(key)
    #     productPriceZehrs.append(value[0])
    #     productUnitZehrs.append(value[1])

    # for key, value in productInfoNofrills.items():
    #     productNameNofrills.append(key)
    #     productPriceNofrills.append(value[0])
    #     productUnitNofrills.append(value[1])

<<<<<<< HEAD
    return productInfoNofrills

=======
    # return productInfoNofrills
>>>>>>> 2476d1bce5840e10000c55345e58c2299f01d210
    #print(productName, file=sys.stdout)

    


    return render_template("results.html", 
        mlength = len(productNameMetro) ,
        metroName = productNameMetro, 
        metroPrice = productPriceMetro,
        metroUnit = productUnitMetro,
        Llength = len(productNameLongos),
        longosName = productNameLongos,
        longosPrice= productPriceLongos,
        longosUnit = productUnitLongos)


if __name__ == "__main__":
    app.run(debug=True)
