@echo off
echo Setting up Telugu OCR Application...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python 3.12 or higher.
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip is not installed. Please install pip.
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "ocr_env" (
    echo Creating virtual environment...
    python -m venv ocr_env
)

REM Activate virtual environment
echo Activating virtual environment...
call ocr_env\Scripts\activate.bat

REM Install requirements
echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Setup completed successfully!
echo NOTE: Please ensure you have the following dependencies installed and added to your PATH:
echo 1. Poppler: Download from http://blog.alivate.com.au/poppler-windows/
echo 2. Tesseract: Download from https://github.com/UB-Mannheim/tesseract/wiki
echo Also ensure you have installed the Telugu language data for Tesseract
echo.
echo To start the application:
echo 1. Run: ocr_env\Scripts\activate.bat
echo 2. Run: streamlit run OCR\streamlit_app.py
pause
