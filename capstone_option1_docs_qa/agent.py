"""
Capstone Option 1: Docs Q&A Agent
RAG over documents + google_search as a fallback for anything not in the corpus.
"""
from google.adk.agents import Agent
from google.adk.tools import google_search
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


# In-memory document store
DOCUMENT_STORE = {}
DOCUMENTS_DIR = Path(__file__).parent / "knowledge_base"


def load_documents_to_store():
    """Load documents into memory on startup."""
    global DOCUMENT_STORE
    if DOCUMENTS_DIR.exists():
        for doc_file in DOCUMENTS_DIR.glob("*.txt"):
            with open(doc_file, 'r') as f:
                DOCUMENT_STORE[doc_file.stem] = {
                    "content": f.read(),
                    "filename": doc_file.name
                }


def search_knowledge_base(query: str) -> dict:
    """Search the local knowledge base for relevant information.

    Args:
        query: The search query

    Returns:
        Relevant documents from the knowledge base
    """
    if not DOCUMENT_STORE:
        load_documents_to_store()

    query_lower = query.lower()
    results = []

    for doc_id, doc_data in DOCUMENT_STORE.items():
        content_lower = doc_data["content"].lower()
        score = sum(1 for word in query_lower.split() if word in content_lower)

        if score > 0:
            results.append({
                "filename": doc_data["filename"],
                "content": doc_data["content"],
                "score": score
            })

    results.sort(key=lambda x: x["score"], reverse=True)

    if results:
        return {
            "found_in_knowledge_base": True,
            "num_results": len(results),
            "top_result": results[0]["content"]
        }
    else:
        return {
            "found_in_knowledge_base": False,
            "message": "No relevant documents found in knowledge base"
        }


# Initialize
load_documents_to_store()


root_agent = Agent(
    name="hybrid_docs_assistant",
    model=_model,
    description="Answers questions from local docs with web search fallback",
    instruction=(
        "You are a helpful Q&A assistant with a two-tier knowledge strategy:\n\n"
        "1. FIRST PRIORITY: Use search_knowledge_base to check local documents\n"
        "2. FALLBACK: If not found in local docs, use google_search for current info\n\n"
        "RULES:\n"
        "- Always try the knowledge base first\n"
        "- Clearly indicate which source you're using (docs or web)\n"
        "- If using local docs, cite the filename\n"
        "- If using web search, mention it's external information\n"
        "- Combine both sources when appropriate\n\n"
        "This hybrid approach gives you the best of both worlds: "
        "trusted internal knowledge + up-to-date external information."
    ),
    tools=[search_knowledge_base, google_search],
)
