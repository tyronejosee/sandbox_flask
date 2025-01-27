"""
Service layer for Category.
"""

from uuid import UUID


from app.categories.models import Category
from app.categories.repositories import (
    get_all_categories,
    get_category_by_id,
    create_category,
    delete_category,
)


def list_categories() -> list[Category]:
    return get_all_categories()


def get_category(category_id: UUID) -> Category | None:
    return get_category_by_id(category_id)


def add_category(data: dict) -> Category:
    return create_category(data)


def remove_category(category_id: UUID) -> bool:
    return delete_category(category_id)
