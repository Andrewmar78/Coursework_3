from project.dao.models.base import BaseModel
from project.setup_db import db


class User(BaseModel):
    __tablename__ = "users"

    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)
    # role = db.Column(db.String, unique=False, nullable=True)
    surname = db.Column(db.String)
    favourite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"))

    genre = db.relationship("Genre")

    # def __repr__(self):
    #     return f"<User '{self.username.title()}'>"
