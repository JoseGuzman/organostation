"""
Flask Application Factory
"""
from flask import Flask

def init_app() -> Flask:
    """
    Creates the Flask app object according 
    """
    app = Flask(__name__, instance_relative_config = False)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes
        
        return app
