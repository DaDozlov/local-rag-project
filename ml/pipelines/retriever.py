import os

from langchain_community.vectorstores import Chroma

if os.getenv("USE_FAKE_EMBEDDINGS") == "1":
    from langchain_community.embeddings import FakeEmbeddings

    _EMB = FakeEmbeddings(size=1536)
else:
    from langchain_community.embeddings import OllamaEmbeddings

    _EMB = OllamaEmbeddings(model="nomic-embed-text")


def build_retriever(persist_dir: str = "./chromadb"):
    db = Chroma(persist_directory=persist_dir, embedding_function=_EMB)
    return db.as_retriever(search_kwargs={"k": 6})
