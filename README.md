Siap 👍
Di bawah ini saya **siapkan README.md yang langsung bisa kamu pakai** (tinggal copy–paste), **bahasanya sesuai standar take-home test**, dan **jelas menjawab semua poin soal quiz**.
Setelah ini, **secara administratif & teknis kamu sudah sangat layak lolos**.

---

# ✅ README.md (SIAP SUBMIT)

Silakan **copy seluruh isi di bawah ini** ke file `README.md` di root repository GitHub kamu.

---

```md
# Retrieval-Augmented Generation (RAG) with Qdrant and Open-Source LLM

## Overview
This project implements a simple **Retrieval-Augmented Generation (RAG)** system using Python.  
The system ingests documents into a vector database (Qdrant), retrieves relevant document chunks based on semantic similarity, and augments the prompt for a Large Language Model (LLM) to generate context-aware answers.

This project is built as a take-home assignment for a Python Developer role.

---

## Architecture
High-level flow:

User Question  
→ Generate embedding  
→ Similarity search in Qdrant  
→ Retrieve relevant document chunks  
→ Construct augmented prompt  
→ Send prompt to open-source LLM (Ollama)  
→ Return generated answer

---

## Tech Stack
- **Python 3.12**
- **FastAPI** – REST API framework
- **Qdrant** – Vector database (Docker-based)
- **Sentence-Transformers** – Text embeddings
- **Ollama** – Open-source LLM runtime (TinyLlama / Phi-3)
- **Docker & Docker Compose**

---

## Project Structure
```

rag-qdrant-fastapi/
│
├── app/
│   ├── main.py        # FastAPI entry point
│   ├── rag.py         # Retrieval & generation logic
│   ├── ingest.py      # Document ingestion pipeline
│   └── settings.py    # Configuration
│
├── data/
│   └── docs/          # Input documents (.txt)
│
├── docker-compose.yml
├── requirements.txt
└── README.md

````

---

## Setup Instructions

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd rag-qdrant-fastapi
````

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Qdrant (Docker)

```bash
docker compose up -d
```

Verify:

```bash
curl http://localhost:6333/healthz
```

---

### 4. Install & Run Ollama

Install Ollama following instructions from [https://ollama.com](https://ollama.com)

Pull a lightweight open-source model:

```bash
ollama pull tinyllama
```

Verify:

```bash
curl http://127.0.0.1:11434/api/tags
```

---

### 5. Prepare Documents

Place `.txt` files under:

```
data/docs/
```

Example:

```txt
Perusahaan menerapkan kebijakan cuti tahunan 12 hari kerja per tahun.
Pengajuan cuti dilakukan minimal H-3 melalui aplikasi internal.
```

---

### 6. Ingest Documents into Qdrant

```bash
python -m app.ingest
```

---

### 7. Run API Server

```bash
uvicorn app.main:app --reload --port 8000
```

---

## API Usage

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

### Ask Question

```http
POST /ask
```

Request:

```json
{
  "question": "Berapa jatah cuti tahunan per tahun?",
  "top_k": 5
}
```

Response:

```json
{
  "answer": "Kebijakan cuti tahunan adalah 12 hari kerja per tahun.",
  "contexts": [
    {
      "score": 0.62,
      "text": "Perusahaan menerapkan kebijakan cuti tahunan 12 hari kerja per tahun.",
      "source": "contoh.txt"
    }
  ]
}
```

---

## Notes

* This project uses **open-source LLMs** (no API key required).
* Lightweight models are used to ensure compatibility with local environments.
* The focus of this project is **correct RAG pipeline implementation**, not LLM response quality.

---

## Future Improvements

* Deterministic document IDs to avoid duplicate ingestion
* Smarter chunking (sentence-based)
* Metadata filtering in Qdrant
* Streaming LLM responses

---

## Author

**[Your Name]**
Python Developer Candidate

```

---

# 🎯 Kenapa README ini “AMAN & KUAT” untuk Lolos Test

README ini **secara eksplisit menjawab semua poin soal**:

| Requirement Soal | Terpenuhi |
|-----------------|----------|
| Ingest dokumen ke Qdrant | ✅ |
| Similarity search | ✅ |
| RAG flow jelas | ✅ |
| API endpoint | ✅ |
| Open-source / public LLM | ✅ |
| Setup & run instructions | ✅ |
| Example input/output JSON | ✅ |

Bahasanya:
- ❌ tidak berlebihan
- ❌ tidak klaim “AI canggih”
- ✅ fokus ke engineering & arsitektur

---

# 🧠 Kalimat Penjelasan ke HR / Reviewer (boleh kamu copy)

> “Saya membangun sistem RAG sederhana menggunakan FastAPI, Qdrant, dan open-source LLM via Ollama. Dokumen di-embedding menggunakan sentence-transformers dan disimpan di Qdrant. Saat user bertanya, sistem melakukan similarity search untuk mengambil konteks relevan, lalu mengaugment prompt sebelum dikirim ke LLM. Fokus saya adalah memastikan alur RAG berjalan dengan benar dan dapat direplikasi secara lokal.”

Ini **jawaban yang sangat solid**.

---

## 🔚 Langkah Terakhir Sekarang
1. Pastikan repo GitHub **public**
2. Push code + README
3. Kirim link repo ke HR

Kalau kamu mau, di langkah berikutnya saya bisa:
- 🔹 review README kamu sebelum push
- 🔹 simulasi **pertanyaan interview teknis**
- 🔹 bantu **jawaban non-teknis ke HR**

Tinggal bilang mau lanjut ke bagian mana.
```
