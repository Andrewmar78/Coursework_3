from marshmallow import fields, Schema


class UserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    role = fields.Str(required=False)
