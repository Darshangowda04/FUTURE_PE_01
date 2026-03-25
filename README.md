# Future PE 1 - PDF Extractor (Basic)

A Python script for extracting text from PDF files with fallback support for multiple PDF libraries.

## Features
- Extracts text from the first 3 pages of a PDF
- Fallback support: tries pypdf first, then pdfplumber
- Error handling for missing libraries

## Requirements
- Python 3.x
- pypdf or pdfplumber

## Usage
```bash
python extract_pdf.py
```

## Notes
Update the `pdf_path` variable to point to your PDF file.
