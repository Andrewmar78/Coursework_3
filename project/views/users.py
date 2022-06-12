#  Недоработан
import jwt
from flask import request
from flask_restx import Resource, Namespace, abort

from helpers.decorators import auth_required
from project.constants import JWT_ALGORITHM, JWT_SECRET
from project.container import auth_service
from project.exceptions import NoUserFound
from project.services import user_service, UserService
from project.setup_db import db
from project.views.auth import user_schema

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self, refresh_token):
        """Получение токена, данных, обновление данных"""
        try:
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            data = jwt.decode(jwt=token, key=JWT_SECRET, algorithms=JWT_ALGORITHM)
            email = data.get("email")

            user = UserService(db.session).get_user_by_email(email)
            return user_schema.dump(user), 200
        except NoUserFound:
            abort(404, 'User is not found')

    def post(self):
        try:
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            data = jwt.decode(jwt=token, key=JWT_SECRET, algorithms=JWT_ALGORITHM)
            email = data.get("email")

            new_data = user_schema.dump(request.json)
            UserService(db.session).update_user(new_data, email)
            return "", 200
        except NoUserFound:
            abort(404, 'User is not found')
