"""
Day 1 - Section 1: Your First Agent
A simple agent with a name, model, description, and instruction.
"""
from google.adk.agents import Agent

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

root_agent = Agent(
    name="research_assistant",
    model=_model,
    description="Answers general questions.",
    instruction=(
        "You are a friendly research assistant. "
        "Answer clearly. If unsure, say so."
    ),
)
