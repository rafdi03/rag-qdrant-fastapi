from fastapi import FastAPI
from pydantic import BaseModel, Field
from .rag import RAGService

app = FastAPI(title="Simple RAG with Qdrant")
rag = RAGService()

class AskRequest(BaseModel):
    question: str = Field(..., min_length=3)
    top_k: int = Field(5, ge=1, le=10)

class AskResponse(BaseModel):
    answer: str
    contexts: list

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    result = rag.answer(req.question, top_k=req.top_k)
    return result

@app.get("/")
def root():
    return {"message": "API is running. Visit /docs"}