#  Недоработан
import datetime
import calendar
import jwt
from flask_restx import abort

from constants import ALGORITHM, SECRET_KEY, JWT_SECRET


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refreshed=False):
        user = self.user_service.get_user_by_name(username)

        if not user:
            raise abort(404)

        if not is_refreshed:
            if not self.user_service.compare_passwords(user.password, password):
                raise abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

        days30 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        data["exp"] = calendar.timegm(days30.timetuple())
        refresh_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=ALGORITHM)
        username = data.get("username")
        user = self.user_service.get_user_by_name(username)
        if not user:
            raise Exception()
        return self.generate_tokens(username, None, is_refreshed=True)

