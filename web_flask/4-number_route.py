#!/usr/bin/python3
"""shebang."""
from flask import Flask


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
    text = text.replace("_", " ")
    return("Python {}".format(text))


@app.toute("/number/<int:n>", strict_slashes=False)
def number(n):
    return("{} is a number".format(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) 
