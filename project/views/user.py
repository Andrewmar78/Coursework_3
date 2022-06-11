#  Недоработан
from flask import request
from flask_restx import Resource, Namespace

from container import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def post(self):
        user_data = request.json
        user = user_service.create_user(user_data)
        return user, 201
