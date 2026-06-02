from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class DocumentResponse(BaseModel):
    id: UUID
    filename: str
    file_type: str
    file_size: int

    created_at: datetime

    class Config:
        from_attributes = True

