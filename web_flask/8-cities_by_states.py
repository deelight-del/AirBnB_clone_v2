#!/usr/bin/python3
""" This module will list all of
the states in a html page"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def tear_down_app(exception=None):
    """Function to tear down the app context of a request"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
