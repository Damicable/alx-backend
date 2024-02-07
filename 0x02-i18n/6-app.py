#!/usr/bin/env python3
"""Flask app module with babel"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Any, Union


app = Flask(__name__)


class Config(object):
    """Babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


def get_locale() -> Any:
    """Gets locale request"""
    req_lang = request.args.get('locale')
    if req_lang and req_lang in app.config['LANGUAGES']:
        return req_lang
    if g.user:
        req_lang = g.user.get('locale')
        if req_lang and req_lang in app.config['LANGUAGES']:
            return req_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[int, None]:
    """Gets a user's details"""
    user_id = request.args.get('login_as')
    try:
        return users.get(int(user_id))
    except Exception:
        return None


@app.before_request
def before_request() -> Any:
    """Before request function"""
    g.user = get_user()


@app.route('/')
def home() -> Any:
    """Application home page"""
    if g.user:
        text = gettext('logged_in_as', username=g.user.get('name'))
    else:
        text - gettext('not_logged_in')
    return render_template('5-index.html',
                           title=gettext('home_title'),
                           body=gettext('home_header'),
                           p_text=text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
