from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.dependencies.auth import (
    get_current_user
)

from app.schemas.chat import (
    ChatRequest
)

from app.services.collection_service import (
    get_collection
)

from app.services.chat_service import (
    ask_collection
)

from app.services.history_service import (
    save_chat
)

from sse_starlette.sse import EventSourceResponse

from app.services.stream_chat_service import (
    stream_collection_answer
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    collection = get_collection(
        db=db,
        collection_id=request.collection_id,
        user_id=current_user.id
    )

    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found"
        )

    result = ask_collection(
        collection_id=request.collection_id,
        question=request.question
    )

    save_chat(
        db=db,
        user_id=current_user.id,
        collection_id=request.collection_id,
        question=request.question,
        answer=payload["answer"]
    )

    return result

import json

@router.post("/stream")
async def stream_chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    collection = get_collection(
        db=db,
        collection_id=request.collection_id,
        user_id=current_user.id
    )

    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found"
        )

    async def event_generator():

        complete_answer = ""

        async for event in stream_collection_answer(
            collection_id=request.collection_id,
            question=request.question
        ):

            if event["event"] == "token":
                complete_answer += event["data"]

            elif event["event"] == "complete":

                payload = json.loads(
                    event["data"]
                )

                complete_answer = payload["answer"]

                save_chat(
                    db=db,
                    user_id=current_user.id,
                    collection_id=request.collection_id,
                    question=request.question,
                    answer=complete_answer
                )

            yield event

    return EventSourceResponse(
        event_generator()
    )