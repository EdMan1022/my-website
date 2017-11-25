from flask_testing import TestCase
from my_website.create_app import create_app
from my_website.config import TestConfig
from my_website.extensions import db


class BaseTest(TestCase):
    """
    Base class for any tests for the voxco_survey_analysis app

    Includes methods for creating the database connection and initializing the application object.
    Different child classes should be made for testing each blueprint.
    """

    def create_app(self):
        """
        Method that initializes a flask application object.

        Required method for flask_testing.TestCase classes,
        which is why we don't just use the create_app function in setUp.
        :return: Flask instance
        """
        app = create_app(config=TestConfig())
        db.app = app
        return app

    def setUp(self):
        """
        Creates the tables in the empty test database for each test.

        Creates all of the tables using the declarative base object.
        -------------------**IMPORTANT NOTE**-----------------------
        This does not CREATE the test database itself.
        The actual database defined in TestConfig needs to already have been created,
        using a database client, the command line, or a web console for the database service.
        ------------------------------------------------------------

        The base method here doesn't fill these tables with any data,
        but if data is required for every test in a blueprint,
        then the Child test class associated with that blueprint may
        alter this method to insert test data into the database.
        :return: None
        """
        db.create_all()
        db.session.commit()

    def tearDown(self):
        """
        Clears the test database after every test.

        Drops all of the tables in the database,
        but doesn't delete the actual database itself.
        :return: None
        """
        db.session.remove()
        db.drop_all()
