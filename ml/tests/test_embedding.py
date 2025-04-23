from ml.pipelines.embedding import embed
from ml.pipelines.ingestion import load_and_split


def test_embedding_vector_shape(sample_pdf):
    chunks = load_and_split(sample_pdf)
    collection = embed(chunks)
    assert collection.count() == len(chunks)
    # spot‑check one vector length
    v = collection.get(include=["embeddings"])["embeddings"][0]
    assert len(v) in {1024, 768, 512}
