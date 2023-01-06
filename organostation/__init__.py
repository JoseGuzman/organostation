"""
Main Flask Application Factory with Blueprints.
Assets are compiled with Flask-Assets from less files

Check for aditional information
https://hackersandslackers.com/flask-application-factory/
"""
from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # initialize the database as global variable


def create_app() -> Flask:
    """Creates the Flask app object and returns it"""
    # Initialize core application
    myapp = Flask(
        __name__,
        instance_relative_config=False,
    )

    myapp.config.from_object("config.DevConfig")  # see config.py

    db.init_app(myapp)  # initialize the database with the app

    # Initialize Assets Environment
    assets = Environment()  # create an assets environment for styling
    assets.init_app(myapp)  # initialize it with the app

    # The app context
    with myapp.app_context():
        # Import parts of our application
        from .assets import compile_static_assets

        # routes related to unregistered users
        from .home.views import home_bp

        # from .guest.routes import guest_bp
        # routes related to registered users
        # from .profile.routes import profile_bp

        db.create_all()  # create database tables for our data models

        # Register Blueprints
        myapp.register_blueprint(home_bp)

        # dashboards

        # Compile static assets for styling
        compile_static_assets(assets)

        return myapp
