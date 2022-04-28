""" This is Flask HTTP REST API skeleton template that already has the elastic database
implemented.

Application features:
    python 3.6
    Flask

This module contains the factory function 'create_app' that is reponsibility for initializing
the application according to a previous configuration.
"""

import os

from flask import Flask
from flask_restx import Api, Resource, fields

def create_app(test_config: dict={}) -> Flask:
    """ This function is reponsibility to create a Flask instance according
    a previous setting passed from environment. In that process, it also
    initialise the database source.

    Parameters: 
        test_config (dict): settings coming from test environment

    returns:
        flask.app.Flask: The application instance."""

    app = Flask(__name__, instance_relative_config=True)

    load_config(app, test_config)
    
    # init_swagger(app)
    init_instance_folder(app)
    init_database(app)
    # init_blueprints(app)
    init_namespaces(app)

    return app


def load_config(app: Flask, test_config) -> None:
    """ Load the application's config

    Parameters:
        app (flask.app.Flask): The application instance Flask that'll be running.
        test_config (dict): 
    """

    if os.environ.get('FLASK_ENV') == 'development' or test_config.get('FLASK_ENV') == 'development':
        app.config.from_object('src.config.Development')
    else:
        app.config.from_object('src.config.Production')

def init_swagger(app) -> None:
    from .swagger_api import init
    init(app)

def init_instance_folder(app: Flask) -> None:
    """ Ensure the instance folder exists.

    Parameters:
        app (flask.app.Flask): The application instance Flask that'll be running.
    """

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def init_database(app) -> None:
    """ Responsible for initilizing and connecting to the database to be used by the application.

    Parameters:
        app (flask.app.Flask): The application instance Flask that'll be running.
    """
    from .database import init
    init(app)


def init_blueprints(app: Flask) -> None:
    """ Registes the blueprint to the application

    Parameters:
        app (flask.app.Flask): The application instance Flask thah'll be running.
    """

    # error handlers
    from .blueprints.handlers import register_handler
    register_handler(app)

    # initializing blueprint
    from .blueprints import (index) 
    app.register_blueprint(index.bp)


def init_namespaces(app: Flask) -> None:
    from .apis import api
    api.init_app(app)

""" def init_commands(app):
    from app.commands import register_commands
    register_commands(app)


def init_jwt_manager(app):
    from .authentication import init
    jwt = JWTManager(app)
    init(jwt) """
