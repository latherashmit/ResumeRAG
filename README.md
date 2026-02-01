# Resume RAG Reviewer

An AI-powered **Resume Review & Skill Gap Analyzer** built using **Retrieval-Augmented Generation (RAG)**. The system semantically compares a candidate’s resume against a job description and provides **actionable feedback**, **missing skills**, and **resume improvement suggestions** using **Gemini LLM**.

---

## ✨ Key Features

* 📄 Upload resume (PDF / DOCX)
* 🧠 Semantic JD–Resume matching using embeddings
* 🔍 Skill gap detection & improvement suggestions
* ✍️ Resume bullet-point rewriting
* ⚡ Fast, local vector search with ChromaDB
* 🌐 Clean full-stack setup (React + FastAPI)

---

## 🧠 System Overview (RAG Flow)

1. Resume is uploaded and parsed into clean text
2. Resume text is chunked and embedded using **Gemini Embeddings**
3. Embeddings are stored in **ChromaDB** (vector database)
4. User submits a query along with a Job Description
5. Relevant resume chunks are retrieved semantically
6. Retrieved context + JD are sent to **Gemini LLM**
7. AI-generated feedback is returned to the UI

---

## 🛠️ Tech Stack

### Frontend

* **React + Vite** – UI framework
* **Axios** – API communication
* (Optional) Tailwind CSS – styling

### Backend

* **FastAPI** – API server
* **LangChain** – RAG utilities
* **Gemini Pro** – LLM for reasoning
* **Gemini Embeddings** – semantic search
* **ChromaDB** – vector storage
* **PyMuPDF / python-docx** – document parsing

---

## 📁 Project Structure

```
resume-rag-reviewer/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/routes.py
│   │   ├── rag/
│   │   │   ├── parser.py
│   │   │   ├── chunker.py
│   │   │   ├── embeddings.py
│   │   │   └── retriever.py
│   │   ├── core/prompt.py
│   │   └── vectorstore/chroma_db/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── api/client.js
│   │   └── App.jsx
│   └── vite.config.js
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend runs at: `http://localhost:8000`

---

### 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:5173`

---

## 📌 Example Queries

* "What skills am I missing for this role?"
* "Rewrite my resume bullets for ATS"
* "How well does my resume match this JD?"

---

## 🎯 Use Cases

* Internship & job preparation
* Resume optimization for ATS systems
* Skill gap analysis for students
* AI-powered career guidance

---

## 🧪 Future Improvements

* Section-wise resume parsing (skills, projects, experience)
* ATS score estimation
* Chat-style conversation history
* Cloud vector DB (Pinecone / Weaviate)
* Authentication & user profiles

---
