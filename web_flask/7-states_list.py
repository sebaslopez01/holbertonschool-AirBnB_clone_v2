#!/usr/bin/python3

"""This module defines a Flask app with dynamic routes"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def close_conn(exception):
    storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
