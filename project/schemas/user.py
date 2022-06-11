from marshmallow import fields, Schema


class UserSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Str(required=True)
    username = fields.Str(required=True)
    # password = fields.Str(required=True)
    password = fields.Str(load_only=True)
    surname = fields.Str()
    # role = fields.Str(required=False)

    favourite_genre = fields.Int()
