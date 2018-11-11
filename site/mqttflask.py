import os
from flask import Flask
from flask import request
from flask import cli as flask_cli
from flask_restful import Api
from controllers.home import HomeController
from controllers.mqtt import MqttController

app_root = os.path.join(os.path.dirname(__file__))
dotenv_path = os.path.join(app_root, '.env')
flask_cli.load_dotenv(dotenv_path)

app = Flask(__name__, static_folder='assets', template_folder="resources/templates", root_path=app_root)
app.testing = True

api = Api(app)

# Regular route that renders a web page
app.add_url_rule('/', view_func=HomeController.as_view('home_page'))

# Api route to post and get mqtt messages
api.add_resource(MqttController, '/mqtt', '/mqtt/<string:topic>')

if __name__ == "__main__":
    app.run()
