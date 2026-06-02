from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.dependencies.auth import (
    get_current_user
)

from app.models.chat import Chat

router = APIRouter(
    prefix="/history",
    tags=["History"]
)

@router.get("/")
def get_history(
    collection_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    chats = (
        db.query(Chat)
        .filter(
            Chat.user_id == current_user.id,
            Chat.collection_id == collection_id
        )
        .order_by(Chat.created_at.desc())
        .all()
    )

    return chats


