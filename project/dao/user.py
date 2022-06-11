#  Недоработан
from project.dao.base import BaseDAO
from project.dao.models import User
from project.schemas.user import UserSchema


class UserDAO(BaseDAO):
	def get_user_bu_name(self, username):
		return self.session.query(User).filter(User.username == username).first()

	def get_one(self, uid):
		return self.session.query(User).get(uid)

	def create_user(self, user_data):
		entity = User(**user_data)
		self.session.add(entity)
		self.session.commit()
		new_user = UserSchema().dump(entity)
		return new_user

	def update(self, user_data):
		self.session.add(user_data)
		self.session.commit()

	def delete(self, uid):
		user_data = self.get_one(uid)
		self.session.delete(user_data)
		self.session.commit()
