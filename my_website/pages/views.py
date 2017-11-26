from flask import Blueprint

page_blueprint = Blueprint('page_blueprint', __name__, template_folder='templates')


@page_blueprint.route('/')
def hello_world():
    return 'Hello World'
