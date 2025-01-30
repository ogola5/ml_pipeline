import os
import PyPDF2
from docx import Document
import pandas as pd
from datetime import datetime

def pdf_to_text(pdf_path):
    """Extract text from PDF files."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = " ".join([page.extract_text() for page in reader.pages])
    return text

def docx_to_text(docx_path):
    """Extract text from Word files."""
    doc = Document(docx_path)
    return " ".join([para.text for para in doc.paragraphs])

def process_raw_data(raw_dir="data/raw", processed_dir="data/processed"):
    """Convert all PDF/Word files in `raw_dir` to a structured CSV."""
    data = []
    
    for filename in os.listdir(raw_dir):
        file_path = os.path.join(raw_dir, filename)
        if filename.endswith(".pdf"):
            content = pdf_to_text(file_path)
            doc_type = "pdf"
        elif filename.endswith(".docx"):
            content = docx_to_text(file_path)
            doc_type = "docx"
        else:
            continue  # Skip non-PDF/DOCX files
        
        # Extract metadata (customize based on your filenames/needs)
        metadata = {
            "doc_id": filename.split(".")[0],
            "doc_type": doc_type,
            "content": content,
            "grade": filename.split("_")[0],  # Example: "Grade9_math_syllabus.pdf"
            "subject": filename.split("_")[1],
            "upload_date": datetime.now().strftime("%Y-%m-%d")
        }
        data.append(metadata)
    
    # Save to CSV
    df = pd.DataFrame(data)
    df.to_csv(f"{processed_dir}/processed_content.csv", index=False)
    print(f"Processed {len(df)} files. Saved to {processed_dir}/processed_content.csv")

if __name__ == "__main__":
    process_raw_data()