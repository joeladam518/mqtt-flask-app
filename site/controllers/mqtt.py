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
        # topic = request.form.get('topic')
        # message = request.form.get('message')

        # if not topic and not message:
        #     return {
        #         'status': 'error',
        #         'messages': [
        #             'No topic and/or No message'
        #         ],
        #     }, 422

        parser = reqparse.RequestParser()
        parser.add_argument('topic', required=True, location='form', nullable=False, help='No Topic')
        parser.add_argument('message', required=True, location='form', nullable=False, help='No Payload')
        args = parser.parse_args()

        topic = str(args['topic'])
        message = str(args['message'])

        """
            mqtt.publish.single(topic, payload=None, qos=0, retain=False, hostname="localhost",
                                port=1883, client_id="", keepalive=60, will=None, auth=None,
                                tls=None, protocol=mqtt.MQTTv311, transport="tcp")
        """
        publish.single(topic=topic, payload=message, hostname=os.getenv('MQTT_SERVER_ADDRESS'))

        return {
            'status': 'success',
            'messages': [
                'The topic submitted: "{}"'.format(topic),
                'The payload submitted: "{}"'.format(message),
            ]
        }, 200
