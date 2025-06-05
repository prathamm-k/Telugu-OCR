# Telugu OCR Web Application 🔍

[![Python](https://img.shields.io/badge/python-v3.12-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.x-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful and user-friendly Optical Character Recognition (OCR) web application built with Streamlit, specifically designed for Telugu text extraction from PDFs and images. This application makes it easy to digitize Telugu documents while maintaining high accuracy and providing a seamless user experience.

## 🌟 Key Features

- 📝 Extract text from PDF files and images
- 📄 Support for multi-page PDF documents
- 🖼️ Image preprocessing for better OCR accuracy
- 📊 Real-time processing status and progress tracking
- 📈 Display statistics (page count, characters, words)
- 💾 Download extracted text as a file
- 🎨 Clean and intuitive user interface

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.12 or higher
- Poppler (required for PDF processing)
  - Ubuntu/Debian: `sudo apt-get install poppler-utils`
  - macOS: `brew install poppler`
  - Windows: Download from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/prathamm-k/Telugu-OCR.git
   cd Telugu-OCR
   ```

2. Choose your setup method:

### Automatic Setup (Recommended)

#### For Linux/macOS:
```bash
chmod +x setup.sh
./setup.sh
```

#### For Windows:
```bash
setup.bat
```

### Manual Setup

1. Create a virtual environment:
```bash
python -m venv ocr_env
source ocr_env/bin/activate  # On Linux/Mac
# or
.\ocr_env\Scripts\activate  # On Windows
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Start the Streamlit application:
```bash
streamlit run streamlit_app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Upload a PDF file or image containing Telugu text

4. Wait for the OCR process to complete

5. View the extracted text and download it as a text file

## 📁 Project Structure

```
.
├── sample/
│   └──test.pdf         # test pdf
├── OCR.py              # Core OCR functionality
├── streamlit_app.py    # Streamlit web interface
├── requirements.txt    # Project dependencies
├── setup.bat          #project setup script for windows
├── setup.sh           #project setup script for Ubuntu/Debian (Linux)
└── README.md          # Project documentation
```

## 🔧 Technologies Used

- Python
- Streamlit
- pdf2image
- PIL (Python Imaging Library)
- OCR Engine
- Other supporting libraries

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📈 Future Improvements

- Add support for more Indian languages
- Implement batch processing
- Enhance text accuracy with advanced preprocessing
- Add text post-processing options
- Support for more input formats
- Integration with cloud storage services
- API endpoint for programmatic access
- Docker containerization

## ⭐ Show your support

Give a ⭐️ if this project helped you! It means a lot.

## 📩 Contact

For any queries or suggestions, feel free to reach out:

Email: kairamkondapratham@gmail.com

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
