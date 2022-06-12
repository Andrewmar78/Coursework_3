from typing import List

from project.dao import GenreDAO
from project.exceptions import ItemNotFound
from project.schemas.genre import GenreSchema
from project.services.base import BaseService


class GenreService(BaseService):
    def get_item_by_id(self, genre_id: int) -> object:
        genre = GenreDAO(self._db_session).get_by_id(genre_id)
        if not genre:
            raise ItemNotFound
        return GenreSchema().dump(genre)

    # def get_one(self, uid: int) -> object:
    #     item = self.dao.get_one(uid)
    #     if not item:
    #         raise ItemNotFound
    #     return item

    def get_all(self) -> List[object]:
        genres = GenreDAO(self._db_session).get_all()
        return GenreSchema(many=True).dump(genres)

    # def get_all(self, page: str = None) -> List[object]:
    #     """
    #     Get all items from the db
    #     :param page: Page number (optional)
    #     :raises ItemNotFound: If no items found
    #     """
    #     items = self.dao.get_all(page, sort=False)
    #     if not items:
    #         raise ItemNotFound
    #     return items
