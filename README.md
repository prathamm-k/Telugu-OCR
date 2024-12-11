# Telugu OCR for High-Accuracy Dataset Creation

This repository contains a robust OCR (Optical Character Recognition) solution tailored for converting large PDF collections, particularly books with images, into structured datasets. The project focuses on the Telugu language, achieving an impressive 91% text recognition accuracy, surpassing other Telugu OCR tools currently available.

## Features

- **High Accuracy**: Achieves 91% text accuracy for Telugu text, significantly improving on existing solutions.
- **PDF to Dataset Conversion**: Processes large PDF files, including books with embedded images, to generate structured datasets.
- **Image Preprocessing**: Uses advanced techniques like resizing, grayscale conversion, shadow removal, and thresholding for enhanced OCR performance.
- **Automated Multi-Image Handling**: Streamlines the process for handling and processing multiple image files efficiently.
- **Custom OCR Workflow**: Integrates OpenCV for preprocessing and Tesseract for text recognition.

## Impact

This project offers a groundbreaking solution for digitizing Telugu content, making it invaluable for researchers, developers, and institutions focusing on preserving and utilizing Telugu literature and historical texts. It bridges the gap between low-resource language processing and modern dataset requirements.

## Requirements

- Python 3.8+
- Libraries: 
  - OpenCV
  - Tesseract OCR
  - NumPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/telugu-ocr-dataset.git
   cd telugu-ocr-dataset
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR and add it to your system's PATH. For instructions, see [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract).

## Usage

1. Place your PDF files in the `input` directory.
2. Run the preprocessing and OCR pipeline:
   ```bash
   python process_pdfs.py
   ```
3. Extracted datasets will be saved in the `output` directory.

## Project Structure

```
├── input/             # Directory for input PDFs or images
├── output/            # Directory for processed datasets
├── src/               # Source code for the OCR pipeline
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## Future Enhancements

- **Language Expansion**: Adapt the OCR pipeline for other low-resource languages.
- **Model Training**: Integrate custom models to improve accuracy further.
- **GUI/Cloud Deployment**: Provide a user-friendly interface and deploy the solution on cloud platforms.

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or collaboration opportunities, please reach out:
- **Name**: Pratham Kairamkonda
- **Email**: kairamkondapratham@gmail.com
- **LinkedIn**: [linkedin.com/in/pratham-kairamkonda-616442287](https://linkedin.com/in/pratham-kairamkonda-616442287)
