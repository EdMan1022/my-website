from dotenv import load_dotenv
from os.path import join, dirname
import os

env_path = join(dirname(__file__), '.env')
load_dotenv(env_path)


class BaseConfig(object):
    """
    Parent configuration class for the flask app.

    An instance of this contains the common things required to run the app across all configurations.
    Flask can import the config values directly from a config instance.
    """

    def __init__(self):
        self.CONFIGURATION_NAME = 'Base Config'
        self.SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
        self.DEBUG = False
        self.SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.APP_NAME = "my_website"

    def __str__(self):
        return self.CONFIGURATION_NAME
