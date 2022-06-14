from typing import List, Optional
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
            # Как-то надо доработать ниже для ITEMS_PER_PAGE != 10:
            genres = genres.limit(10).offset(10*(page_number - 1))

        return genres.all()
