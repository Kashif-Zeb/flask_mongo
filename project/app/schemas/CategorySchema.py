from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
)


class CategorySchema(Schema):
    _id = fields.Integer(dump_only=True)
    category_name = fields.String(
        validate=validate.Length(min=2, max=50),
        required=True,
    )
