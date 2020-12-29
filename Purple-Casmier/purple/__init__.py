import os
from flask import Flask

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__,instance_relative_config=True)
    app.secret_key = "dev"

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)

    else:
        # Load the test config is if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Hello, World!'

    from . import game

    app.register_blueprint(game.bp)

    return app