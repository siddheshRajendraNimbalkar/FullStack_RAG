from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_EXPIRE_MINUTES = int(
    os.getenv("JWT_EXPIRE_MINUTES")
)

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL"
)

OLLAMA_LLM = os.getenv(
    "OLLAMA_LLM"
)

OLLAMA_EMBEDDING_MODEL = os.getenv(
    "OLLAMA_EMBEDDING_MODEL"
)