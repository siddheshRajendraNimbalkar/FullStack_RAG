from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.collections import (
    router as collection_router
)

app = FastAPI()

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "RAG Backend Running"
    }


app.include_router(
    collection_router
)