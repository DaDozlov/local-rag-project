from ml.models.rag_model import rag_chain


def test_rag_basic():
    resp = rag_chain.invoke("What is this repository about?")
    assert isinstance(resp.content, str)
    assert "repository" in resp.content.lower()
