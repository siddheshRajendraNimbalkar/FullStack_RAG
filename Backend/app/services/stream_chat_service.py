from app.services.chroma_service import (
    get_retriever
)

from app.services.prompt_service import (
    RAG_PROMPT
)

from app.services.llm_service import (
    get_llm
)

from app.services.memory_service import (
    get_recent_chats
)

from app.services.chat_service import build_history

import json

async def stream_collection_answer(
    db,
    user_id,
    collection_id: str,
    question: str
):
    history = get_recent_chats(
        db=db,
        user_id=user_id,
        collection_id=collection_id,
        limit=5
    )

    history_text = build_history(
        history
    )
    retriever = get_retriever(
    collection_id,
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
        history=history_text,
        context=context,
        question=question
    )

    llm = get_llm()

    answer = ""

    async for chunk in llm.astream(prompt):

        content = chunk.content

        if content:
            answer += content

            yield {
                "event": "token",
                "data": content
            }

    yield {
        "event": "complete",
        "data": json.dumps({
            "answer": answer,
            "sources": [
                {
                    "filename": doc.metadata.get("filename"),
                    "document_id": doc.metadata.get("document_id")
                }
                for doc in docs
            ]
        })
    }