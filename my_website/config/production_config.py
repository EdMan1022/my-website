from .base_config import BaseConfig


class ProductionConfig(BaseConfig):

    def __init__(self):
        super().__init__()
        self.CONFIGURATION_NAME = "Production Config"
