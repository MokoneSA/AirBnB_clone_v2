#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list_route():
    """display a HTML page with the states listed in alphabetical order"""
    states = storage.all("State").value()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_db(exception=None):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
