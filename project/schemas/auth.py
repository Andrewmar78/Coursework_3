from marshmallow import fields, Schema


class AuthSchema(Schema):
    # id = fields.Int(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
