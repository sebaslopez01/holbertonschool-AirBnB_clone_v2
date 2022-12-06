#!/usr/bin/python3

"""This module defines a Flask app with dynamic routes"""


from flask import Flask

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    text = text.replace('_', ' ')

    return f'C {text}'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
