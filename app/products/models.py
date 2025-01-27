from app.extensions import db
from app.utils.base_model import BaseModel


class Product(BaseModel):
    __tablename__ = "products"

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    category_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("categories.id"),
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<Product {self.name} - ${self.price}>"
