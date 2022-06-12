from project.dao.models.base import BaseModel
from project.setup_db import db


class Genre(BaseModel):
    __tablename__ = "genres"
    __table_args__ = {'extend_existing': True}
    # this will allow this column to 'extend' the parent attributes

    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Genre '{self.name.title()}'>"
