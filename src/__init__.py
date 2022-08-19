from flask import Flask, jsonify
from flask_restx import Resource, Api
from werkzeug.utils import cached_property

app = Flask(__name__)

api = Api(app)

app.config.from_object('src.config.DevelopmentConfig') 

class Ping(Resource):
    def get(self):
        return {
            'status': 'success 01',
            'message': 'pong!'
        }

api.add_resource(Ping, '/ping')
    