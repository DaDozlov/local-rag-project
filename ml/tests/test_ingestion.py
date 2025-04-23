from ml.pipelines.ingestion import load_and_split


def test_load_and_split(sample_pdf):
    chunks = load_and_split(sample_pdf)
    assert len(chunks) > 0
    assert len(chunks[0].page_content) <= 1024
