from fastapi import APIRouter

from app.services.chroma_service import (
    similarity_search,
    collection_count
)

router = APIRouter(
    prefix="/debug",
    tags=["Debug"]
)


@router.get("/count")
def count_chunks(
    collection_id: str
):
    return {
        "chunks": collection_count(
            collection_id
        )
    }


@router.get("/search")
def search_chunks(
    collection_id: str,
    query: str
):
    docs = similarity_search(
        collection_id,
        query
    )

    return [
        {
            "content": doc.page_content,
            "metadata": doc.metadata
        }
        for doc in docs
    ]