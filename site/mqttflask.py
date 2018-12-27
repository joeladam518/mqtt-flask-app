import os
from flask import Flask, cli as flask_cli, request
from flask_restful import Api
from mqttflask_config import Config as mqttflask_config
from controllers.home import HomeController
from controllers.mqtt import MqttController

app_root = os.path.dirname(__file__)
dotenv_path = os.path.join(app_root, '.env')
flask_cli.load_dotenv(dotenv_path)

app = Flask(__name__, static_folder='assets', template_folder="resources/templates", root_path=app_root)
app.config.from_object(mqttflask_config)
api = Api(app)

# Regular route that renders a web page
app.add_url_rule('/', view_func=HomeController.as_view('home_page'))

# Api route to post and get mqtt messages
#api.add_resource(MqttController, '/mqtt', '/mqtt/<string:topic>')
api.add_resource(MqttController, '/mqtt')

@app.route('/bob', methods=['POST'])
def bob():
    print(request.form)
    exit()


if __name__ == "__main__":
    app.run()
