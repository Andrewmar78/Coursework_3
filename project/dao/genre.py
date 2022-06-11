from typing import List, Optional
from project.dao.base import BaseDAO
from project.dao.models import Genre
from project.schemas.genre import GenreSchema


class GenreDAO(BaseDAO):
    def get_by_id(self, genre_id: int) -> Optional[GenreSchema]: # Optional - [GenreSchema] or None
        genre: Optional[Genre] = self.session.query(Genre).filter(Genre.id == genre_id).scalar()
        # Optional means: genre = [Genre] or None

        if genre is not None:
            return GenreSchema().dump(genre)

    # def get_by_id(self, pk):
    #     return self._db_session.query(Genre).filter(Genre.id == pk).one_or_none()

    def get_all(self) -> List[GenreSchema]:
        genres: List[Genre] = self.session.query(Genre).all()
        return GenreSchema().dump(genres, many=True)
