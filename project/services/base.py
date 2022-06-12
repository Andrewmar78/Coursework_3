# from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm import Session


class BaseService:
    # def __init__(self, session: scoped_session):
    def __init__(self, session: Session):
        self._db_session = session
