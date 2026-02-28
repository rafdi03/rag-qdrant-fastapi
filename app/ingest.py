import os
import uuid
from typing import List, Dict
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance, PointStruct
from sentence_transformers import SentenceTransformer
from app.setting import settings

def read_txt_files(folder: str) -> List[Dict]:
    docs = []
    if not os.path.isdir(folder):
        return docs
    for fn in os.listdir(folder):
        if fn.lower().endswith(".txt"):
            path = os.path.join(folder, fn)
            with open(path, "r", encoding="utf-8") as f:
                docs.append({"source": fn, "text": f.read().strip()})
    return docs

def chunk_text(text: str, chunk_size: int = 800, overlap: int = 150) -> List[str]:
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i:i+chunk_size])
        i += max(1, chunk_size - overlap)
    return [c.strip() for c in chunks if c.strip()]

def main():
    qdrant = QdrantClient(url=settings.QDRANT_URL)
    embedder = SentenceTransformer(settings.EMBEDDING_MODEL)

    dim = embedder.get_sentence_embedding_dimension()
    existing = [c.name for c in qdrant.get_collections().collections]
    if settings.COLLECTION_NAME not in existing:
        qdrant.create_collection(
            collection_name=settings.COLLECTION_NAME,
            vectors_config=VectorParams(size=dim, distance=Distance.COSINE)
        )

    docs = read_txt_files("data/docs")
    points = []

    for d in docs:
        for chunk in chunk_text(d["text"]):
            vec = embedder.encode(chunk, normalize_embeddings=True).tolist()
            points.append(PointStruct(
                id=str(uuid.uuid4()),
                vector=vec,
                payload={"text": chunk, "source": d["source"]}
            ))

    if points:
        qdrant.upsert(collection_name=settings.COLLECTION_NAME, points=points)
        print(f"Inserted {len(points)} chunks into '{settings.COLLECTION_NAME}'")
    else:
        print("No documents found. Put .txt files under data/docs")

if __name__ == "__main__":
    main()