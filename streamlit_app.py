import streamlit as st
import os
import tempfile
import subprocess
import base64
from OCR import preprocess_image, perform_ocr
from pdf2image import convert_from_path

# Set wide mode and configure the page
st.set_page_config(
    page_title="Telugu OCR",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add custom CSS for better styling
st.markdown("""
<style>
/* Main app styling */
.main {
    padding: 1rem;
}

/* Progress bar styling */
.stProgress > div > div > div > div {
    background-color: #3b82f6;
}

/* Success message styling */
div.element-container div.stSuccess {
    background-color: #dcfce7;
    color: #166534;
    border: 1px solid #22c55e;
    border-radius: 0.375rem;
    padding: 0.5rem 1rem;
}

/* Error message styling */
div.element-container div.stError {
    background-color: #fef2f2;
    color: #991b1b;
    border: 1px solid #f87171;
    border-radius: 0.375rem;
    padding: 0.5rem 1rem;
}

/* Remove default backgrounds */
div.stSuccess, div.stError {
    background-color: transparent !important;
}

/* Main title styling */
.main-title {
    color: #1e293b;
    font-size: 2.5rem !important;
    margin-bottom: 0.5rem !important;
    text-align: center;
    padding: 1rem;
}

/* Subtitle styling */
.subtitle {
    color: #475569;
    text-align: center;
    margin-bottom: 1rem;
}

/* Custom card styling */
.stCard {
    padding: 1rem;
    border-radius: 0.5rem;
    border: 1px solid #e2e8f0;
    background-color: white;
    margin-bottom: 1rem;
}

/* Status section */
.status-section {
    margin: 1rem 0;
    padding: 0.5rem;
    background-color: #f8fafc;
    border-radius: 0.375rem;
}

/* PDF preview container */
.pdf-preview {
    border: 1px solid #e2e8f0;
    border-radius: 0.5rem;
    height: 750px;
    overflow: hidden;
    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
}

.pdf-preview iframe {
    width: 100%;
    height: 100%;
    border: none;
}

/* Button styling */
.stButton button {
    width: 100%;
    background-color: #3b82f6 !important;
    color: white !important;
    border-radius: 0.375rem !important;
    padding: 0.5rem 1rem !important;
    border: none !important;
    box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05) !important;
    height: 45px !important;
    margin-top: 1px !important;
}

.stButton button:hover {
    background-color: #2563eb !important;
}

/* File uploader styling */
div.stUploader > div {
    height: 42px !important;
    padding: 0 !important;
    margin-bottom: 0 !important;
}
.stUploader {
    border: 2px dashed #e2e8f0;
    border-radius: 0.5rem;
    padding: 1rem;
    margin-bottom: 1rem;
}

/* Text area styling */
.stTextArea textarea {
    border-radius: 0.375rem;
    border-color: #e2e8f0;
    height: 750px !important;
}

/* Info box styling */
.stInfo {
    background-color: #f0f9ff;
    color: #000000;
    padding: 1rem;
    border-radius: 0.375rem;
    margin: 0.5rem 0;
    border: 1px solid ;
}

/* Section headers */
h3 {
    margin: 1rem 0 !important;
    color: #000000 !important;
}

/* Stats section */
.stats-section {
    background-color: #f8fafc;
    padding: 1rem;
    border-radius: 0.375rem;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="main-title">Telugu OCR Application</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Extract text from Telugu PDF documents with ease</p>', unsafe_allow_html=True)

# System Check Section
with st.container():
    #st.markdown('<div class="stCard">', unsafe_allow_html=True)
    try:
        subprocess.run(['pdftoppm', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        poppler_installed = True
        st.success("✅ System Check Passed - Ready to process PDFs")
    except FileNotFoundError:
        poppler_installed = False
        st.error("""
        ❌ Poppler is not installed. Please install it first:

        • Ubuntu/Debian: `sudo apt-get install poppler-utils`
        • macOS: `brew install poppler`
        • Windows: [Download Poppler](http://blog.alivate.com.au/poppler-windows/)
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# File Upload Section
if poppler_installed:
    upload_col, button_col = st.columns([5, 2])
    with upload_col:
        uploaded_file = st.file_uploader("Upload a Telugu PDF file", type="pdf", label_visibility="collapsed")

    with button_col:
        sample_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sample", "test.pdf")
        if os.path.exists(sample_path):
            if st.button("Try Sample PDF", use_container_width=True):
                with open(sample_path, 'rb') as f:
                    bytes_data = f.read()
                class SampleFile:
                    def __init__(self, content, name):
                        self.content = content
                        self.name = name
                    def getvalue(self):
                        return self.content
                uploaded_file = SampleFile(bytes_data, "test.pdf")

    # Main content section
    if uploaded_file is not None:
        # Status indicators before columns
        status_text = st.empty()
        progress_bar = st.progress(0)

        # Content columns for PDF preview and output
        preview_col, output_col = st.columns(2)

        # PDF Preview
        with preview_col:
            st.markdown("#### PDF Preview")
            if isinstance(uploaded_file, SampleFile):
                with open(sample_path, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            else:
                base64_pdf = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')

            pdf_display = f'''
                <div class="pdf-preview">
                    <iframe src="data:application/pdf;base64,{base64_pdf}" type="application/pdf"></iframe>
                </div>
            '''
            st.markdown(pdf_display, unsafe_allow_html=True)

        # Process and show output
        with output_col:
            st.markdown("#### Extracted Text")

            # Create temporary file for the PDF
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                pdf_path = tmp_file.name

            try:
                # Convert PDF to images
                with st.spinner('Converting PDF to images...'):
                    images = convert_from_path(pdf_path)
                    total_pages = len(images)
                    #st.info(f"Found {total_pages} pages in the PDF")

                # Process and show output
                with output_col:
                    #st.markdown("#### Extracted Text")

                    # Create temporary directory for processing
                    with tempfile.TemporaryDirectory() as temp_dir:
                        # Process each page
                        all_text = []
                        for i, image in enumerate(images):
                            # Update status
                            status_text.text(f"Processing page {i+1} of {total_pages}")
                            progress_bar.progress((i + 1) / total_pages)

                            # Save image temporarily
                            image_path = os.path.join(temp_dir, f'page_{i+1}.png')
                            image.save(image_path, 'PNG')

                            # Preprocess and perform OCR
                            processed_img = preprocess_image(image_path)
                            ocr_text = perform_ocr(processed_img)

                            # Add page marker and text
                            all_text.append(f"\n--- Page {i+1} ---\n")
                            all_text.append(ocr_text)
                            all_text.append("\n")

                        # Combine all text
                        final_text = "".join(all_text)

                        # Show completion message
                        status_text.text("✅ OCR completed successfully!")

                        # Display text area with extracted text
                        st.text_area("", final_text, label_visibility="collapsed")

                        # Download and stats section
                        #st.markdown('<div class="stats-section">', unsafe_allow_html=True)
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Pages", total_pages)
                        with col2:
                            st.metric("Characters", len(final_text))
                        with col3:
                            st.metric("Words", len(final_text.split()))

                        st.download_button(
                            label="📥 Download Text File",
                            data=final_text,
                            file_name=f"{uploaded_file.name.rsplit('.', 1)[0]}_ocr.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                        st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")

            finally:
                # Clean up the temporary PDF file
                try:
                    os.unlink(pdf_path)
                except Exception as e:
                    st.warning(f"⚠️ Could not delete temporary file: {str(e)}")

# Help Section moved to sidebar
with st.sidebar:
    st.markdown("#### ℹ️ Instructions & Tips")
    st.markdown("""
    #### How to Use
    1. **System Check**: Ensure Poppler is installed
    2. **Upload**: Choose a Telugu PDF or try the sample
    3. **Process**: Wait for OCR completion
    4. **Review**: Check the extracted text
    5. **Download**: Save the results

    #### Tips for Best Results
    • Use clearly scanned PDFs
    • Large documents may take longer
    • OCR quality depends on PDF quality
    """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #64748b; padding: 0.5rem;'>
    Made by Pratham Kairamkonda | OCR Technology for Telugu Documents
    </div>
    """,
    unsafe_allow_html=True
)
