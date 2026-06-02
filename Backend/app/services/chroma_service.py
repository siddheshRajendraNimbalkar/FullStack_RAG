from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from app.core.config import (
    OLLAMA_BASE_URL,
    OLLAMA_EMBEDDING_MODEL
)


embeddings = OllamaEmbeddings(
    model=OLLAMA_EMBEDDING_MODEL,
    base_url=OLLAMA_BASE_URL
)


def get_chroma_collection(
    collection_id: str
):
    return Chroma(
        collection_name=collection_id,
        embedding_function=embeddings,
        persist_directory="./chroma_db"
    )


def add_documents(
    collection_id: str,
    docs
):
    db = get_chroma_collection(
        collection_id
    )

    db.add_documents(docs)


def delete_document_chunks(
    collection_id: str,
    document_id: str
):
    db = get_chroma_collection(
        collection_id
    )

    result = db._collection.get(
        where={
            "document_id": document_id
        }
    )

    ids = result.get("ids", [])

    if ids:
        db.delete(ids=ids)


def get_retriever(
    collection_id: str,
    k: int = 5
):
    db = get_chroma_collection(
        collection_id
    )

    return db.as_retriever(
        search_kwargs={
            "k": k
        }
    )


def similarity_search(
    collection_id: str,
    query: str,
    k: int = 5
):
    db = get_chroma_collection(
        collection_id
    )

    return db.similarity_search(
        query=query,
        k=k
    )


def similarity_search_with_score(
    collection_id: str,
    query: str,
    k: int = 5
):
    db = get_chroma_collection(
        collection_id
    )

    return db.similarity_search_with_score(
        query=query,
        k=k
    )


def collection_count(
    collection_id: str
):
    db = get_chroma_collection(
        collection_id
    )

    return db._collection.count()


def get_all_documents(
    collection_id: str
):
    db = get_chroma_collection(
        collection_id
    )

    return db._collection.get()


def delete_collection(
    collection_id: str
):
    db = get_chroma_collection(
        collection_id
    )

    all_docs = db._collection.get()

    ids = all_docs.get("ids", [])

    if ids:
        db.delete(ids=ids)