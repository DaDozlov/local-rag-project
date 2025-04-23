import os

from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

from ml.pipelines.retriever import build_retriever


def test_precision_at_k(tmp_path):
    # Documents to seed the vector store
    test_docs = [
        Document(page_content="This repository structure is important."),
        Document(
            page_content="Repository layout includes app/, ml/, and infra/."
        ),
        Document(page_content="Completely unrelated content."),
    ]

    # Use test-specific DB location
    if os.getenv("USE_FAKE_EMBEDDINGS") == "1":
        from langchain_community.embeddings import FakeEmbeddings

        embedding = FakeEmbeddings(size=1536)
    else:
        from langchain_community.embeddings import OllamaEmbeddings

        embedding = OllamaEmbeddings(model="nomic-embed-text")

    # Create and persist the vector store
    Chroma.from_documents(
        documents=test_docs,
        embedding=embedding,
        persist_directory=str(tmp_path),
    )

    # Build retriever on the seeded DB
    retriever = build_retriever(persist_dir=str(tmp_path))

    # Query the retriever
    query = "repository structure"
    docs = retriever.get_relevant_documents(query)
    hits = [d for d in docs if "repository" in d.page_content.lower()]
    precision = len(hits) / len(docs) if docs else 0

    assert len(docs) > 0, "Retriever returned no documents"
    assert precision >= 0.5, f"Precision too low: {precision}"
