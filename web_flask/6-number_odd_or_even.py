""" shebang. """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ first end point """
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ second end point """
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ capture var """
    text = text.replace("_", " ")
    return("C {}".format(text))


@app.route("/python", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>")
def python(text):
    """capture variable python"""
    text = text.replace("_", " ")
    return("Python {}".format(text))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ number integer """
    return("{} is a number".format(n))


@app.route("/number_template/<int:n>")
def number_template(n):
    number = "Number: {}".format(n)
    return render_template("5-number.html", number=number)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_even(n):
    """is odd or even"""
    if (n % 2 == 0):
        number = "Number: {} is even".format(n)
    else:
        number = "Number: {} is odd".format(n)
    return render_template("6-number_odd_or_even.html", number=number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
