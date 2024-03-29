"""
Main Flask Application Factory with Blueprints.
Assets are compiled with Flask-Assets from .less files

Shell context (only available in development):
(see here: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
Typing flask shell will permit access to the app and database:
>>> flask shell
>>> Python 3.9.16 (main, Dec  7 2022, 10:15:43)
[Clang 14.0.0 (clang-1400.0.29.202)] on darwin
App: organostation
Instance: /Users/joseguzman/git/og/instance
>>> app
>>> <Flask 'organostation'>
>>> db
>>> <SQLAlchemy sqlite:////Users/joseguzman/git/og/instance/organostation_users.db>
>>> User
>>> User <class 'organostation.models.User'>
>>> myuser = User.query.filter_by(username='jose').first()
>>> myuser = User.query.filter(User.email == 'jose.guzman@example.com').first()
>>> db.session.commit()
"""
from flask import Flask
from flask_assets import Environment
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # initialize the database as GLOBAL
login_manager = LoginManager()


def create_app() -> Flask:
    """Creates the Flask app object and returns it"""
    # Initialize core application
    myapp = Flask(
        __name__,
        instance_relative_config=False,
    )

    myapp.config.from_object("config.DevConfig")  # see config.py

    db.init_app(myapp)  # initialize the database with the app
    login_manager.init_app(myapp)

    # Initialize Assets Environment
    assets = Environment()  # create an assets environment for styling
    assets.init_app(myapp)  # initialize it with the app

    # provide access to User model in shell
    @myapp.shell_context_processor
    def make_shell_context():
        """makes User model available in shell context"""
        from .models import User

        return {"User": User}

    # The app context
    with myapp.app_context():
        if myapp.config["DEBUG"]:  # active in DevConfig class:
            # Import parts of our application
            from .assets import compile_static_assets

        # Register Blueprints
        from .main.views import main_bp
        from .tutorials.views import tutorials_bp

        db.create_all()  # create sql tables for our data models

        # Register Blueprints
        myapp.register_blueprint(main_bp)
        myapp.register_blueprint(tutorials_bp)

        # dashboards
        from .dashboards.visualoid import test

        myapp = test(myapp)

        if myapp.config["DEBUG"]:  # active in DevConfig class:
            # Compile static assets for styling
            compile_static_assets(assets)

        return myapp
