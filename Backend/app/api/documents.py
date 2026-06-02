from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dependencies.auth import get_current_user

from app.models.document import Document

from app.services.collection_service import get_collection
from app.services.upload_service import save_file
from app.services.document_loader import load_document
from app.services.chunk_service import split_documents
from app.services.chroma_service import add_documents

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload")
async def upload_document(
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

    # Save file
    path = await save_file(
        collection_id,
        file
    )

    # Create database record
    document = Document(
        collection_id=collection.id,
        filename=file.filename,
        file_path=path,
        file_type=file.content_type,
        file_size=0
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    # Load document
    docs = load_document(path)

    # Create chunks
    chunks = split_documents(docs)

    # Add metadata
    for chunk in chunks:
        chunk.metadata.update({
            "document_id": str(document.id),
            "collection_id": str(collection.id),
            "filename": document.filename
        })

    # Store chunks in Chroma
    add_documents(
        collection_id=str(collection.id),
        docs=chunks
    )

    return {
        "message": "File uploaded successfully",
        "document_id": str(document.id),
        "chunks": len(chunks)
    }