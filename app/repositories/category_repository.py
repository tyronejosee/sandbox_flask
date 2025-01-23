from app.models.category_model import Category
from app.extensions import db


def get_all_categories():
    return Category.query.all()


def get_category_by_id(category_id):
    return Category.query.get(category_id)


def create_category(data):
    new_category = Category(**data)
    db.session.add(new_category)
    db.session.commit()
    return new_category


def delete_category(category_id) -> bool:
    category = Category.query.get(category_id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return True
    return False
