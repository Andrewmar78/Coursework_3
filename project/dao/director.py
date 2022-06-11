from project.dao.base import BaseDAO
from project.dao.models import Director
from typing import List, Optional

from project.schemas.director import DirectorSchema


class DirectorDAO(BaseDAO):
    def get_by_id(self, director_id: int) -> Optional[DirectorSchema]:
        director: Optional[Director] = self.session.query(Director).filter(Director.id == director_id).scalar()

        if director is not None:
            return DirectorSchema().dump(director)

    def get_all(self) -> List[DirectorSchema]:
        directors: List[Director] = self.session.query(Director).all()
        return DirectorSchema().dump(directors, many=True)
