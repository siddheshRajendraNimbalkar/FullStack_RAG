from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.dependencies.auth import (
    get_current_user
)

from app.services.voice_service import (
    speech_to_text
)

from app.services.tts_service import (
    text_to_speech
)

from app.services.chat_service import (
    ask_collection
)

from app.services.history_service import (
    save_chat
)

from app.services.collection_service import (
    get_collection
)

router = APIRouter(
    prefix="/voice",
    tags=["Voice"]
)

@router.post("/stt")
def transcribe_audio(
    file: UploadFile = File(...)
):
    
    result = speech_to_text(
        file
    )

    return result

@router.post("/chat")
async def voice_chat(
    collection_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    collection = get_collection(
        db=db,
        collection_id=collection_id,
        user_id=current_user.id
    )

    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found"
        )
    
    stt_result = speech_to_text(
        file
    )

    question = stt_result["text"]

    result = ask_collection(
        db=db,
        user_id=current_user.id,
        collection_id=collection_id,
        question=question
    )

    save_chat(
        db=db,
        user_id=current_user.id,
        collection_id=collection_id,
        question=question,
        answer=result["answer"]
    )

    return {
        "question": question,
        "answer": result["answer"],
        "sources": result["sources"]
    }

@router.post("/tts")
def generate_speech(
    text: str
):

    result = text_to_speech(
        text
    )

    return result