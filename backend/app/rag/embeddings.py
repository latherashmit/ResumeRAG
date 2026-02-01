import os
from google import genai
from chromadb import Client
from chromadb.config import Settings


gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


chroma_client = Client(
    Settings(
        persist_directory="app/vectorstore/chroma_db",
        anonymized_telemetry=False
    )
)

def embed_and_store(chunks, collection_name):
    collection = chroma_client.get_or_create_collection(
        name=collection_name
    )

    for idx, chunk in enumerate(chunks):
        response = gemini_client.models.embed_content(
            model="models/text-embedding-004",
            contents=chunk
        )

       
        embedding = response.embedding

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"{collection_name}_{idx}"]
        )

def query_embeddings(query, collection_name, k=5):
    collection = chroma_client.get_or_create_collection(
        name=collection_name
    )

    response = gemini_client.models.embed_content(
        model="models/text-embedding-004",
        contents=query
    )

    query_embedding = response["embedding"]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results["documents"][0]