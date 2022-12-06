#!/usr/bin/python3
"""This module defines a Flask app with dynamic routes 

This application listen in localhost port 5000.
Routes:
    /
    /hbnb
    /c/<text>
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Prints 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Prints 'C' followed by a <text>."""
    text = text.replace('_', ' ')

    return f'C {text}'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
