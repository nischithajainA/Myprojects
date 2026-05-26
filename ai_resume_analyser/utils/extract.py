import pdfplumber
from docx import Document

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def extract_text_from_docx(docx_path):
    doc = Document(docx_path)

    text = "\n".join([para.text for para in doc.paragraphs])

    return text