from typing import List, Optional

from flask import current_app

from project.dao.base import BaseDAO
from project.dao.models import Genre
from project.schemas.genre import GenreSchema


class GenreDAO(BaseDAO):
    def get_by_id(self, genre_id: int) -> Optional[GenreSchema]: # Optional means: [GenreSchema] or None
        # genre: Optional[Genre] = self.session.query(Genre).filter(Genre.id == genre_id).scalar()
        genre: Optional[Genre] = self.session.query(Genre).get(genre_id)
        return genre

    def get_all(self, page_number=None) -> List[object]:
        genres = self.session.query(Genre)
        if page_number:
            genres = genres.limit(current_app.config.get('ITEMS_PER_PAGE'))\
                .offset(current_app.config.get('ITEMS_PER_PAGE')*(page_number - 1))
        return genres.all()
