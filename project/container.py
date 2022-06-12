from project.services import GenreService, user_service
from project.services.auth import AuthService
from project.setup_db import db
from project.dao import GenreDAO

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(dao=genre_dao)
auth_service = AuthService(user_service)
