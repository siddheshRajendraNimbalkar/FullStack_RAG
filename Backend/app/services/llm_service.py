from langchain_ollama import ChatOllama

from app.core.config import (
    OLLAMA_BASE_URL,
    OLLAMA_LLM
)


llm = ChatOllama(
    model=OLLAMA_LLM,
    base_url=OLLAMA_BASE_URL,
    temperature=0.7
)


def get_llm():
    return llm