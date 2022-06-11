from project.dao.models.base import BaseModel
from project.setup_db import db


class Director(BaseModel):
    __tablename__ = "directors"

    name = db.Column(db.String(100), unique=True, nullable=False)

    # def __repr__(self):
    #     return f"<Director '{self.name.title()}'>"