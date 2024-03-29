#!/usr/bin/env python3
"""Get_locale module"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """Babel configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def home() -> str:
    """index page"""
    return render_template("2-index.html")


@babel.localeselector
def get_locale() -> str:
    """Gets locale supported languages"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == '__main__':
    app.run(debug=True)
