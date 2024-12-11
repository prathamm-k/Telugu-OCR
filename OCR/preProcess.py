
import numpy as np
import cv2
import os
import pytesseract
import shutil
import temp


input_img = r'ocr_input_img'
output_text_file = r'output_path'

if not os.path.exists(output_text_file):
    os.makedirs(output_text_file)

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

    # Process multiple images
files = os.listdir(input_img)
file_count = len(files) + 1

for i in range(1, file_count):
        img_path = os.path.join(input_img, temp.pdf_name+f'_page_{i}.png')

        if os.path.exists(img_path):
            try:
                processed_img = preprocess_image(img_path)
                ocr_text = perform_ocr(processed_img)
                output_file_path = os.path.join(output_text_file, f'page_{i}.txt')
                with open(output_file_path, 'w', encoding='utf-8') as text_file:
                    text_file.write(ocr_text)
            except Exception as e:
                print(f'An error occurred with {img_path}: {e}')
        else:
            print(f'File not found: {img_path}')

    #delete preprocessed images
'''folder = 'ocr_input_img'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))'''