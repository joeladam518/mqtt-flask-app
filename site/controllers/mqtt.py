from flask import request
from flask_restful import Resource

class MqttController(Resource):

    def __init__(self):
        pass

    def get(self, topic = None):
        data = { 'bob': 'yourmom', 'topic': topic }
        return data

    def post(self):
        return request.form