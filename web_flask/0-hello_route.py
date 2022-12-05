#!/usr/bin/python3

"""This module defines a Flask app"""


from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'
