from .base_config import BaseConfig
import os


class DevelopmentConfig(BaseConfig):
    """
    Config class used for development.

    Sets debug to true, and changes the name to development config
    """

    def __init__(self):
        super().__init__()
        self.CONFIGURATION_NAME = "Testing Config"
        self.DEBUG = True
        self.SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')
