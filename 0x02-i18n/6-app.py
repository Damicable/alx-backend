#!/usr/bin/env python3
"""Flask app module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
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
    """index page"""
    return render_template("5-index.html")


@babel.localeselector
def get_locale() -> str:
    """Gets the locale supported languages"""

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
    """Returns a user dictionary"""
    id = request.args.get('login_as')
    if id is not None:
        try:
            user_id = int(id)
            return users.get(user_id)
        except (ValueError, TypeError):
            pass
    return None


@app.before_request
def before_request() -> None:
    """executed before all other functions"""
    user = get_user()
    if user:
        g.user = user


if __name__ == '__main__':
    app.run(debug=True)
