import uuid

from app.models.product_model import Product
from app.extensions import db


def get_all_products():
    return Product.query.all()


def get_product_by_id(product_id):
    return Product.query.get(product_id)


def create_product(data):
    data["category_id"] = uuid.UUID(data["category_id"])
    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
    return new_product


def delete_product(product_id) -> bool:
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return True
    return False
