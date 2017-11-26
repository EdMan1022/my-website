from flask import Blueprint, request
from .helper_functions import text_content_function


text_content = Blueprint('text_content', __name__, template_folder='templates')


@text_content.route('/api/text_content')
def text_content_view():
    """
    API route to handle text content jquery calls.

    :return:
    """
    text_content_response = text_content_function(request)
    return text_content_response

