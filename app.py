from flask import Flask, render_template, request
import flask_metro
import flask_longos
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
    # Metro Product Info
    productNameMetro = []
    productPriceMetro = []
    productUnitMetro = []
    # Longos Product Info
    productNameLongos = []
    productPriceLongos = []
    productUnitLongos = []

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

    #print(productName, file=sys.stdout)
    return render_template("results.html")
    

if __name__ == "__main__":
    app.run(debug=True)
