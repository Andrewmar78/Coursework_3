from project.dao import GenreDAO
from project.exceptions import ItemNotFound
from project.schemas.genre import GenreSchema
from project.services.base import BaseService


class GenreService(BaseService):
    def get_item_by_id(self, genre_id):
        genre = GenreDAO(self._db_session).get_by_id(genre_id)
        if not genre:
            raise ItemNotFound
        return GenreSchema().dump(genre)

    def get_all(self):
        genres = GenreDAO(self._db_session).get_all()
        return GenreSchema(many=True).dump(genres)
