from ml.pipelines.retriever import build_retriever
import os

def test_precision_at_k(tmp_path):
    retriever = build_retriever()
    query = "repository structure"
    docs = retriever.get_relevant_documents(query)
    hits = [d for d in docs if "repository" in d.page_content.lower()]
    precision = len(hits) / len(docs) if docs else 0
    assert precision >= 0.5
    
    if os.getenv("USE_FAKE_EMBEDDINGS") == "1":
        assert len(docs) > 0
    else:
        assert precision >= 0.5