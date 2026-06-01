from sqlalchemy.orm import Session

from app.models.collection import Collection


def create_collection(
    db: Session,
    user_id,
    name: str
):
    collection = Collection(
        name=name,
        user_id=user_id
    )

    db.add(collection)
    db.commit()
    db.refresh(collection)

    return collection


def get_collections(
    db: Session,
    user_id
):
    return (
        db.query(Collection)
        .filter(Collection.user_id == user_id)
        .all()
    )


def get_collection(
    db: Session,
    collection_id,
    user_id
):
    return (
        db.query(Collection)
        .filter(
            Collection.id == collection_id,
            Collection.user_id == user_id
        )
        .first()
    )


def delete_collection(
    db: Session,
    collection
):
    db.delete(collection)
    db.commit()

