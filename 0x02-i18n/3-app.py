#!/usr/bin/env python3
"""Flask app module with babel"""


from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from typing import Any


app = Flask(__name__)


class Config(object):
    """Babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home() -> Any:
    """Application home page"""
    return render_template('3-index.html',
                           title=gettext('home_title'),
                           body=gettext('home_header'))


def get_locale() -> Any:
    """Gets local request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
