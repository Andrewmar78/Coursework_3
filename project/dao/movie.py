from flask import current_app
from sqlalchemy import desc

from project.dao.base import BaseDAO
from project.dao.models import Movie
from typing import List, Optional

from project.schemas.movie import MovieSchema


class MovieDAO(BaseDAO):
    def get_by_id(self, movie_id: int) -> Optional[MovieSchema]:
        genre: Optional[Movie] = self.session.query(Movie).get(movie_id)
        return genre

    def get_all(self, page_number=None, is_status: bool = False) -> List[object]:
        movies = self.session.query(Movie)

        if is_status:
            movies = movies.order_by(desc(Movie.year))

        if page_number:
            movies = movies.limit(current_app.config.get('ITEMS_PER_PAGE'))\
                .offset(current_app.config.get('ITEMS_PER_PAGE')*(page_number - 1))
        return movies.all()
