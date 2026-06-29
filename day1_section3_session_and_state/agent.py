"""
Day 1 - Section 3: Sessions & State - Short-term Memory
Understanding sessions, state, and the Runner.
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


def save_preference(key: str, value: str) -> dict:
    """Saves a user preference to remember during this conversation.

    Args:
        key: The preference name (e.g., "favorite_color", "language")
        value: The preference value

    Returns:
        Confirmation with the saved key and value
    """
    # The actual saving to session state is handled by the agent framework
    # This tool just signals the intent
    return {
        "saved": True,
        "key": key,
        "value": value,
        "message": f"Saved preference: {key} = {value}"
    }


def recall_preference(key: str) -> dict:
    """Recalls a previously saved user preference from this conversation.

    Args:
        key: The preference name to recall

    Returns:
        The preference value if found, or a not found message
    """
    # The actual retrieval from session state is handled by the agent framework
    # This is a placeholder to demonstrate the concept
    return {
        "found": False,
        "key": key,
        "message": f"Looking for preference: {key} (handled by session state)"
    }


def add_to_list(item: str, list_name: str = "items") -> dict:
    """Adds an item to a named list for this conversation.

    Args:
        item: The item to add
        list_name: The name of the list (default: "items")

    Returns:
        Confirmation of the added item
    """
    return {
        "added": True,
        "item": item,
        "list_name": list_name,
        "message": f"Added '{item}' to {list_name}"
    }


root_agent = Agent(
    name="stateful_assistant",
    model=_model,
    description="An assistant that remembers things during the conversation.",
    instruction=(
        "You are a helpful assistant that can remember preferences and information "
        "within this conversation session. When users tell you to remember something, "
        "use the save_preference tool. When they ask you to recall, use recall_preference. "
        "You can also maintain lists using add_to_list. "
        "\n\n"
        "Key points:\n"
        "- Session: The current ongoing conversation\n"
        "- State: A key-value store that persists within this session\n"
        "- This is SHORT-TERM memory - it only lasts for this conversation\n"
        "- Be clear about what you've saved and can recall\n"
    ),
    tools=[
        save_preference,
        recall_preference,
        add_to_list,
    ],
)
