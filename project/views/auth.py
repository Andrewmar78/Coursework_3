from flask import request
from flask_restx import Namespace, Resource, abort
from project.container import auth_service, user_service
from project.exceptions import NoUserFound, IncorrectPassword, UserAlreadyExists, InvalidToken
from project.schemas import UserSchema
from project.schemas.auth import AuthSchema

auth_ns = Namespace("auth")
user_schema = UserSchema()
auth_schema = AuthSchema()


@auth_ns.route("/register/")
class AuthView(Resource):
    @auth_ns.doc(description='New User')
    @auth_ns.response(201, 'Registered')
    @auth_ns.response(400, 'Problem')
    def post(self):
        """Получение и проверка наличия почты и пароля, регистрация пользователя"""
        req_json = request.json
        email = req_json.get("email", None)
        password = req_json.get("password", None)
        created_data = {"email": email, "password": password}
        if None in [email, password]:
            return "Incorrect fields fulfilled", 400

        try:
            # user_data = user_schema.load(created_data)
            user_data = auth_schema.load(created_data)
            new_user = user_service.create_user(user_data)
            return "", 201, {"location": f"/user/{new_user.id}"}
        except UserAlreadyExists:
            abort(400, 'User exists')


@auth_ns.route('/login/')
class AuthView(Resource):
    @auth_ns.doc(description='User entering')
    @auth_ns.response(201, 'User entered')
    @auth_ns.response(400, 'Problem')
    def post(self):
        """Получение и проверка наличия почты и пароля, создание токенов"""
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

    @auth_ns.doc(description='New tokens')
    @auth_ns.response(201, 'Tokens received')
    @auth_ns.response(401, 'Invalid token')
    def put(self):
        """Проверка даты и получение токена"""
        try:
            refresh_token = request.json.get('refresh_token')
            if not refresh_token:
                abort(400, '')
            tokens = auth_service.approve_refresh_token(refresh_token)
            return tokens, 201

        except InvalidToken:
            abort(401, 'Invalid token passed')

