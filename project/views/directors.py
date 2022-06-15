from flask import request
from flask_restx import abort, Namespace, Resource
from project.container import director_service
from project.exceptions import ItemNotFound
from project.schemas import DirectorSchema

directors_ns = Namespace("directors")
director_schema = DirectorSchema()


@directors_ns.route("/")
class DirectorsView(Resource):
    @directors_ns.response(200, "OK")
    def get(self):
        """Get all directors"""
        page_number = request.args.get('page', type=int)

        try:
            directors = director_service.get_all(page_number)
            return director_schema.dump(directors, many=True), 200
        except ItemNotFound:
            abort(404, message="Page is not found")


@directors_ns.route("/<int:director_id>")
class DirectorView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Director is not found")
    def get(self, director_id: int):
        try:
            director = director_service.get_item_by_id(director_id)
            return director_schema.dump(director), 200
        except ItemNotFound:
            abort(404, "Director is not found")
