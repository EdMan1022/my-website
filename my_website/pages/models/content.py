from my_website.extensions import db


class Content(db.Model):
    """
    SQLAlchemy model for the content that fills sections of the body of a web page.

    A page can have multiple contents.
    Each content is associated with a content type, which determines what templates are used for the content.
    """

    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'))
    content_type_id = db.Column(db.Integer, db.ForeignKey('content_type.id'))
    created_time = db.Column(db.TIMESTAMP(timezone=True))

    def __init__(self, id=None, content_type_id=None, created_time=None):
        if id is not None:
            self.id = id
        self.content_type_id = content_type_id
        self.created_time = created_time

    pass
