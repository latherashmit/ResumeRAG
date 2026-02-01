from fastapi import APIRouter, UploadFile, File
from app.rag.parser import parse_document
from app.rag.chunker import chunk_text
from app.rag.embeddings import embed_and_store, query_embeddings
from app.core.prompt import build_prompt

router = APIRouter()

RESUME_COLLECTION = "resume_chunks"

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    text = parse_document(file)
    chunks = chunk_text(text)
    embed_and_store(chunks, RESUME_COLLECTION)
    return {"message": "Resume uploaded and indexed"}

@router.post("/analyze")
async def analyze_resume(query: str, jd: str):
    retrieved_chunks = query_embeddings(query, RESUME_COLLECTION)

    prompt = build_prompt(
        resume_context=retrieved_chunks,
        jd_text=jd,
        user_query=query
    )

    from google.generativeai import GenerativeModel
    model = GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return {"analysis": response.text}
