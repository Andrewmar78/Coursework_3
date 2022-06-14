# недоделано
from typing import List

from project.dao import MovieDAO
from project.exceptions import ItemNotFound
from project.schemas.movie import MovieSchema


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_item_by_id(self, movie_id: int) -> object:
        movie = self.dao.get_by_id(movie_id)
        if not movie:
            raise ItemNotFound
        return movie

    def get_all(self, page_number=None, status=None) -> List[object]:
        # Как-то некорректно прописано со статусом ниже
        if status != "new":
            movies = self.dao.get_all(page_number, is_status=False)
        else:
            movies = self.dao.get_all(page_number, is_status=True)

        if not movies:
            raise ItemNotFound

        return movies
