#!/usr/bin/env python3
"""Flask app module containing get_timezone method"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from typing import Union, Dict


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """Babel configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def home() -> str:
    """Application home page"""
    return render_template("5-index.html")


@babel.localeselector
def get_locale() -> str:
    """Matches locale with the supported languages"""

    locale = request.args.get('locale')
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user.get('locale')

    header_locale = request.headers.get('locale')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale

    return app.config["BABEL_DEFAULT_LOCALE"]


def get_user() -> Union[Dict, None]:
    """ returns a user dictionary"""
    id = request.args.get('login_as')
    return users.get(int(id), None)


@app.before_request
def before_request() -> None:
    """Before all other functions request"""
    user = get_user()
    if user:
        g.user = user


@babel.timezoneselector
def get_timezone() -> str:
    """gets the timezone"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and 'timezone' in g.user:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return app.config.get('BABEL_DEFAULT_TIMEZONE')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
