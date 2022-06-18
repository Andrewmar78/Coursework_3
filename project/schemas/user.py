from marshmallow import fields, Schema


class UserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=False)
    surname = fields.Str(required=False)
    email = fields.Str(required=True)
    # password = fields.Str(required=True)
    password = fields.Str(load_only=True)
    favourite_genre = fields.Int()
    role = fields.Str(required=False)
