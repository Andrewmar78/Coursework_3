#  Недоработан
import base64
import hashlib
import hmac

from flask import current_app
from project.dao.user import UserDAO
from project.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
	def __init__(self, dao: UserDAO):
		self.dao = dao

	def get_user_by_name(self, username):
		return self.dao.get_user_bu_name(username)

	def get_one(self, uid):
		return self.dao.get_one(uid)

	# def get_hash(self, password):
	# 	return hashlib.pbkdf2_hmac(
	# 		'sha256',
	# 		password.encode('utf-8'),
	# 		PWD_HASH_SALT,
	# 		PWD_HASH_ITERATIONS
	# 	)

	def generate_password_digest(self, password):
		# from security.py
		return hashlib.pbkdf2_hmac(
			hash_name="sha256",
			password=password.encode("utf-8"),
			salt=PWD_HASH_SALT,
			iterations=PWD_HASH_ITERATIONS,
			# salt=current_app.config["PWD_HASH_SALT"],
			# iterations=current_app.config["PWD_HASH_ITERATIONS"],
			#
		)

	def generate_user_password(self, password):
		# hash_digest = self.get_hash(password)
		hash_digest = self.generate_password_digest(password)

		return base64.b64encode(hash_digest)

	def create_user(self, user_data):
		user_data["password"] = self.generate_user_password(user_data["password"])
		return self.dao.create_user(user_data)

	def update(self, user_data):
		user_data["password"] = self.generate_user_password(user_data["password"])
		self.dao.update(user_data)

	def delete(self, uid):
		self.dao.delete(uid)

	def compare_passwords(self, password_hash, other_password):
		return hmac.compare_digest(
			base64.b64decode(password_hash),
			self.generate_password_digest(other_password)
			# self.get_hash(other_password)
		)
