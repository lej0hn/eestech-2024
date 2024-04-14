import fitz  # PyMuPDF
from pdfminer.high_level import extract_text

# def extract_text_from_pdf(pdf_path):
#     text = ""
#     with fitz.open(pdf_path) as pdf:
#         for page_number in range(0, 50):  # Adjust to 0-based indexing
#             page = pdf.load_page(page_number)
#             text += page.get_text()
#     return text

def extract_text_from_pdf(pdf_path, start_page=None, end_page=None):
    if start_page is None:
        start_page = 1
    if end_page is None:
        end_page = -1  # Extract until the last page
    
    text = extract_text(pdf_path, page_numbers=range(start_page, end_page + 1))
    return text

def extract_text_from_pdf_all(pdf_path):
    
    text = extract_text(pdf_path)
    return text

def save_text_to_file(text, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

# Example usage
pdf_path = "C:/Users/jdara/Downloads/RealChef-obooko-fd0013.pdf"
# extracted_text = extract_text_from_pdf(pdf_path, 20, 30)\
extracted_text = extract_text_from_pdf_all(pdf_path)
output_file = "RealChef_obooko.txt"
save_text_to_file(extracted_text, output_file)