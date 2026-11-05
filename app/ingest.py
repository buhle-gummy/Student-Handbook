from pypdf import PdfReader
from pathlib import Path

PDF_PATH = Path(__file__).parent.parent / "handbook" / "handbook.pdf"


def extract_text_from_pdf():
    """Extract text from every page of the handbook."""

    if not PDF_PATH.exists():
        raise FileNotFoundError(f"PDF not found: {PDF_PATH}")

    reader = PdfReader(str(PDF_PATH))
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text and text.strip():
            pages.append({
                "page": page_number,
                "text": text.strip()
            })

    return pages


if __name__ == "__main__":
    extracted_pages = extract_text_from_pdf()

    print(f"Successfully extracted {len(extracted_pages)} pages.")

    for page in extracted_pages[:3]:
        print(f"\n--- Page {page['page']} ---")
        print(page["text"][:500])