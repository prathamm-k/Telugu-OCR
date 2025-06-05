from PIL import Image
import numpy as np
import subprocess
import tempfile
import os

def preprocess_image(img_path):
    # Read image using PIL
    img = Image.open(img_path).convert('L')  # Convert to grayscale

    # Convert to numpy array
    img_array = np.array(img)

    # Resize with PIL
    width, height = img.size
    img = img.resize((int(width * 1.5), int(height * 1.5)), Image.Resampling.LANCZOS)

    # Convert back to numpy array
    img_array = np.array(img)

    # Apply threshold
    threshold = np.mean(img_array)
    img_array = np.where(img_array > threshold, 255, 0).astype(np.uint8)

    return Image.fromarray(img_array)

def perform_ocr(img):
    # Save the image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
        if isinstance(img, Image.Image):
            img.save(tmp.name)
        else:
            Image.fromarray(img).save(tmp.name)

        # Call tesseract directly
        try:
            result = subprocess.run(
                ['tesseract', tmp.name, 'stdout', '-l', 'tel'],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        finally:
            # Clean up
            os.unlink(tmp.name)