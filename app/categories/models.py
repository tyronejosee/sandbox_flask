from app import db
from app.utils.base_model import BaseModel


class Category(BaseModel):
    """
    Category model.
    """

    __tablename__ = "categories"

    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self) -> str:
        return f"<Category {self.name}>"
