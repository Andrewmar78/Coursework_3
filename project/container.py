from project.services.auth import AuthService
from project.setup_db import db
from project.dao import GenreDAO
from services.genre_service import GenresService

genre_dao = GenreDAO(session=db.session)
genre_service = GenresService(dao=genre_dao)
auth_service = AuthService(user_service)
