#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
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
