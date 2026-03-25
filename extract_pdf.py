import sys

try:
    import pypdf
    pdf_path = r'c:\Users\Darsh\Downloads\task.pdf'
    with open(pdf_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        print(f"Total pages: {len(reader.pages)}\n")
        for i, page in enumerate(reader.pages[:3]):  # First 3 pages
            print(f'=== Page {i+1} ===')
            text = page.extract_text()
            print(text if text else "No text found on this page")
            print("\n")
except ImportError:
    print("pypdf not available, trying pdfplumber...")
    try:
        import pdfplumber
        pdf_path = r'c:\Users\Darsh\Downloads\task.pdf'
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Total pages: {len(pdf.pages)}\n")
            for i, page in enumerate(pdf.pages[:3]):
                print(f'=== Page {i+1} ===')
                text = page.extract_text()
                print(text if text else "No text found on this page")
                print("\n")
    except ImportError:
        print("Neither pypdf nor pdfplumber available")
        sys.exit(1)
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
