class BasePageError(Exception):
    def __init__(self):
        Exception.__init__(self, 'Base error class for the pages module')
