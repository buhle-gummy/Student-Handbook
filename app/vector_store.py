import chromadb
from pathlib import Path
from embeddings import generate_embeddings


# Create a permanent database location
DB_PATH = Path(__file__).parent.parent / "chroma_db"

# Connect to ChromaDB
client = chromadb.PersistentClient(path=str(DB_PATH))

# Create or access our collection
collection = client.get_or_create_collection(
    name="student_handbook"
)


def store_handbook():
    """Generate and store handbook embeddings in ChromaDB."""

    print("Preparing handbook data...")

    chunks, embeddings = generate_embeddings()

    print("Storing embeddings in ChromaDB...")

    collection.upsert(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        documents=[chunk["text"] for chunk in chunks],
        embeddings=embeddings.tolist(),
        metadatas=[
            {"page": chunk["page"]}
            for chunk in chunks
        ]
    )

    print(f"Successfully stored {len(chunks)} chunks!")

    print(f"Database location: {DB_PATH}")


if __name__ == "__main__":
    store_handbook()