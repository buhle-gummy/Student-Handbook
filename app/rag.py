import chromadb
from pathlib import Path
from sentence_transformers import SentenceTransformer


# Connect to the saved ChromaDB database
DB_PATH = Path(__file__).parent.parent / "chroma_db"

client = chromadb.PersistentClient(path=str(DB_PATH))

collection = client.get_collection(
    name="student_handbook"
)

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_handbook_context(question):
    """Find the most relevant handbook sections for a question."""

    question_embedding = model.encode([question]).tolist()

    results = collection.query(
        query_embeddings=question_embedding,
        n_results=3
    )

    retrieved_chunks = []

    for text, metadata in zip(
        results["documents"][0],
        results["metadatas"][0]
    ):
        retrieved_chunks.append({
            "page": metadata["page"],
            "text": text
        })

    return retrieved_chunks


if __name__ == "__main__":

    question = input("Ask a question about the handbook: ")

    results = retrieve_handbook_context(question)

    print("\nRelevant handbook information:\n")

    for result in results:
        print(f"Page {result['page']}")
        print(result["text"])
        print("-" * 50)