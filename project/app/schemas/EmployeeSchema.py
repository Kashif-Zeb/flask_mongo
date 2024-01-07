from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
)
from project.app.schemas.DepartmentSchema import DepartmentSchema
from project.app.schemas.StoreSchema import StoreSchema


class EmployeeSchema(Schema):
    _id = fields.Integer(dump_only=True)
    first_name = fields.String(
        validate=validate.Length(min=2, max=50),
        required=True,
    )
    last_name = fields.String(
        validate=validate.Length(min=2, max=50),
        required=True,
    )
    role = fields.String(required=True)
    store_id = fields.Integer(required=True)
    department_id = fields.Integer(required=True)


class employee_ESD_schema(Schema):
    first_name = fields.String(
        validate=validate.Length(min=2, max=50),
        required=True,
    )
    last_name = fields.String(
        validate=validate.Length(min=2, max=50),
        required=True,
    )
    role = fields.String(required=True)
    department = fields.Nested(DepartmentSchema)
    store = fields.Nested(StoreSchema)
