#!/usr/bin/python3

"""This module defines a Flask app with dynamic routes"""


from flask import Flask, render_template
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


@app.route('/number_template/<int:n>')
def number_template(n: int):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n: int):
    s = f'{n} is even' if n % 2 == 0 else f'{n} is odd'
    return render_template('6-number_odd_or_even.html', n=s)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
