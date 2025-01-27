from uuid import UUID

from app.products.models import Product
from app.extensions import db


def get_all_products() -> list[Product]:
    return Product.query.all()


def get_product_by_id(product_id) -> Product | None:
    return Product.query.get(product_id)


def create_product(data: dict) -> Product:
    data["category_id"] = UUID(data["category_id"])
    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
    return new_product


def delete_product(product_id: UUID) -> bool:
    product: Product | None = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return True
    return False
