"""
routes.py
Created: Sat Dec  3 12:13:14 CET 2022

Flask routes declaration file
"""
from flask import current_app as app
from flask import render_template

@app.route("/")
def test():
    """ test page """
    return 'Hello world'
