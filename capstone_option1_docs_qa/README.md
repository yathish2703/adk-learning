# Capstone Option 1: Docs Q&A Agent

## Overview
A hybrid Q&A agent that searches local documents first, then falls back to web search for information not in the knowledge base.

## Strategy
1. **Primary**: Search local knowledge base (trusted, curated info)
2. **Fallback**: Google search (current, external info)

## Key Features
- Prioritizes internal documentation
- Falls back to web when needed
- Cites sources clearly
- Can combine both sources

## How to Run
```bash
adk web capstone_option1_docs_qa
```

## Try It
Add documents to the `knowledge_base/` folder, then ask:
- Questions about your documents (uses local search)
- Current events (uses google_search)
- Topics partially in docs (combines both!)

## Customization
1. Add your own .txt files to `knowledge_base/`
2. Adjust the search strategy in the instruction
3. Add more sophisticated ranking if needed

## Real-world Applications
- Internal company Q&A with web fallback
- Product documentation + latest updates
- Policies & procedures + regulatory news
