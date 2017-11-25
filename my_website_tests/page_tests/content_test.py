from .base_test import BasePageTest
from my_website.pages import exceptions
import pytest


class ContentTest(BasePageTest):
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
