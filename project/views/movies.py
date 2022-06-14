from flask import request
from flask_restx import abort, Namespace, Resource

from project.container import movie_service
from project.exceptions import ItemNotFound
from project.schemas import MovieSchema
from project.services import MovieService
from project.setup_db import db

movies_ns = Namespace("movies")
movie_schema = MovieSchema()


@movies_ns.route("/")
class MoviesView(Resource):
    # @auth_required
    @movies_ns.response(200, 'Success')
    @movies_ns.response(404, 'Not found')
    def get(self):
        """Get all movies"""
        page_number = request.args.get('page', type=int)
        status = request.args.get('status', type=str)

        try:
            movies = movie_service.get_all(page_number, status)
            return movie_schema.dump(movies, many=True), 200
        except ItemNotFound:
            abort(404, message="Page is not found")


@movies_ns.route("/<int:movie_id>")
class MovieView(Resource):
    # @auth_required
    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie not found")
    def get(self, movie_id: int):
        """Get movie by id"""
        try:
            movie = movie_service.get_item_by_id(movie_id)
            return movie_schema.dump(movie), 200
        except ItemNotFound:
            abort(404, message="Movie not found")
