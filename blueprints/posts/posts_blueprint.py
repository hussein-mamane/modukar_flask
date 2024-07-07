import flask
from flask import Blueprint, session, render_template, request, redirect, url_for, flash, abort, jsonify, helpers, \
    after_this_request
from .data import franchises

posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="posts_pages")


@posts_blueprint.route("/")
def index():
    # @after_this_request
    # def add_header(response):
    #     response.headers['X-Foo'] = 'Parachute'
    #     return response

    response = flask.make_response(jsonify({
        "message": "Welcome to Posts Blog"
    }))
    # response.set_cookie("username", session["username"])
    del response.headers["Server"]  # Does not work
    print(response.headers)

    return response


@posts_blueprint.route("/all", methods=["GET"])
def get_all_data():
    return jsonify(franchises)



@posts_blueprint.errorhandler(404)
def page_not_found():
    abort(404, description="Not Found")