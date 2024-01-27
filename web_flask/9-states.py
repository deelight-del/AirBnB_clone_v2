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


@app.route("/states")
@app.route("/states/<id>")
def states(id=None):
    """ Define routing html page to cities by state"""
    states = storage.all(State)
    state = None  # If a given state is not found.
    if id:
        for value in states.values():
            if value.id == id:
                state = value
                break
    return render_template("9-states.html", states=states, id=id, state=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
