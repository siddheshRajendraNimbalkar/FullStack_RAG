from sqlalchemy.orm import Session

from app.models.chat import Chat


def get_recent_chats(
    db: Session,
    user_id,
    collection_id,
    limit: int = 5
):
    chats = (
        db.query(Chat)
        .filter(
            Chat.user_id == user_id,
            Chat.collection_id == collection_id
        )
        .order_by(Chat.created_at.desc())
        .limit(limit)
        .all()
    )

    return list(reversed(chats))