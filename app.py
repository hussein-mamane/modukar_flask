from flask import Flask, redirect, url_for, jsonify, request, session, flash, abort
from flask import helpers
from flask_caching import Cache
from flask_cors import CORS
from blueprints.auth.auth_blueprint import auth_blueprint
from blueprints.posts.posts_blueprint import posts_blueprint

app = Flask(__name__)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(posts_blueprint, url_prefix='/posts')

config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)
CORS(app, origins=["http://localhost:3000"])


@app.route('/')
def handle_arrival():
    return redirect("/posts")


@app.errorhandler(404)
def page_not_found():
    # return render_template('404.html'), 404
    # Do not use abort to avoid internal server errror
    abort(404, description="Not Found")
    # abort(404,jsonify({'error': 'Not found'}))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

# TODO : Try something in gunicorn
# Does not work
# @app.after_request
# def remove_server_header(response):
#     response.headers.pop('Server', None)
#     return response
