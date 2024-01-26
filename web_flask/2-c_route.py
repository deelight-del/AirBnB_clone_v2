#!/usr/bin/python3
""" This module contains the simple implementation of a
simple flask program"""
from flask import Flask

app = Flask(__name__)


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
    if (text):
        text = text.replace("_", " ")
        return f"C {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
