import os
import re

output_path = r'Merged'
input_path = r'output_path'
pdf_file_path = r'input_pdf\book.pdf'
base_name = os.path.splitext(os.path.basename(pdf_file_path))[0]
merged_file_name = base_name+".txt"
merged_file_path = os.path.join(output_path, merged_file_name)

def extract_page_number(file_name):
    match = re.search(r'page_(\d+)', file_name)
    return int(match.group(1)) if match else float('inf')

try:
    # Merge all text files into one in the correct order
    with open(merged_file_path, 'w', encoding='utf-8') as merged_file:
        text_files = [f for f in os.listdir(input_path) if f.endswith('.txt')]
        if not text_files:
            raise FileNotFoundError("No text files found in the specified directory.")

        for file_name in sorted(text_files, key=extract_page_number):
            page_number = extract_page_number(file_name)
            file_path = os.path.join(input_path, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    merged_file.write('\n')
                    merged_file.write(content)
                    merged_file.write(f"\n--- Page {page_number} ---\n")
                    merged_file.write('\n')
            except Exception as e:
                print(f"Error reading {file_name}: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
