from flask import Flask, request
from flask_restful import Resource, Api
from flask_script import Manager


app = Flask(__name__)
api = Api(app)
manager = Manager(app)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'Hello World!'
    if request.method == 'POST':
        print('A value for debugging')
        return 'You POSTED!'

class WebHook(Resource):
    def get(self):
        hub_challenge = request.args.get('hub.challenge','')
        if hub_challenge == '':
            return "Hello, you didn't specify a hub.challenge"
        return hub_challenge

    def post(self):
        data = request.get_json()
        return data['sender']

api.add_resource(WebHook,'/webhook')


if __name__== '__main__':
    manager.run()
