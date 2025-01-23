"""
Service layer for product.
"""

from app.models.product_model import Product
from app.repositories.product_repository import (
    get_all_products,
    get_product_by_id,
    create_product,
)


def list_products():
    return get_all_products()


def get_product(product_id):
    return get_product_by_id(product_id)


def add_product(data) -> Product:
    return create_product(data)
