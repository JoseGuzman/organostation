"""
Flask Application Factory

Check for aditional information
https://hackersandslackers.com/flask-application-factory/
"""
from flask import Flask
from flask_bootstrap import Bootstrap


def init_app() -> Flask:
    """
    Creates the Flask app object
    """
    # Initialize core application
    myapp = Flask(__name__, instance_relative_config=False)
    myapp.config.from_object("config.DevConfig")  # see config.py

    # Initialize plugings
    Bootstrap(myapp)

    # The app context
    with myapp.app_context():
        # Include routes
        from . import routes

        # dashboards
        return myapp
