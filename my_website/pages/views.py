from flask import Blueprint, redirect, url_for, render_template, request
from .helper_functions import home_function, page_function, index_function

page_blueprint = Blueprint('page_blueprint', __name__, template_folder='templates')


@page_blueprint.route('/')
def root_redirect():
    return redirect(url_for('page_blueprint.'))


@page_blueprint.route('/home')
def home_view():
    """
    View for the home page

    :return:
    """
    page_data = home_function(request)
    return render_template('page_blueprint/pages/home_page.html', page_data=page_data)


@page_blueprint.route('/<page_type>/index')
def index_view(page_type):
    """
    View function for the index page of a given page type

    :param page_type:
    :return:
    """
    page_list_data, page_type_data = index_function(page_type)
    return render_template('page_blueprint/pages/index.html')


@page_blueprint.route('/<page_type>/<page_identifier>')
def page_view(page_type, page_identifier):
    """
    View for a standard page

    :param page_type: Name of the page type
    :param page_identifier: Name of the page
    :return:
    """
    page_data = page_function(request, page_type, page_identifier)
    return render_template(page_data.page_type.template, page_data=page_data)
