# app/api/collections.py

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dependencies.auth import get_current_user

from app.schemas.collection import (
    CreateCollectionRequest,
    CollectionResponse
)

from app.services.collection_service import (
    create_collection,
    get_collections,
    get_collection,
    delete_collection
)

router = APIRouter(
    prefix="/collections",
    tags=["Collections"]
)


@router.post(
    "/",
    response_model=CollectionResponse,
    status_code=201
)
def create_new_collection(
    request: CreateCollectionRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    collection = create_collection(
        db=db,
        user_id=current_user.id,
        name=request.name.strip()
    )

    return collection

@router.post("/")
def create_new_collection(
    request: CreateCollectionRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    collection = create_collection(
        db=db,
        user_id=current_user.id,
        name=request.name
    )

    return collection

@router.get("/")
def list_collections(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_collections(
        db=db,
        user_id=current_user.id
    )

@router.get("/{collection_id}")
def get_single_collection(
    collection_id: str,
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

    return collection


@router.delete("/{collection_id}")
def remove_collection(
    collection_id: str,
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

    delete_collection(
        db=db,
        collection=collection
    )

    return {
        "message": "Collection deleted"
    }