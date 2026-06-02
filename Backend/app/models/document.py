import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import BigInteger

from datetime import datetime

from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    collection_id = Column(
        UUID(as_uuid=True),
        ForeignKey("collections.id")
    )

    filename = Column(
        String,
        nullable=False
    )

    file_path = Column(
        String,
        nullable=False
    )


    file_type = Column(String)
    file_size = Column(BigInteger)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )