from flask import Flask
from my_website.config import DevelopmentConfig
from my_website.extensions import db
from my_website.pages import page_blueprint


def create_app(config=DevelopmentConfig()):
    """
    Create the Flask application object, and link it to the declarative base

    :param config:
    :return: The flask application object
    """

    app = Flask(config.APP_NAME)
    app.config.from_object(config)
    app.register_blueprint(page_blueprint)

    db.init_app(app)
    db.app = app

    return app
