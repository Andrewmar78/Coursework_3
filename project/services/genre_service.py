from typing import List
from project.dao import GenreDAO
from project.exceptions import ItemNotFound


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_item_by_id(self, genre_id: int) -> object:
        genre = self.dao.get_by_id(genre_id)
        if not genre:
            raise ItemNotFound
        return genre

    def get_all(self, page_number=None) -> List[object]:
        genres = self.dao.get_all(page_number)
        if not genres:
            raise ItemNotFound
        return genres
