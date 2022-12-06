#!/usr/bin/python3

"""This module defines a Flask app with dynamic routes"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text: str):
    text = text.replace('_', ' ')

    return 'C {}'.format(escape(text))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text: str):
    text = text.replace('_', ' ')

    return 'Python {}'.format(escape(text))


@app.route('/number/<int:n>')
def number_route(n: int):
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
