from flask import Blueprint

page_blueprint = Blueprint('pages', __name__, template_folder='templates')

@pages.route('/')
def hello_world():
    return 'Hello World'
