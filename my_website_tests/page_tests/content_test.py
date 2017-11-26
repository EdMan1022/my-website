from ..base_test import BaseTest
from my_website.pages import exceptions, models
from my_website.extensions import db
import pytest
from sqlalchemy.orm.exc import FlushError


class ContentTest(BaseTest):
    """
    Test the content model sections of the app
    """

    def test_invalid_content_type(self):
        """
        Calling an invalid content type should return an exception.
        :return:
        """

        with pytest.raises(exceptions.InvalidContentTypeError) as e_info:
            self.client.get('/')

    def test_invalid_page(self):
        """
        Attempting to navigate to an unrecognized route should return a 404 error
        :return:
        """

        with pytest.raises(exceptions.InvalidContentTypeError) as e_info:
            self.client.get('/no/page/exists/here')

    def test_duplicate_content(self):
        """
        Creating content objects with identical ids should raise an error
        :return:
        """

        content = models.Content()
        db.session.add(content)
        db.session.commit()

        with pytest.raises(FlushError) as e_info:
            duplicate_content = models.Content(id=content.id)
            db.session.add(duplicate_content)
            db.session.commit()

