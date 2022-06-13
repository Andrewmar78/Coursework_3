from sqlalchemy.exc import IntegrityError
from project.config import DevelopmentConfig
from project.dao.models import User
from project.dao.models.director import Director
from project.dao.models.genre import Genre
from project.dao.models.movie import Movie
from project.server import create_app
from project.setup_db import db
from project.utils import read_json

app = create_app(DevelopmentConfig)

data = read_json("fixtures.json")

with app.app_context():
    for genre in data["genres"]:
        # db.session.add(Genre(**genre))
        db.session.add(Genre(id=genre["pk"], name=genre["name"]))

    for director in data["directors"]:
        # db.session.add(Director(**director))
        db.session.add(Director(id=director["pk"], name=director["name"]))

    for movie in data["movies"]:
        # db.session.add(Movie(**movie))
        db.session.add(Movie(id=movie["pk"], title=movie["title"], description=movie["description"],
                             trailer=movie["trailer"], year=movie["year"], rating=movie["rating"],
                             genre_id=movie["genre_id"], director_id=movie["director_id"]))

    for user in data["users"]:
        # db.session.add(Movie(**movie))
        db.session.add(User(id=user["pk"], username=user["username"], surname=user["surname"], email=user["email"],
                            password=user["password"], favourite_genre=user["favourite_genre"], role=user["role"]))

    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")
