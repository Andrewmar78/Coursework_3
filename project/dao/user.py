#  Недоработан
from typing import Optional
from project.dao.base import BaseDAO
from project.dao.models import User
from project.exceptions import NoUserFound
from project.schemas.user import UserSchema


class UserDAO(BaseDAO):
	def get_user_by_email(self, email: str) -> Optional[User]:
		try:
			return self.session.query(User).filter(User.email == email).one()
		except NoUserFound:
			return None

	# def get_one(self, uid):
	# 	return self.session.query(User).get(uid)

	def create_user(self, user_data: dict) -> User:
		entity = User(**user_data)
		self.session.add(entity)
		self.session.commit()
		# new_user = UserSchema().dump(entity)
		# return new_user
		return entity

	def update(self, user_data: dict, email: str) -> None:
		self.session.query(User).filter(User.email == email).update(user_data)
		# self.session.add(user_data)
		self.session.commit()

	# def delete(self, uid: int):
	# 	user_data = self.get_one(uid)
	# 	self.session.delete(user_data)
	# 	self.session.commit()
