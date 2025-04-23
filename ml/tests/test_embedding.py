from typing import List, cast
from ml.pipelines.embedding import embed
from ml.pipelines.ingestion import load_and_split


def test_embedding_vector_shape(sample_pdf, tmp_path):
    chunks = load_and_split(sample_pdf)
    collection = embed(
        chunks, collection_name="test_embed", db_path=str(tmp_path)
    )

    assert collection.count() == len(chunks)

    result = collection.get(include=["embeddings"])
    assert result is not None and "embeddings" in result

    embeddings = cast(List[List[float]], result["embeddings"])

    assert len(embeddings[0]) in {384, 512, 768, 1024}
