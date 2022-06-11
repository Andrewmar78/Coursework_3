from project.dao.base import BaseDAO
from project.dao.models import Director, Movie
from typing import List, Optional

from project.schemas.movie import MovieSchema


class MovieDAO(BaseDAO):
    def get_by_id(self, movie_id: int) -> Optional[MovieSchema]:
        movie: Optional[Movie] = self.session.query(Movie).filter(Movie.id == movie_id).scalar()

        if movie is not None:
            return MovieSchema().dump(movie)

    def get_all(self) -> List[MovieSchema]:
        movies: List[Movie] = self.session.query(Movie).all()
        return MovieSchema().dump(movies, many=True)
