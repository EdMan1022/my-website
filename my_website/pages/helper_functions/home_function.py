from ..models import Page, PageType
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound


def home_function(request):
    """
    Returns the home page data from the database

    :param request:
    :return:
    """

    try:
        page_type = PageType.query.filter_by(name='home').one()
    except MultipleResultsFound as e:
        raise e
    except NoResultFound as e:
        raise e

    try:
        page = Page.query.filter_by(page_type_id=page_type.id).one()
    except MultipleResultsFound as e:
        raise e
    except NoResultFound as e:
        raise e
    return page
