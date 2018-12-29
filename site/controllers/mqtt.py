import os
from flask import request
from flask_restful import Resource, reqparse
from flask_httpauth import HTTPTokenAuth
import paho.mqtt.publish as publish


auth = HTTPTokenAuth('Bearer')


@auth.verify_token
def verify_token(token):
    return (str(os.getenv('MQTT_PUBLISH_SECRET')) == str(token))


class MqttController(Resource):

    def __init__(self):
        pass

    @auth.login_required
    def get(self):
        return {
            'status': 'success',
            'messages': [
                'This endpoint will never do anything.'
            ],
            'data': {
                'requested_topic': '',
            }
        }, 200

    @auth.login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('topic', required=True, location='form', help='No topic.')
        parser.add_argument('message', required=True, location='form', dest='payload', help='No payload.')
        args = parser.parse_args()

        topic = str(args['topic'])
        message = str(args['message'])

        if not topic or not message:
            return {
                'status': 'error',
                'message': {
                    "general": "No topic and/or no payload.",
                },
            }, 422

        """
            mqtt.publish.single(topic, payload=None, qos=0, retain=False, hostname="localhost",
                                port=1883, client_id="", keepalive=60, will=None, auth=None,
                                tls=None, protocol=mqtt.MQTTv311, transport="tcp")
        """
        publish.single(topic=topic, payload=message, hostname=os.getenv('MQTT_SERVER_ADDRESS'))

        return {
            'status': 'success',
            'message': {
                "topic_submitted": "{}".format(topic),
                "payload_submitted": "{}".format(message),
            }
        }, 200
