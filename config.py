"""
Set Flask Config variables.

Check here: https://hackersandslackers.com/configure-flask-applications/
Check here to use S3 for static content: 
https://abhishekm47.medium.com/serve-static-assets-on-s3-bucket-a-complete-flask-guide-fbe128d97e71
"""
from os import environ
from pathlib import Path

from dotenv import load_dotenv

BASEDIR = Path(__file__).resolve().parent

load_dotenv(BASEDIR / '.env')

class Config:
    """
    Basic Flask config
    """
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')

    # AWS Access
    AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    AWS_KEY_ID = environ.get('AWS_KEY_ID')
    AWS_REGION = environ.get('AWS_REGION')

    ACL = 'public-read'
    FLASKS3_BUCKET_NAME = environ.get('FLASKS3_BUCKET_NAME')

class DevConfig(Config):
    """
    Flask config file for Development
    """
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

class ProdConfig(Config):
    """
    Flask config file for Production
    """
    FLASK_ENV = 'production'
    DEBUG = False 
    TESTING = False