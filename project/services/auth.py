import datetime
import calendar
import jwt
from flask import current_app
from flask_restx import abort

from project.constants import SECRET_KEY, JWT_SECRET, JWT_ALGORITHM
from project.exceptions import IncorrectPassword, NoUserFound


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refreshed=False):
        user = self.user_service.get_user_by_email(email)

        if not user:
            raise abort(404)

        if not is_refreshed:
            if not self.user_service.compare_passwords(user.password, password):
                raise IncorrectPassword

        # Данные для токена
        data = {
            "email": user.email
        }

        # Генерирование токенов
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config.get('TOKEN_EXPIRE_MINUTES'))
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET_KEY, algorithm=JWT_ALGORITHM)

        days30 = datetime.datetime.utcnow() + datetime.timedelta(days=current_app.config.get('TOKEN_EXPIRE_DAYS'))
        data["exp"] = calendar.timegm(days30.timetuple())
        refresh_token = jwt.encode(data, SECRET_KEY, algorithm=JWT_ALGORITHM)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, refresh_token) -> dict:
        """Получение почты из токена и создание новых токенов"""
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=JWT_ALGORITHM)
        email = data.get("email")
        user = self.user_service.get_user_by_email(email)
        if not user:
            raise NoUserFound

        new_token = self.generate_tokens(email=email, password=None, is_refreshed=True)
        return new_token
