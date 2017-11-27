from my_website.extensions import db


class TextContent(db.Model):
    """
    SQLAlchemy model for the actual text of a text_content block.
    """

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Text)

    content = db.relationship('Content', backref=db.backref('text_content'))

    def __init__(self, id=None, value=None):
        if id is not None:
            self.id = id
        self.value = value

    pass
