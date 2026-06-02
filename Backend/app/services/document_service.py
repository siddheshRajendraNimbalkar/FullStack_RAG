from sqlalchemy.orm import Session

from app.models.document import Document


def get_documents(
    db: Session,
    collection_id
):
    return (
        db.query(Document)
        .filter(
            Document.collection_id == collection_id
        )
        .all()
    )


def get_document(
    db: Session,
    document_id
):
    return (
        db.query(Document)
        .filter(
            Document.id == document_id
        )
        .first()
    )


def delete_document(
    db: Session,
    document
):
    db.delete(document)
    db.commit()