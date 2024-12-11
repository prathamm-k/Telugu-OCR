import os
import re
import shutil
import cv2
import numpy as np
import pytesseract
#from pdf2image import convert_from_path

# Define directories
pdf_directory = 'ocr_pdf_input'
output_img_dir = 'ocr_img_input'
output_text_dir = 'ocr_text_output'
merged_text_dir = 'ocr_output_files'

# Ensure directories exist
os.makedirs(output_img_dir, exist_ok=True)
os.makedirs(output_text_dir, exist_ok=True)
os.makedirs(merged_text_dir, exist_ok=True)

def preprocess_image(img_path):
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Image not found or unable to read: {img_path}")

    # Rescale the image
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Remove shadows
    rgb_planes = cv2.split(img)
    result_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7, 7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        result_planes.append(diff_img)
    img = cv2.merge(result_planes)

    # Apply dilation and erosion to remove noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Apply Gaussian blur
    img = cv2.GaussianBlur(img, (1, 1), 0)

    # Apply threshold
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    return img

def perform_ocr(img):
    return pytesseract.image_to_string(img, lang="tel")

def extract_page_number(file_name):
    match = re.search(r'page_(\d+)', file_name)
    return int(match.group(1)) if match else float('inf')

# Process each PDF
for filename in os.listdir(pdf_directory):
    if filename.lower().endswith('.pdf'):
        # Convert PDF to images
        pdf_file_path = os.path.join(pdf_directory, filename)
        pdf_name = os.path.splitext(filename)[0]
        images = convert_from_path(pdf_file_path)

        # OCR each image
        for i, image in enumerate(images):
            image_path = os.path.join(output_img_dir, f'{pdf_name}_page_{i+1}.png')
            image.save(image_path, 'PNG')

            # Preprocess and perform OCR
            processed_img = preprocess_image(image_path)
            ocr_text = perform_ocr(processed_img)

            # Save OCR text to a file
            output_text_path = os.path.join(output_text_dir, f'{pdf_name}_page_{i+1}.txt')
            with open(output_text_path, 'w', encoding='utf-8') as text_file:
                text_file.write(ocr_text)

        # Merge all text files into one
        merged_file_name = f'{pdf_name}.txt'
        merged_file_path = os.path.join(merged_text_dir, merged_file_name)
        with open(merged_file_path, 'w', encoding='utf-8') as merged_file:
            text_files = [f for f in os.listdir(output_text_dir) if f.startswith(pdf_name) and f.endswith('.txt')]
            for text_file_name in sorted(text_files, key=extract_page_number):
                page_number = extract_page_number(text_file_name)
                text_file_path = os.path.join(output_text_dir, text_file_name)
                with open(text_file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    merged_file.write("\n")
                    merged_file.write(content)
                    merged_file.write(f"--- Page {page_number} ---\n")
                    merged_file.write("\n")

        # Clean up or delete images and text files
        for img_file in os.listdir(output_img_dir):
            if img_file.startswith(pdf_name):
                os.remove(os.path.join(output_img_dir, img_file))
        for txt_file in os.listdir(output_text_dir):
            if txt_file.startswith(pdf_name):
                os.remove(os.path.join(output_text_dir, txt_file))
