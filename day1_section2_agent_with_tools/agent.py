"""
Day 1 - Section 2: Agent with Tools
An agent equipped with tools - functions it can call to perform actions.
"""
from google.adk.agents import Agent
from google.adk.tools import google_search

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


def get_word_count(text: str) -> dict:
    """Counts the words in a piece of text.

    Args:
        text: The text to count words in.

    Returns:
        A dictionary with the word count: {"word_count": int}
    """
    words = text.split()
    return {"word_count": len(words)}


def calculate_sum(numbers: list[float]) -> dict:
    """Calculates the sum of a list of numbers.

    Args:
        numbers: A list of numbers to sum.

    Returns:
        A dictionary with the sum: {"sum": float}
    """
    total = sum(numbers)
    return {"sum": total}


def get_text_stats(text: str) -> dict:
    """Analyzes text and returns comprehensive statistics.

    Args:
        text: The text to analyze.

    Returns:
        A dictionary with various text statistics including word count,
        character count, sentence count, and average word length.
    """
    words = text.split()
    sentences = text.split('.')

    return {
        "word_count": len(words),
        "character_count": len(text),
        "sentence_count": len([s for s in sentences if s.strip()]),
        "average_word_length": sum(len(w) for w in words) / len(words) if words else 0
    }


root_agent = Agent(
    name="research_assistant_with_tools",
    model=_model,
    description="A research assistant that can search the web and analyze text.",
    instruction=(
        "You are a friendly research assistant with access to tools. "
        "When asked to count words, analyze text, or search for information, "
        "use your available tools. Always explain what you're doing and "
        "present results clearly. If unsure, say so."
    ),
    tools=[
        get_word_count,
        calculate_sum,
        get_text_stats,
        #google_search,
    ],
)
