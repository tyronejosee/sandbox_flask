"""
Service layer for Category.
"""

from app.models.category_model import Category
from app.repositories.category_repository import (
    get_all_categories,
    get_category_by_id,
    create_category,
)


def list_categories():
    return get_all_categories()


def get_category(category_id):
    return get_category_by_id(category_id)


def add_category(data) -> Category:
    return create_category(data)
