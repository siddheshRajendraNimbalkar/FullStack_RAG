from pydantic import BaseModel


class ChatRequest(BaseModel):
    collection_id: str
    question: str


class ChatResponse(BaseModel):
    answer: str