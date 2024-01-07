from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
)
from project.app.schemas.CategorySchema import CategorySchema
from project.app.schemas.SupplierSchema import SupplierSchema


class ProductSchema(Schema):
    _id = fields.Integer(dump_only=True)
    product_name = fields.String(
        validate=validate.Length(min=2, max=50),
        required=True,
    )
    description = fields.String(required=True)
    price = fields.Integer(required=True)
    stock = fields.Integer(required=True)
    supplier_id = fields.Integer(required=True)
    category_id = fields.Integer(required=True)


class product_SC(ProductSchema):
    supplier_id = fields.Integer(required=False)
    category_id = fields.Integer(required=False)
    supplier = fields.Nested(SupplierSchema)
    category = fields.Nested(CategorySchema)
