from project.dao.models.base import BaseModel
from project.setup_db import db


class Movie(BaseModel):
    __tablename__ = "movies"
    __table_args__ = {'extend_existing': True}

    title = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=True)
    trailer = db.Column(db.String(255), unique=True, nullable=True)
    year = db.Column(db.Integer, unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=False)

    genre = db.relationship("Genre")
    director = db.relationship("Director")
    # status = db.Column(db.String(10), unique=False, nullable=True)

    def __repr__(self):
        return f"<Movie '{self.title.title()}'>"
