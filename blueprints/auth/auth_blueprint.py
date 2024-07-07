from flask import Blueprint, render_template, abort, redirect, url_for, session, request
from jinja2 import TemplateNotFound

# auth_blueprint = Blueprint('auth_blueprint', __name__,template_folder="C:\\Users\\"
#                                                                       "Housseini\\PycharmProjects\\review_blog\\blueprints\\auth\\auth_pages")

auth_blueprint = Blueprint('auth_blueprint', __name__, template_folder='auth_pages')


@auth_blueprint.route('/', methods=['GET', 'POST'], )
def login():
    try:
        return render_template("login_page.html")
    except TemplateNotFound:
        abort(404)



