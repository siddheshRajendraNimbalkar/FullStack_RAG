from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    Docx2txtLoader
)

def load_document(path: str):

    if path.endswith(".pdf"):
        loader = PyPDFLoader(path)

    elif path.endswith(".docx"):
        loader = Docx2txtLoader(path)

    elif path.endswith(".txt"):
        loader = TextLoader(path,encoding="utf-8")

    elif path.endswith(".csv"):
        loader = CSVLoader(path)

    elif path.endswith(".md"):
        loader = TextLoader(path)

    else:
        raise ValueError(
            "Unsupported file type"
        )

    return loader.load()