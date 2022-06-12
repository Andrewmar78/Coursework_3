from marshmallow import fields, Schema

from project.schemas.director import DirectorSchema
from project.schemas.genre import GenreSchema


class MovieSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=False)
    trailer = fields.Str(required=False)
    year = fields.Int(required=True)
    rating = fields.Float(required=False)
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)

    # genre_id = fields.Int(required=True)
    # director_id = fields.Int(required=True)
    # status = fields.Str(required=False)
