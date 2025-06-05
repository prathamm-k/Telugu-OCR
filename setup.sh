#!/bin/bash

echo "Setting up Telugu OCR Application..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3.12 or higher."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "pip is not installed. Please install pip."
    exit 1
fi

# Check if poppler-utils is installed
if ! command -v pdftoppm &> /dev/null; then
    echo "poppler-utils is not installed. Installing..."
    if [ -f /etc/debian_version ]; then
        sudo apt-get update
        sudo apt-get install -y poppler-utils
    elif [ -f /etc/redhat-release ]; then
        sudo yum install -y poppler-utils
    elif command -v brew &> /dev/null; then
        brew install poppler
    else
        echo "Could not install poppler-utils automatically. Please install manually."
        exit 1
    fi
fi

# Check if tesseract is installed
if ! command -v tesseract &> /dev/null; then
    echo "tesseract-ocr is not installed. Installing..."
    if [ -f /etc/debian_version ]; then
        sudo apt-get update
        sudo apt-get install -y tesseract-ocr tesseract-ocr-tel
    elif [ -f /etc/redhat-release ]; then
        sudo yum install -y tesseract tesseract-langpack-tel
    elif command -v brew &> /dev/null; then
        brew install tesseract tesseract-lang
        echo "Please make sure to install Telugu language data manually"
    else
        echo "Could not install tesseract automatically. Please install manually."
        exit 1
    fi
fi

# Create virtual environment if it doesn't exist
if [ ! -d "ocr_env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv ocr_env
fi

# Activate virtual environment
echo "Activating virtual environment..."
source ocr_env/bin/activate

# Install requirements
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Setup completed successfully!"
echo "To start the application, run: source ocr_env/bin/activate && streamlit run OCR/streamlit_app.py"
