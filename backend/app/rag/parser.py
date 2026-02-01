import fitz  # PyMuPDF
from docx import Document
from fastapi import UploadFile

def parse_document(file: UploadFile) -> str:
    if file.filename.endswith(".pdf"):
        doc = fitz.open(stream=file.file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    elif file.filename.endswith(".docx"):
        document = Document(file.file)
        return "\n".join([p.text for p in document.paragraphs])

    else:
        raise ValueError("Unsupported file format")
