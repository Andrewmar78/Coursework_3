from typing import List

from project.dao.director import DirectorDAO
from project.exceptions import ItemNotFound


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_item_by_id(self, director_id: int) -> object:
        director = self.dao.get_by_id(director_id)
        if not director:
            raise ItemNotFound
        return director

    def get_all(self, page_number=None) -> List[object]:
        directors = self.dao.get_all(page_number)
        if not directors:
            raise ItemNotFound
        return directors
