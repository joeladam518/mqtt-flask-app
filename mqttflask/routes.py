from mqttflask import app
from mqttflask.controllers.HomeController import HomeController
from mqttflask.resources.mqtt import Mqtt

@app.route('/')
HomeController.index()
