from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
)


class SupplierSchema(Schema):
    _id = fields.Integer(dump_only=True)
    supplier_name = fields.String(
        validate=validate.Length(min=2, max=50),
        required=True,
    )
    contact_person = fields.String(
        validate=validate.Length(min=2, max=50),
        required=True,
    )
    email = fields.Email(required=True)
    phone = fields.String(validate=validate.Length(11))
    address = fields.String(required=True)

    @validates("phone")
    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 11:
            raise ValidationError("Phone number must contain only  digits .")


class update_customer_schema(SupplierSchema):
    _id = fields.Integer(required=True)
