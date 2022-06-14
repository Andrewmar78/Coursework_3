from flask import request
from flask_restx import abort, Namespace, Resource
from project.container import genre_service
from project.exceptions import ItemNotFound
from project.schemas import GenreSchema

genres_ns = Namespace("genres")
genre_schema = GenreSchema()


@genres_ns.route("/")
class GenresView(Resource):
    @genres_ns.response(200, "OK")
    def get(self):
        """Get all genres"""
        # Для пагинации:
        page_number = request.args.get('page', type=int)

        try:
            # genres = genre_service.get_all()
            genres = genre_service.get_all(page_number)
            return genre_schema.dump(genres, many=True), 200
        except ItemNotFound:
            abort(404, message="Page is not found")


@genres_ns.route("/<int:genre_id>")
class GenreView(Resource):
    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Director is not found")
    def get(self, genre_id: int):
        try:
            genre = genre_service.get_item_by_id(genre_id)
            return genre_schema.dump(genre), 200
        except ItemNotFound:
            abort(404, "Genre is not found")
