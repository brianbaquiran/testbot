from flask import Flask, request
from flask_restful import Resource, Api
from flask.ext.script import Manager


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

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        # Facebook is validating the webhook subscription.
        # See https://developers.facebook.com/docs/graph-api/webhooks
        # Section: Handling Verification Requests
        hub_challenge = request.args.get('hub.challenge','')
        if hub_challenge == '':
            return "Hello, you didn't specify a hub.challenge"
        return hub_challenge
    elif request.method == 'POST':
        return ""

if __name__== '__main__':
    manager.run()
