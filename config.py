"""
Set Flask Config variables.

Check here: https://hackersandslackers.com/configure-flask-applications/
"""
from os import environ
from dotenv import load_dotenv

BASEDIR = Path(__file__).resolve().parent

load_dotenv(BASEDIR / '.env')

class Config:
    """
    Basic Flask config
    """
    TESTING = True
    SECRET_KEY = environ.get('SECRET_KEY')

    # AWS Secrets
    AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    AWS_KEY_ID = environ.get('AWS_KEY_ID')


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False 
    TESTING = False