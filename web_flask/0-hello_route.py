#!/usr/bin/python3

"""This module defines a Flask app"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'
