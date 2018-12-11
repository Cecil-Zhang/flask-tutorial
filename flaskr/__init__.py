import os

from flask import Flask, jsonify
from flaskr.my_exception import My_Exception

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:root@localhost:3306/test',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    app.logger.debug(app.instance_path)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flaskr.models import db
    db.init_app(app)

    from . import users
    app.register_blueprint(users.bp)

    @app.errorhandler(My_Exception)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app