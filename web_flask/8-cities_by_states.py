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


@app.route("/cities_by_states")
def cities_by_state():
    """ Define routing html page to cities by state"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
