from ingest import extract_text_from_pdf


def chunk_text(pages, chunk_size=1000, overlap=200):
    """Split handbook text into smaller chunks while keeping page numbers."""

    chunks = []

    for page in pages:
        text = page["text"]

        start = 0

        while start < len(text):
            end = start + chunk_size

            chunk = text[start:end].strip()

            if chunk:
                chunks.append({
                    "page": page["page"],
                    "text": chunk
                })

            start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    pages = extract_text_from_pdf()

    chunks = chunk_text(pages)

    print(f"Successfully created {len(chunks)} chunks.")

    for number, chunk in enumerate(chunks[:3], start=1):
        print(f"\n--- Chunk {number} | Page {chunk['page']} ---")
        print(chunk["text"])