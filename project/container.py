from project.services import GenreService, DirectorService, MovieService, UserService, AuthService
from project.setup_db import db
from project.dao import GenreDAO, DirectorDAO, MovieDAO, UserDAO

genre_dao = GenreDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)

genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service)
