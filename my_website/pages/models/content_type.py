from my_website.extensions import db


class ContentType(db.Model):
    """
    Model that distinguishes the different types of content that fill pages,
    and controls which Jinja templates are loaded to handle the content's data.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    template = db.Column(db.Text, unique=True)

    content = db.relationship('Content', backref=db.backref('content_type'))

    def __init__(self, id=None, name=None, template=None):
        if id is not None:
            self.id = id
        self.name = name
        self.template = template
