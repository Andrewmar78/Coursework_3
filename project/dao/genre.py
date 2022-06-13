from typing import List, Optional
from project.dao.base import BaseDAO
from project.dao.models import Genre
from project.schemas.genre import GenreSchema


class GenreDAO(BaseDAO):
    def get_by_id(self, genre_id: int) -> Optional[GenreSchema]: # Optional means: [GenreSchema] or None
        # genre: Optional[Genre] = self.session.query(Genre).filter(Genre.id == genre_id).scalar()
        genre: Optional[Genre] = self.session.query(Genre).get(genre_id)
        return genre

    # def get_by_id(self, pk):
    #     return self._db_session.query(Genre).filter(Genre.id == pk).one_or_none()

    def get_all(self) -> List[object]:
        genres = self.session.query(Genre)
        return genres.all()

    # Без пагинации
