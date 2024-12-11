#from pdf2image import convert_from_path
import os
import fitz # PyMuPDF
pdf_directory = 'ocr_pdf_input/book.pdf'
output_dir = 'ocr_input_img'

# Open the PDF file
pdf_document = fitz.open(pdf_directory)

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate through the pages and save as images
for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    pix = page.get_pixmap()
    image_path = os.path.join(output_dir, f'page_{page_num + 1}.png')
    pix.save(image_path)
