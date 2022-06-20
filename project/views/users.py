import jwt
from flask import request, current_app
from flask_restx import Resource, Namespace, abort
from helpers.decorators import auth_required
from project.constants import JWT_ALGORITHM
from project.container import auth_service, user_service
from project.exceptions import NoUserFound, IncorrectPassword, ItemNotFound
from project.schemas import UserSchema

from project.views.auth import user_schema

user_ns = Namespace('user')
user_schema = UserSchema()


@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    @user_ns.doc(description='Get one user by id')
    @user_ns.response(200, 'OK')
    @user_ns.response(404, 'Not Found')
    def get(self):
        """Получение токена, обновление данных"""
        try:
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            data = jwt.decode(jwt=token, key=current_app.config.get('SECRET_KEY'), algorithms=JWT_ALGORITHM)
            email = data.get("email")
            user = user_service.get_user_by_email(email)

            return user_schema.dump(user), 200
        except NoUserFound:
            abort(404, 'User is not found')

    @auth_required
    @user_ns.doc(description='Get one user by id')
    @user_ns.response(200, 'OK')
    @user_ns.response(404, 'Not Found')
    def patch(self):
        """Получение токена, обновление данных"""
        try:
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            data = jwt.decode(jwt=token, key=current_app.config.get('SECRET_KEY'), algorithms=JWT_ALGORITHM)
            email = data.get("email")
            new_data = user_schema.dump(request.json)
            user_service.update_user(new_data, email)
            return "", 200
        except NoUserFound:
            abort(404, 'User is not found')


@user_ns.route('/password/')
class PasswordView(Resource):
    @auth_required
    @user_ns.doc(description='Update password')
    @user_ns.response(200, 'Updated')
    @user_ns.response(401, 'Password incorrect')
    @user_ns.response(404, 'Not Found')
    def put(self):
        """Получение токена, обновление данных"""
        try:
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            data = jwt.decode(jwt=token, key=current_app.config.get('SECRET_KEY'), algorithms=JWT_ALGORITHM)
            email = data.get("email")
            passwords = request.json
            user_service.update_password(passwords, email)
            return "", 200
        except IncorrectPassword:
            abort(401, 'Password is incorrect')
        except ItemNotFound:
            abort(404, 'User not found')
