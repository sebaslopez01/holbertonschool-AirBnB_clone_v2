#!/usr/bin/python3

"""This module defines a Flask app with dynamic routes"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text: str):
    text = text.replace('_', ' ')

    return f'C {text}'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
