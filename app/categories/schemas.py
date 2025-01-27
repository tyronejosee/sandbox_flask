from marshmallow import validates, ValidationError, fields

from app.extensions import ma
from app.categories.models import Category


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True
        include_relationships = True
        ordered = True

    id = fields.UUID()
    name = fields.String(required=True, validate=lambda x: len(x) >= 5)
    description = fields.String(required=True, validate=lambda x: len(x) >= 5)
    is_available = fields.Bool()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    @validates("name")
    def validate_description(self, value) -> None:
        if len(value) > 255:
            raise ValidationError("The name must not exceed 255 characters.")


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
