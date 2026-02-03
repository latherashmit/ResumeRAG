import os
from pathlib import Path

from chromadb import Client
from chromadb.config import Settings
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment.")

genai.configure(api_key=api_key)

chroma_path = Path(__file__).resolve().parent.parent / "vectorstore" / "chroma_db"
chroma_path.mkdir(parents=True, exist_ok=True)

chroma_client = Client(
    Settings(
        persist_directory=str(chroma_path),
        anonymized_telemetry=False
    )
)

def embed_and_store(chunks, collection_name):
    collection = chroma_client.get_or_create_collection(
        name=collection_name
    )

    for idx, chunk in enumerate(chunks):
        response = genai.embed_content(
            model="models/text-embedding-004",
            content=chunk
        )

        embedding = response["embedding"]

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"{collection_name}_{idx}"]
        )

def query_embeddings(query, collection_name, k=5):
    collection = chroma_client.get_or_create_collection(
        name=collection_name
    )

    response = genai.embed_content(
        model="models/text-embedding-004",
        content=query
    )

    query_embedding = response["embedding"]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results["documents"][0]
