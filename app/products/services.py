"""
Service layer for product.
"""

from uuid import UUID

from app.products.models import Product
from app.products.repositories import (
    get_all_products,
    get_product_by_id,
    create_product,
)


def list_products() -> list[Product]:
    return get_all_products()


def get_product(product_id: UUID) -> Product | None:
    return get_product_by_id(product_id)


def add_product(data: dict) -> Product:
    return create_product(data)
