from .base_page_error import BasePageError


class InvalidContentTypeError(BasePageError):
    def __init__(self):
        Exception.__init__(self,
                           'The function attempted to call a non-existent content type')
