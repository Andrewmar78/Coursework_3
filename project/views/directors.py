from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.services import DirectorsService
from project.setup_db import db

directors_ns = Namespace("directors")


@directors_ns.route("/")
class GenresView(Resource):
    @directors_ns.response(200, "OK")
    def get(self):
        """Get all directors"""
        return DirectorsService(db.session).get_all()


@directors_ns.route("/<int:genre_id>")
class DirectorView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Genre is not found")
    def get(self, director_id: int):
        """Get director by id"""
        try:
            return DirectorsService(db.session).get_item_by_id(director_id)
        except ItemNotFound:
            abort(404, message="Director is not found")