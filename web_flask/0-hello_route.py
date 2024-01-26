#!/usr/bin/python3
""" This module contains the simple implementation of a
simple flask program"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Simple HBNB route functon"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
