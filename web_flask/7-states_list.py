#!/usr/bin/python3

"""This module defines a Flask app with dynamic routes"""


from flask import Flask, render_template
from models import storage

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_conn():
    storage.close()


@app.route('/states_list')
def states_list():
    return render_template('7-states_list.html', states=storage.all('State'))


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
