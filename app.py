from flask import Flask, render_template, request
import flask_metro

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("landingPage.html")

@app.route("/productQuery", methods=['POST'])
def data():
    productName = request.form['product']
    # userAddress = request.form['address']
    # The function returns a python dictionary
    productInfo = flask_metro.flask_metro(productName)

    return productInfo

@app.route("/results")
def results():
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True)
