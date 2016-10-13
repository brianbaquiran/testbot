import logging
import sys

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)

from flask import Flask, request
from flask_restful import Api
from flask_script import Manager

from resources.webhooks import WebHook

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
api = Api(app)
manager = Manager(app)

app.logger.addHandler(stdout_handler)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'Hello World!'
    if request.method == 'POST':
        print('A value for debugging')
        return 'You POSTED!'

api.add_resource(WebHook,'/webhook')


if __name__== '__main__':
    manager.run()
