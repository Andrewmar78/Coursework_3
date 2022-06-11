from project.dao.models.base import BaseModel
from project.setup_db import db


class Genre(BaseModel):
    __tablename__ = "genres"

    name = db.Column(db.String(100), unique=True, nullable=False)

    # def __repr__(self):
    #     return f"<Genre '{self.name.title()}'>"
