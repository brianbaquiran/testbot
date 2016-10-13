from flask import request, current_app, make_response
from flask_restful import Resource
import logging, sys
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

class WebHook(Resource):
    def get(self):
        hub_challenge = request.args.get('hub.challenge','')
        if hub_challenge == '':
            return "Hello, you didn't specify a hub.challenge"
        return make_response(hub_challenge)

    def post(self):
        data = request.get_json()
        current_app.logger.debug(data)
        url = "https://graph.facebook.com/v2.6/me/messages?access_token=%s" % app.config['PAGE_ACCESS_TOKEN']
        requests.post(url, data={"recipient":{ "id":data['sender']['id']},"message":{"text":"hello, world!"}})
        return data['message']
