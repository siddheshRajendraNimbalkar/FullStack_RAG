from langchain_chroma import Chroma

from langchain_ollama import (
    OllamaEmbeddings
)

from app.core.config import (
    OLLAMA_BASE_URL,
    OLLAMA_EMBEDDING_MODEL
)

embeddings = OllamaEmbeddings(
    model=OLLAMA_EMBEDDING_MODEL,
    base_url=OLLAMA_BASE_URL
)

def get_collection(collection_id: str):

    return Chroma(
        collection_name=collection_id,
        embedding_function=embeddings,
        persist_directory="./chroma_db"
    )

def add_documents(
    collection_id: str,
    docs
):

    db = get_collection(
        collection_id
    )

    db.add_documents(docs)