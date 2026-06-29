# Day 1 - Section 2: Agent with Tools

## What You'll Learn
- How to give an agent tools (Python functions)
- How to write good tool docstrings that the model understands
- How the agent decides when and how to call tools
- Using built-in tools like `google_search`

## The Key: Tools are Just Functions
A tool is a Python function with:
1. Type hints for parameters
2. A clear docstring (this is what the model reads!)
3. Structured return data (use dict, not plain strings)

## Tools Included
- `get_word_count`: Count words in text
- `calculate_sum`: Sum a list of numbers
- `get_text_stats`: Comprehensive text analysis
- `google_search`: Built-in web search (ADK provided)

## How to Run
```bash
adk web day1_section2_agent_with_tools
```

## Try It
- "Count the words in 'Hello world from ADK'"
- "What is the sum of 10, 25, and 37?"
- "Analyze this text: [paste a paragraph]"
- "Search for the latest news about Google AI"
- "What's the weather?" (watch it decide to use google_search)

## Key Lessons
- **Bad docstring = misused tool**: The model relies on your description
- **Return structured data**: Use `{"key": value}` not just strings
- **The model decides**: You don't control when tools are called
- **Watch the trace**: See the agent's reasoning in adk web

## Common Mistakes
- Missing or vague docstrings
- Returning plain strings instead of structured data
- Not handling edge cases in tools
