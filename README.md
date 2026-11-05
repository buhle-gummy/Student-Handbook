# Student Handbook AI Assistant

## Project Overview

The Student Handbook AI Assistant is an AI-powered question-answering application that helps students find information from the Zaio Student Handbook.

Students can ask questions in natural language and receive relevant answers based on the handbook. The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information before generating answers.

## Features

- PDF text extraction.
- Text chunking.
- Text embeddings using Sentence Transformers.
- Vector storage using ChromaDB.
- Semantic search and information retrieval.
- AI-generated answers using a locally hosted Llama model.
- FastAPI REST API.
- Source page references.
- Fallback responses when information is unavailable.

## Technologies Used

- Python
- FastAPI
- Sentence Transformers
- ChromaDB
- Ollama
- Llama 3.2 (1B)
- PyPDF

## Project Structure

```text
Student Handbook/
│
├── app/
│   ├── ingest.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── rag.py
│   ├── llm.py
│   └── main.py
│
├── handbook/
│   └── handbook.pdf
│
├── chroma_db/
├── tests/
├── venv/
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd "Student Handbook"
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Download and install Ollama for Windows.

Download the Llama model:

```bash
ollama run llama3.2:1b
```

Keep Ollama available while using the application.

### 6. Start the API

```bash
python -m uvicorn app.main:app --reload
```

## API Usage

### Endpoint

`POST /ask`

### Request

```json
{
  "question": "What are the live class times?"
}
```

### Response

```json
{
  "answer": "According to the handbook, the live class times are ...",
  "source": "Page 7, Page 11, Page 12"
}
```

If the handbook does not contain the requested information, the assistant returns:

```json
{
  "answer": "I don't know. The handbook does not provide this information.",
  "source": null
}
```

## API Documentation

After starting the server, open:

`http://127.0.0.1:8000/docs`

## How It Works

1. The handbook PDF is loaded and its text is extracted.
2. The extracted text is divided into smaller chunks.
3. Sentence Transformers converts the chunks into embeddings.
4. ChromaDB stores the embeddings and corresponding text.
5. A student's question is converted into an embedding.
6. Relevant handbook chunks are retrieved.
7. Ollama uses the Llama model to generate an answer based on the retrieved context.
8. FastAPI returns the answer and its source pages.

## Project Status

Core functionality implemented and tested locally.