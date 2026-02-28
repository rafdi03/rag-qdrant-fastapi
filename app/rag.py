from typing import List, Dict, Any
import requests
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from app.setting import settings

class RAGService:
    def __init__(self):
        self.embedder = SentenceTransformer(settings.EMBEDDING_MODEL)
        self.qdrant = QdrantClient(url=settings.QDRANT_URL)

    def embed(self, text: str) -> List[float]:
        return self.embedder.encode(text, normalize_embeddings=True).tolist()

    def retrieve(self, question: str, top_k: int = 5) -> List[Dict[str, Any]]:
        qvec = self.embed(question)
        hits = self.qdrant.search(
            collection_name=settings.COLLECTION_NAME,
            query_vector=qvec,
            limit=top_k,
        )
        results = []
        for h in hits:
            payload = h.payload or {}
            results.append({
                "score": float(h.score),
                "text": payload.get("text", ""),
                "source": payload.get("source", "unknown"),
            })
        return results

    def build_prompt(self, question: str, contexts: List[Dict[str, Any]]) -> str:
        ctx_block = "\n\n".join(
            [f"[{i+1}] (source: {c['source']})\n{c['text']}"
             for i, c in enumerate(contexts)]
        )
        return f"""You are a helpful assistant. Answer the question ONLY using the provided context.
If the context is insufficient, say you don't know.

CONTEXT:
{ctx_block}

QUESTION:
{question}

ANSWER (in Indonesian):
"""

    def call_ollama(self, prompt: str) -> str:
        resp = requests.post(
            f"{settings.OLLAMA_URL}/api/generate",
            json={"model": settings.OLLAMA_MODEL, "prompt": prompt, "stream": False},
            timeout=120
        )
        resp.raise_for_status()
        return resp.json().get("response", "").strip()

    def answer(self, question: str, top_k: int = 5) -> Dict[str, Any]:
        contexts = self.retrieve(question, top_k=top_k)
        prompt = self.build_prompt(question, contexts)
        output = self.call_ollama(prompt)
        return {"answer": output, "contexts": contexts}