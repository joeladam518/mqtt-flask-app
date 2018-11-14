import os
from flask import request
from flask_restful import Resource
from flask_httpauth import HTTPTokenAuth
import paho.mqtt.publish as publish


auth = HTTPTokenAuth('Bearer')

@auth.verify_token
def verify_token(token):
    return (os.getenv('MQTT_PUBLISH_SECRET') == token)


class MqttController(Resource):

    def __init__(self):
        pass

    @auth.login_required
    def get(self, topic = None):
        return {
            'status': 'success',
            'messages': [
                'This endpoint will never do anything.'
            ],
            'data': {
                'requested_topic': topic,
            }
        }, 200

    @auth.login_required
    def post(self):

        topic = request.form.get('topic')
        message = request.form.get('message')

        if not topic and not message:
            return {
                'status': 'error',
                'messages': [
                    'No topic and/or No message'
                ],
            }, 422

        """
            mqtt.publish.single(topic, payload=None, qos=0, retain=False, hostname="localhost",
                                port=1883, client_id="", keepalive=60, will=None, auth=None,
                                tls=None, protocol=mqtt.MQTTv311, transport="tcp")
        """
        publish.single(topic=topic, payload=message, hostname=os.getenv('MQTT_SERVER_ADDRESS'))

        if message == '1':
            return_message = 'You turn an led on!!!!!'
        elif message == '0':
            return_message = 'You turn an led off!!!!!'
        else:
            return_message = 'I don\'t know what the fuck you did...'

        return {
            'status': 'success',
            'messages': [
                return_message
            ],
        }, 200
