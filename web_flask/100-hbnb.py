#!/usr/bin/python3

"""This module defines a Flask app with dynamic routes"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    return render_template('100-hbnb.html',
                           states=storage.all(State),
                           amenities=storage.all(Amenity),
                           places=storage.all(Place))


@app.teardown_appcontext
def close_conn(exception):
    storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
