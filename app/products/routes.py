from uuid import UUID

from flask import Blueprint, Response, request, jsonify

from app.products.models import Product
from app.products.services import (
    list_products,
    get_product,
    add_product,
)
from app.products.schemas import (
    product_schema,
    products_schema,
)

product_bp = Blueprint("product_bp", __name__, url_prefix="/api")


@product_bp.route("/products", methods=["GET"])
def get_products() -> tuple[Response, int]:
    products: list[Product] = list_products()
    return jsonify(products_schema.dump(products)), 200


@product_bp.route("/products/<uuid:product_id>", methods=["GET"])
def get_product_by_id(product_id: UUID) -> tuple[Response, int]:
    product: Product | None = get_product(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    return product_schema.jsonify(product), 200


@product_bp.route("/products", methods=["POST"])
def create_product() -> tuple[Response, int]:
    data: dict = request.get_json()
    errors: dict[str, list[str]] = product_schema.validate(data)
    if errors:
        return jsonify({"errors": errors}), 400
    new_product: Product = add_product(data)
    return product_schema.jsonify(new_product), 201
