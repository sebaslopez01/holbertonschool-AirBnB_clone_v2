#!/usr/bin/python3

"""This module defines a Flask app"""


from web_flask import app


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'
