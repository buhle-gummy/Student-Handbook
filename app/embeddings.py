from chunking import chunk_text
from ingest import extract_text_from_pdf
from sentence_transformers import SentenceTransformer


def generate_embeddings():
    """Generate numerical embeddings for handbook chunks."""

    print("Loading embedding model...")

    model = SentenceTransformer("all-MiniLM-L6-v2")

    pages = extract_text_from_pdf()
    chunks = chunk_text(pages)

    texts = [chunk["text"] for chunk in chunks]

    print("Generating embeddings...")

    embeddings = model.encode(texts)

    print(f"\nSuccessfully generated {len(embeddings)} embeddings.")

    print(f"Embedding dimensions: {embeddings.shape[1]}")

    return chunks, embeddings


if __name__ == "__main__":
    generate_embeddings()