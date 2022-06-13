# недоделано
from project.dao import MovieDAO
from project.exceptions import ItemNotFound
from project.schemas.movie import MovieSchema


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_item_by_id(self, pk):
        movie = MovieDAO(self._db_session).get_by_id(pk)
        if not movie:
            raise ItemNotFound
        return MovieSchema().dump(movie)

    def get_all(self):
        movie = MovieDAO(self._db_session).get_all()
        return MovieSchema(many=True).dump(movie)
