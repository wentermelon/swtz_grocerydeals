from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("landingPage.html")


@app.route("/productQuery", methods=['POST'])
def data():
    productName = request.form['product']
    userAddress = request.form['address']
    return productName + " , " + userAddress


if __name__ == "__main__":
    app.run(debug=True)
