from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
)


class StoreSchema(Schema):
    _id = fields.Integer(dump_only=True)
    store_name = fields.String(
        validate=validate.Length(min=2, max=50),
        required=True,
    )
    location = fields.String(required=True)
