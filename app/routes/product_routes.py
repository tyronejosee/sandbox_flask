from flask import Blueprint, request, jsonify

from app.services.product_service import (
    list_products,
    get_product,
    add_product,
)
from app.schemas.product_schema import (
    product_schema,
    products_schema,
)

product_bp = Blueprint("product_bp", __name__, url_prefix="/api")


@product_bp.route("/products", methods=["GET"])
def get_products():
    products = list_products()
    return jsonify(products_schema.dump(products)), 200


@product_bp.route("/products/<uuid:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = get_product(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    return product_schema.jsonify(product), 200


@product_bp.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    errors = product_schema.validate(data)
    if errors:
        return jsonify({"errors": errors}), 400
    new_product = add_product(data)
    return product_schema.jsonify(new_product), 201
