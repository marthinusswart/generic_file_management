from flask import request
from flask_restful import Resource


class ApiManagement(Resource):
    def get(self):
        return {'about': 'Generic File Management API is online'}

    def post(self):
        some_json = request.get_json()
        return {'JSON received by the API': some_json}
