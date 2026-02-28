from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    QDRANT_URL: str = "http://localhost:6333"
    COLLECTION_NAME: str = "documents"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    OLLAMA_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "tinyllama" 

settings = Settings()
