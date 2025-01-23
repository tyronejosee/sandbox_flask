import uuid
from datetime import datetime, timezone

from app.extensions import db


class BaseModel(db.Model):
    """
    Base model class.
    """

    __abstract__ = True

    id = db.Column(
        db.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    is_available = db.Column(
        db.Boolean,
        default=True,
        nullable=False,
    )
