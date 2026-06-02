from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template(
"""
You are a helpful AI assistant.

Use the conversation history and context.

If the answer is not available in the context,
say:

"I could not find that information in the uploaded documents."

Conversation History:
{history}

Context:
{context}

Question:
{question}

Answer:
"""
)