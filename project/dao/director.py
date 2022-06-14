from project.dao.base import BaseDAO
from project.dao.models import Director
from typing import List, Optional

from project.schemas.director import DirectorSchema


class DirectorDAO(BaseDAO):
    def get_by_id(self, director_id: int) -> Optional[DirectorSchema]:
        director: Optional[Director] = self.session.query(Director).get(director_id)
        return director

    def get_all(self, page_number=None) -> List[object]:
        directors = self.session.query(Director)
        if page_number:
            # Как-то надо доработать ниже для ITEMS_PER_PAGE != 10:
            directors = directors.limit(10).offset(10*(page_number - 1))

        return directors.all()
