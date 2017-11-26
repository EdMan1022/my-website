from my_website.extensions import db


class Page(db.Model):
    """
    SQLAlchemy model that defines a web page.
    """
    id = db.Column(db.Integer, primary_key=True)
    page_type_id = db.Column(db.Integer, db.ForeignKey('page_type.id'))
    created_time = db.Column(db.TIMESTAMP(timezone=True))

    def __init__(self, page_type_id=None, created_time=None, id=None):
        """
        Instantiates a new page object.

        :param page_type_id: integer that identifies the page type this page will belong with. Helps organize the site.
        :param created_time: Time the page was created at
        :param id: primary key of the object. If left as None, then db will use serial value.
        """
        if id is not None:
            self.id = id
        self.page_type_id = page_type_id
        self. created_time = created_time

    pass
