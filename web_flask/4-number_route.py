#!/usr/bin/python3
""" This module contains the simple implementation of a
simple flask program"""
from flask import Flask

app = Flask(__name__)
# app.url_map.strict_slashes = False


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Simple HBNB route functon"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """The route definition of display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Simple route function to dispaly text passed in url"""
    if (text):
        text = text.replace("_", " ")
        return f"C {text}"  # HTML escaping though...


@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def display_python(text=None):
    """Same as `display_c` but with default value and
    using python instead of c"""
    if text is None:
        text = "is cool"
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """Function to display numbers that are int"""
    if isinstance(n, int):
        return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
