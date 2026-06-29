"""
Day 2 - Section 1: Sequential Agent (Multi-agent Pipeline)
Runs specialized agents one after another: researcher → writer
"""
from google.adk.agents import Agent
from google.adk.agents.workflow_agents import SequentialAgent
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


# First specialized agent: Research
researcher_agent = Agent(
    name="researcher",
    model=_model,
    description="Researches topics and gathers information",
    instruction=(
        "You are a research specialist. When given a topic, gather comprehensive "
        "information about it. Use google_search to find current data. "
        "Organize your findings into clear bullet points with key facts, "
        "statistics, and recent developments. Be thorough but concise."
    ),
    #tools=[google_search],
)


# Second specialized agent: Writer
writer_agent = Agent(
    name="writer",
    model=_model,
    description="Takes research findings and writes clear summaries",
    instruction=(
        "You are a writing specialist. You receive research findings and turn them "
        "into a well-structured summary. Write in clear, engaging prose. "
        "Structure your output with:\n"
        "1. A brief introduction\n"
        "2. Main points in organized paragraphs\n"
        "3. A concise conclusion\n"
        "Make it readable and professional. Do not add information not in the research."
    ),
)


# Root agent: Sequential pipeline
root_agent = SequentialAgent(
    name="research_pipeline",
    description="A research-to-report pipeline that researches then writes",
    instruction=(
        "You coordinate a two-step pipeline:\n"
        "1. First, the researcher gathers information on the topic\n"
        "2. Then, the writer creates a polished summary from those findings\n"
        "Each step builds on the previous one."
    ),
    sub_agents=[researcher_agent, writer_agent],
)
