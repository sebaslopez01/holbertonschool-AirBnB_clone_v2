#!/usr/bin/python3

"""This module defines a Flask app with dynamic routes"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def states_list(id):
    error = False
    if id is None:
        states = storage.all(State)
        state = None
    else:
        states = None
        state = storage.all(State).get('State.'+id, None)
        if state is None:
            error = True
    return render_template('9-states.html', states=states,
                           state=state, error=error)


@app.errorhandler(404)
def not_found():
    return render_template('9-states.html', states=None,
                           state=None, error=True)


@app.teardown_appcontext
def close_conn(exception):
    storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
