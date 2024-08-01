#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    modified_text = text.replace('_', ' ')
    return f"C {modified_text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python_text(text):
    modified_text = text.replace('_', ' ')
    return f"Python {modified_text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
