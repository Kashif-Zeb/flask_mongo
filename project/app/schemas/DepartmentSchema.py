from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
)


class DepartmentSchema(Schema):
    _id = fields.Integer(dump_only=True)
    department_name = fields.String(
        validate=validate.Length(min=2, max=50),
        required=True,
    )
