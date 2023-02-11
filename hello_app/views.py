"""
hello_app: module docstring goes here
"""

# pylint: disable=unused-import

from datetime import datetime
from flask import Flask, render_template
from . import app

@app.route("/")
def home():
    """
    Function docstring goes here
    """
    return render_template("home.html")

@app.route("/about/")
def about():
    """
    Function docstring goes here
    """
    return render_template("about.html")

@app.route("/contact/")
def contact():
    """
    Function docstring goes here
    """
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    """
    Function docstring goes here
    """
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    """
    Function docstring goes here
    """
    return app.send_static_file("data.json")
