"""
Set Flask Config variables.

Check here: https://hackersandslackers.com/configure-flask-applications/
Check here to use S3 for static content: 
https://abhishekm47.medium.com/serve-static-assets-on-s3-bucket-a-complete-flask-guide-fbe128d97e71
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
    ACL = 'public-read'
    FLASKS3_BUCKET_NAME = environ.get('FLASKS3_BUCKET_NAME')


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False 
    TESTING = False
