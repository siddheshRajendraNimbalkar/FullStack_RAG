from sqlalchemy.orm import Session

from app.models.chat import Chat


def save_chat(
    db: Session,
    user_id,
    collection_id,
    question,
    answer
):
    chat = Chat(
        user_id=user_id,
        collection_id=collection_id,
        question=question,
        answer=answer
    )

    db.add(chat)
    db.commit()

    return chat