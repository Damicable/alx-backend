#!/usr/bin/env python3
"""0-app flask module"""

from flask import Flask, render_template
from typig import Any


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home() -> Any:
    """Home page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
