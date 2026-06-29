# Day 1 - Section 1: Your First Agent

## What You'll Learn
- What an agent really is (reason → act → observe)
- The 4 essential components of an agent: name, model, description, instruction
- How to run and test your agent locally

## The Simplest Agent
This is the most basic agent possible - just a name, model, and instructions.

## How to Run
```bash
# From the repo root directory:
adk web day1_section1_first_agent

# Or for terminal chat:
adk run day1_section1_first_agent
```

## Try It
- Ask it: "What is artificial intelligence?"
- Ask it: "What is the capital of France?"
- Ask it something it doesn't know
- Watch how it responds when uncertain

## Key Concepts
- **name**: How other agents refer to it
- **model**: Which LLM powers it (gemini-2.0-flash)
- **description**: Used when delegating to sub-agents
- **instruction**: The system prompt that defines behavior
