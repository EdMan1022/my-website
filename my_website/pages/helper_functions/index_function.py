from ..models import Page, PageType
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound


def index_function(page_type):
    """
    Return the data for the index page of a page type.

    Contains links to all of the pages in the page type.
    :param page_type:
    :return: List of the page objects in this page type.
    """
    try:
        page_type_instance = PageType.query.filter_by(name=page_type).all()
    except NoResultFound as e:
        raise e
    except MultipleResultsFound as e:
        raise e

    try:
        return Page.query.filter_by(page_type_id=page_type_instance.id).all(), page_type_instance
    except NoResultFound as e:
        raise e
    except MultipleResultsFound as e:
        raise e
