#!/usr/bin/env python3
"""Module to bootstrap a Flask app using babel"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/', strict_slashes=False)
def home() -> str:
    """Home page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
