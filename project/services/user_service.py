import base64
import hashlib
import hmac
from project.dao.models import User
from project.dao.user import UserDAO
from project.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from project.exceptions import NoUserFound, UserAlreadyExists, IncorrectPassword


class UserService:
	def __init__(self, dao: UserDAO):
		self.dao = dao

	def get_user_by_email(self, email: str) -> User:
		user = self.dao.get_user_by_email(email)
		if not user:
			raise NoUserFound
		return user

	def create_user(self, user_data: dict) -> User:
		user = self.dao.get_user_by_email(user_data.get('email'))
		if user:
			raise UserAlreadyExists
		user_data["password"] = self.generate_user_password(user_data["password"])
		user = self.dao.create_user(user_data)
		return user

	def update_user(self, user_data: dict, email: str) -> None:
		self.get_user_by_email(email)
		if 'email' not in user_data.keys() and 'password' not in user_data.keys():
			self.dao.update_user_by_email(user_data, email)

	# def delete(self, uid: int) -> None:
	# 	self.dao.delete(uid)

	# def get_by_id(self, uid: int) -> User:
	# 	user = self.dao.get_by_id(uid)
	# 	if not user:
	# 		raise NoUserFound
	# 	return user

	def generate_password_digest(self, password: str):
		# from security.py
		""" Создание хэшированного пароля"""
		hash_digest = hashlib.pbkdf2_hmac(
			hash_name="sha256",
			password=password.encode("utf-8"),
			salt=PWD_HASH_SALT,
			iterations=PWD_HASH_ITERATIONS
		)
		return hash_digest

	def generate_user_password(self, password: str):
		"""Создание закодированного из хэша пароля в байтах"""
		hash_digest = self.generate_password_digest(password)
		encoded_digest = base64.b64encode(hash_digest)
		return encoded_digest

	def compare_passwords(self, password_hash, other_password) -> bool:
		"""Сравнение вводимого и заданного паролей"""
		decoded_digest = base64.b64decode(password_hash)
		passed_hash = self.generate_password_digest(other_password)
		return hmac.compare_digest(decoded_digest, passed_hash)

	def update_password(self, data: dict, email: str) -> None:
		user = self.get_user_by_email(email)
		current_password = data.get('current_password')
		new_password = data.get('new_password')

		if not self.compare_passwords(user.password, current_password):
			raise IncorrectPassword

		data = {'password': self.generate_password_digest(new_password)}
		self.dao.update_user_by_email(data, email)
