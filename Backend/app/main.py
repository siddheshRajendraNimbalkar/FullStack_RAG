from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.collections import (
    router as collection_router
)

from app.api.documents import router as documents_router

from app.api.debug import (
    router as debug_router
)

from app.api.chat import (
    router as chat_router
)

from app.api.chat import (
    router as history_router
)

from app.api.voice import (
    router as voice_router
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

app.include_router(documents_router)



app.include_router(
    debug_router
)



app.include_router(
    chat_router
)

app.include_router(history_router)

app.include_router(
    voice_router
)