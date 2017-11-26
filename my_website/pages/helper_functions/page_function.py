from ..models import Page, PageType
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound


def page_function(request, page_type, page_identifier):
    """
    Function that returns the correct database object for the requested page

    :param request: The flask http request object
    :param page_type: stripped from the url. String identifier for the page type.
    :param page_identifier: Stripped from the url. ID or name of the page.
    :return: page data
    """

    try:
        page_type_instance = PageType.query.filter_by(name=page_type).one()
    except MultipleResultsFound as e:
        raise e
    except NoResultFound as e:
        raise e

    try:
        return Page.query.filter_by(page_type_id=page_type_instance.id, name=page_identifier).one()
    except MultipleResultsFound as e:
        raise e
    except NoResultFound as e:
        raise e
