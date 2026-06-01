from pydantic import BaseModel
from uuid import UUID


class CreateCollectionRequest(BaseModel):
    name: str


class CollectionResponse(BaseModel):
    id: UUID
    name: str

    class Config:
        from_attributes = True