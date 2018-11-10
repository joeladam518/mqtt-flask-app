import os
from flask import Flask, render_template
from flask_restful import Api

def create_app():
    # instantiate the flask app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    # instantiate the flask_restful app
    api = Api(app)

    import mqttflask.routes

    return app
