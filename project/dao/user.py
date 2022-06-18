from typing import Optional
from project.dao.base import BaseDAO
from project.dao.models import User
from project.exceptions import NoUserFound


class UserDAO(BaseDAO):
	def get_user_by_email(self, email: str) -> Optional[User]:
		try:
			return self.session.query(User).filter(User.email == email).one_or_none()
		except NoUserFound:
			return None

	def get_by_id(self, uid: int) -> Optional[User]:
		try:
			return self.session.query(User).get(uid)
		except NoUserFound:
			return None

	def create_user(self, user_data: dict) -> User:
		entity = User(**user_data)
		self.session.add(entity)
		self.session.commit()
		return entity

	def update_user_by_email(self, user_data: dict, email: str) -> None:
		self.session.query(User).filter(User.email == email).update(user_data)
		# self.session.add(user_data)
		self.session.commit()

	# def delete(self, uid: int) -> None:
	# 	user_data = self.get_by_id(uid)
	# 	self.session.delete(user_data)
	# 	self.session.commit()
