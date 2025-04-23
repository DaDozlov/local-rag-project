import pytest
from fastapi import status
from fastapi.testclient import TestClient

from app.api.main import app

client = TestClient(app)


@pytest.mark.skipif(app.debug, reason="skip in debug mode")
def test_query_endpoint():
    r = client.post("/query", json={"question": "What is DeepSeek‑R1?"})
    assert r.status_code == status.HTTP_200_OK
    assert "DeepSeek" in r.json()["answer"]
