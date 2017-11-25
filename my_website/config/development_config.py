from .base_config import BaseConfig


class DevelopmentConfig(BaseConfig):
    """
    Config class used for development.

    Sets debug to true, and changes the name to development config
    """

    def __init__(self):
        super().__init__()
        self.CONFIGURATION_NAME = "Development Config"
        self.DEBUG = True
