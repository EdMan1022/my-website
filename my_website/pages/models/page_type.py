from my_website.extensions import db


class PageType(db.Model):
    """
    Model that distinguishes the different types of pages.
    Used to organize the site and fit pages into the correct index.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)

    page = db.relationship('Page', backref=db.backref('page_type'))

    def __init__(self, id=None, name=None):
        if id is not None:
            self.id = id
        self.name = name
