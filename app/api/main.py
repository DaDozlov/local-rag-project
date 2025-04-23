from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from ml.models.rag_model import rag_chain

app = FastAPI(title="DeepSeek‑R1 RAG API")


class Query(BaseModel):
    question: str


@app.post("/query")
async def query(payload: Query):
    try:
        answer = rag_chain.invoke(payload.question)
        return {"answer": answer.content}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
