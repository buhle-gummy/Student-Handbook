import ollama


def generate_answer(question, context):
    """Generate an answer using the local Llama model."""

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful Zaio Student Handbook AI Assistant. "
                    "Answer questions using ONLY the information provided "
                    "in the handbook context. Do not invent information. "
                    "If the answer is not explicitly stated in the provided context, "
            "respond exactly:"" I don't know. The handbook does not provide this information. "
                    "Keep answers clear, friendly and concise."
                    "If the answer is not explicitly stated in the provided context, "

                )
            },
            {
                "role": "user",
                "content": (
                    f"Handbook context:\n{context}\n\n"
                    f"Student question:\n{question}"
                )
            }
        ],
        options={
            "temperature": 0.2
        }
    )

    return response.message.content.strip()