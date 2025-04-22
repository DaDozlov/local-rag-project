import os
import pytest
import textwrap
import pathlib
from fpdf import FPDF

# tell retriever to use FakeEmbeddings
os.environ["USE_FAKE_EMBEDDINGS"] = "1"

@pytest.fixture(scope="session")
def ollama():
    """Backward‑compat dummy; real Ollama is skipped in tests."""
    yield  # nothing to do

@pytest.fixture(scope="session")
def sample_pdf(tmp_path_factory) -> pathlib.Path:
    """Generate a 1‑page PDF for ingestion tests."""
    pdf_file = tmp_path_factory.mktemp("data") / "sample.pdf"
    if not pdf_file.exists():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=textwrap.fill("Local‑RAG test PDF.", 40))
        pdf.output(str(pdf_file))
    return pdf_file