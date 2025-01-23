from uuid import UUID
from typing import Union, Any

from flask import Blueprint, Response, request, jsonify

from app.services.category_service import (
    list_categories,
    get_category,
    add_category,
)
from app.schemas.category_schema import category_schema, categories_schema

category_bp = Blueprint("category_bp", __name__, url_prefix="/api")


@category_bp.route("/categories", methods=["GET"])
def get_categories() -> tuple[Response, int]:
    categories: list = list_categories()
    serialized_data: list[dict] = list(categories_schema.dump(categories))
    return jsonify(serialized_data), 200


@category_bp.route("/categories/<uuid:category_id>", methods=["GET"])
def get_category_by_id(category_id: UUID):
    category = get_category(category_id)
    if not category:
        return jsonify({"message": "Category not found"}), 404
    serialized_data: Union[
        dict[str, Any],
        list[dict[str, Any]],
    ] = category_schema.dump(category)
    return jsonify(serialized_data), 200


@category_bp.route("/categories", methods=["POST"])
def create_category():
    data = request.get_json()
    errors = category_schema.validate(data)
    if errors:
        return jsonify({"errors": errors}), 400
    new_category = add_category(data)
    return category_schema.jsonify(new_category), 201
