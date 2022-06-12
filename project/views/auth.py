from flask import request
from flask_restx import Namespace, Resource, abort
from project.container import auth_service
from project.exceptions import NoUserFound, IncorrectPassword, UserAlreadyExists
from project.schemas import UserSchema
from project.services import UserService
from project.setup_db import db

auth_ns = Namespace("auth")
user_schema = UserSchema()

@auth_ns.route("/registration/")
class AuthView(Resource):
    def post(self):
        """Получение и проверка почты и пароля, регистрация пользователя"""
        req_json = request.json
        email = req_json.get("email", None)
        password = req_json.get("password", None)
        created_data = {"email": email, "password": password}
        if None in [email, password]:
            return "Incorrect fields fulfilled", 400

        try:
            user_data = user_schema.load(created_data)
            new_user = UserService(db.session).create_user(user_data)
            return "", 201, {"location": f"/user/{new_user.id}"}
        except UserAlreadyExists:
            abort(400, 'User already exists')


@auth_ns.route('/login/')
class AuthView(Resource):
    def post(self):
        """Получение и проверка почты и пароля, создание токенов"""
        req_json = request.json
        email = req_json.get("email", None)
        password = req_json.get("password", None)
        if None in [email, password]:
            abort(400, 'Incorrect email or password')

        try:
            tokens = auth_service.generate_tokens(email, password)
            return tokens, 201
        except NoUserFound:
            abort(404, 'User not found')
        except IncorrectPassword:
            abort(401, 'Incorrect password')

    def put(self):
        """Проверка даты и получение токена"""
        refresh_token = request.json.get('refresh_token')
        if not refresh_token:
            abort(400, '')

        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201
