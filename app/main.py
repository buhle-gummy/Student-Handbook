from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.rag import retrieve_handbook_context
from app.llm import generate_answer

app = FastAPI(
    title="Student Handbook AI Assistant",
    description="An AI assistant that answers questions using the Zaio Student Handbook.",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Welcome to the Student Handbook AI Assistant!"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    question = request.question.strip()

    if not question:
        return {
            "answer": "Please enter a question.",
            "source": None
        }

    try:
        results = retrieve_handbook_context(question)

        if not results:
            return {
                "answer": "I don't know. The handbook does not provide this information.",
                "source": None
            }

        context = "\n\n".join(
            f"Page {item['page']}: {item['text']}"
            for item in results
        )

        answer = generate_answer(question, context)
        answer_lower = answer.lower()

        unknown_phrases = [
            "i don't know",
            "no information provided",
            "not provided in the context",
            "not available in the context",
            "not mentioned in the context",
            "does not contain information"
        ]

        if any(phrase in answer_lower for phrase in unknown_phrases):
            return {
                "answer": "I don't know. The handbook does not provide this information.",
                "source": None
            }

        sources = sorted(set(item["page"] for item in results))

        return {
            "answer": answer,
            "source": ", ".join(
                f"Page {page}" for page in sources
            )
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )