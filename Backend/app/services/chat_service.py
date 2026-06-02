from app.services.chroma_service import (
    get_retriever
)

from app.services.llm_service import (
    get_llm
)

from app.services.prompt_service import (
    RAG_PROMPT
)


def ask_collection(
    collection_id: str,
    question: str
):
    retriever = get_retriever(
        collection_id=collection_id,
        k=5
    )

    docs = retriever.invoke(
        question
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    llm = get_llm()

    response = llm.invoke(
        prompt
    )

    return {
        "answer": response.content,
        "sources": [
            {
                "filename": doc.metadata.get(
                    "filename"
                ),
                "document_id": doc.metadata.get(
                    "document_id"
                )
            }
            for doc in docs
        ]
    }


def build_history(chats):

    history = []

    for chat in chats:

        history.append(
            f"User: {chat.question}"
        )

        history.append(
            f"Assistant: {chat.answer}"
        )

    return "\n".join(history)