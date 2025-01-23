from marshmallow import validates, ValidationError, fields

from app.extensions import ma
from app.models.product_model import Product


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_fk = True
        load_instance = True

    name = fields.String(required=True, validate=lambda x: len(x) >= 5)
    price = fields.Float(required=True, validate=lambda x: x > 0)
    stock = fields.Integer(
        required=True,
        error_messages={"required": "Stock is required."},
    )
    category_id = fields.UUID(
        required=True,
        error_messages={"required": "Category ID is required."},
    )

    @validates("price")
    def validate_price(self, value) -> None:
        if value <= 0:
            raise ValidationError("Price must be greater than zero.")

    @validates("stock")
    def validate_stock(self, value):
        if value < 0:
            raise ValidationError("Stock cannot be negative.")


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
