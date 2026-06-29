# Day 2 - Section 4: RAG Agent (Local Document Retrieval)

## What You'll Learn
- What RAG (Retrieval-Augmented Generation) is
- The 6-step RAG pipeline: ingest → chunk → embed → index → retrieve → generate
- How to ground AI responses in your own documents
- The difference between RAG and memory

## RAG in Simple Terms

**RAG = Retrieval-Augmented Generation**

Instead of the model making things up, it:
1. **Retrieves** relevant passages from your documents
2. **Reads** those passages
3. **Generates** answers grounded in what it just read

```
User Question → Retrieve Docs → Put in Prompt → LLM Answer
```

## The Six Steps

```
1. Ingestion    → Load your files (PDF, TXT, etc.)
2. Chunking     → Split into small passages
3. Embedding    → Turn text into vectors (numbers)
4. Indexing     → Store vectors in a searchable database
5. Retrieval    → Find most similar chunks to the query
6. Generation   → LLM answers using retrieved chunks
```

## Local vs Cloud RAG

This example uses **local retrieval** (simplified):
- Simple keyword matching instead of semantic embeddings
- In-memory document store instead of vector database
- No Google Cloud dependencies

**Production RAG** would use:
- Semantic embeddings (e.g., sentence-transformers)
- Vector databases (ChromaDB, FAISS, Pinecone)
- Proper chunking strategies

## How to Run
```bash
adk web day2_section4_rag_agent
```

## Try It

### Questions it CAN answer (from the documents):
- "What is Python used for?"
- "What are the types of machine learning?"
- "What is an AI agent?"
- "List available documents"

### Questions it SHOULD NOT answer (not in documents):
- "What is JavaScript?" (should say "I don't have that information")
- "What's the weather today?"

Watch how it:
1. Calls `retrieve_documents` with your question
2. Gets relevant document chunks
3. Answers ONLY from those chunks

## Key Concepts

### Why RAG?
- ✅ Grounded in real sources (not hallucinated)
- ✅ Updated by changing documents (not retraining)
- ✅ Cites sources for transparency
- ❌ Limited to what's in the documents

### RAG vs Memory
- **Session State**: Temporary (this conversation only)
- **Memory**: Long-term facts across conversations
- **RAG**: Answering from your document library

They solve different problems!

## Making it Production-Ready

To upgrade this to real RAG:
1. **Use embeddings**: Install `sentence-transformers` for semantic search
2. **Add a vector DB**: Use ChromaDB or FAAS for scalable storage
3. **Better chunking**: Use `langchain` text splitters (recursive, semantic)
4. **Add metadata**: Store source, page numbers for citations
5. **Tune retrieval**: Adjust `top_k` and similarity thresholds

## Sample Code for Production RAG

```python
# Install: pip install chromadb sentence-transformers

from chromadb import Client
from sentence_transformers import SentenceTransformer

# Create embeddings model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create vector database
client = Client()
collection = client.create_collection("docs")

# Add documents with embeddings
collection.add(
    documents=[chunk1, chunk2, chunk3],
    embeddings=model.encode([chunk1, chunk2, chunk3]),
    ids=["id1", "id2", "id3"]
)

# Query
query_embedding = model.encode(query)
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)
```

## Common Pitfalls
- **Bad chunks**: Lost context from splitting mid-sentence
- **Wrong threshold**: Too strict = no results, too loose = irrelevant results
- **Missing instruction**: Agent hallucinates instead of using retrieved docs
- **Poor parsing**: Messy text from PDFs breaks retrieval

## Next Steps
This is a simplified example for learning. For production:
- See the workshop slides on chunking strategies (recursive, semantic, document-based)
- Study embedding models and similarity metrics
- Explore proper vector databases
- Learn PDF parsing techniques (OCR, layout-aware)
