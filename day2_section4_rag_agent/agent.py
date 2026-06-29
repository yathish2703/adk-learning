"""
Day 2 - Section 4: RAG Agent (Local Document Retrieval)
Demonstrates Retrieval-Augmented Generation using local document embeddings.
This version uses local tools instead of Google Cloud services.
"""
from google.adk.agents import Agent
import os
import json
from pathlib import Path

# Try to use authenticated LLM, fall back to Gemini if not available
try:
    from lilly_tools.llm_config import create_llm_model_with_auth
    LLM_AUTHENTICATED = True
except ImportError:
    LLM_AUTHENTICATED = False

if LLM_AUTHENTICATED:
    try:
        _model = create_llm_model_with_auth(model_name="anthropic/claude-sonnet-4.6")
    except Exception:
        _model = "anthropic/claude-sonnet-4.6"
else:
    _model = "gemini-2.0-flash"


# In-memory document store (simulating a vector database)
DOCUMENT_STORE = {}
DOCUMENTS_DIR = Path(__file__).parent / "sample_documents"


def load_documents_to_store():
    """Load sample documents into memory on startup."""
    global DOCUMENT_STORE
    if DOCUMENTS_DIR.exists():
        for doc_file in DOCUMENTS_DIR.glob("*.txt"):
            with open(doc_file, 'r') as f:
                DOCUMENT_STORE[doc_file.stem] = {
                    "content": f.read(),
                    "filename": doc_file.name
                }


def retrieve_documents(query: str, top_k: int = 3) -> dict:
    """Retrieves relevant documents based on the query.

    This is a simplified version that does keyword matching instead of
    semantic search. In a real RAG system, you would use embeddings
    and vector similarity.

    Args:
        query: The search query
        top_k: Number of top documents to return (default: 3)

    Returns:
        A dictionary with retrieved documents and their relevance
    """
    if not DOCUMENT_STORE:
        load_documents_to_store()

    # Simple keyword matching (in production, use embeddings + cosine similarity)
    query_lower = query.lower()
    results = []

    for doc_id, doc_data in DOCUMENT_STORE.items():
        content_lower = doc_data["content"].lower()
        # Count keyword matches (simple scoring)
        score = sum(1 for word in query_lower.split() if word in content_lower)

        if score > 0:
            results.append({
                "doc_id": doc_id,
                "filename": doc_data["filename"],
                "content": doc_data["content"],
                "score": score
            })

    # Sort by score and take top_k
    results.sort(key=lambda x: x["score"], reverse=True)
    top_results = results[:top_k]

    return {
        "query": query,
        "num_results": len(top_results),
        "documents": [
            {
                "filename": r["filename"],
                "content": r["content"][:500],  # Truncate for context
                "relevance_score": r["score"]
            }
            for r in top_results
        ]
    }


def list_available_documents() -> dict:
    """Lists all documents available in the knowledge base.

    Returns:
        A dictionary with the list of available documents
    """
    if not DOCUMENT_STORE:
        load_documents_to_store()

    return {
        "total_documents": len(DOCUMENT_STORE),
        "documents": [
            {"id": doc_id, "filename": data["filename"]}
            for doc_id, data in DOCUMENT_STORE.items()
        ]
    }


# Initialize document store
load_documents_to_store()


root_agent = Agent(
    name="docs_assistant",
    model=_model,
    description="A document Q&A assistant that answers questions from a knowledge base",
    instruction=(
        "You are a helpful assistant that answers questions based on retrieved documents. "
        "\n\n"
        "IMPORTANT RULES:\n"
        "1. Use the retrieve_documents tool to find relevant information\n"
        "2. Answer ONLY based on the retrieved document content\n"
        "3. If the information is not in the documents, say 'I don't have that information in my knowledge base'\n"
        "4. Cite which document you're using when answering\n"
        "5. If asked what documents are available, use list_available_documents\n"
        "\n"
        "This demonstrates RAG (Retrieval-Augmented Generation) - you retrieve relevant "
        "passages first, then generate answers grounded in those sources."
    ),
    tools=[retrieve_documents, list_available_documents],
)
