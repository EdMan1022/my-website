from my_website.pages.models import Content
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
import json


def text_content_function(request):
    """
    API function for text content sections.


    :param request: http request object.
    :return: JSON version of the text content associated with the content block's id
    """
    try:
        content = Content.query.filter_by(id=int(request.data.get('content_id'))).one()
    except KeyError as e:
        raise e
    except MultipleResultsFound as e:
        raise e
    except NoResultFound as e:
        raise e

    return json.dumps({'text_content': content.text_content.value})
