"""
Day 2 - Section 2: Parallel Agent (Fan-out Research)
Runs specialized agents simultaneously, then gathers results
"""
from google.adk.agents import Agent
from google.adk.agents.workflow_agents import ParallelAgent
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


# Specialist 1: Technical Research
tech_researcher = Agent(
    name="tech_researcher",
    model=_model,
    description="Researches technical aspects and specifications",
    instruction=(
        "You are a technical research specialist. When given a topic, focus on "
        "technical details, specifications, performance metrics, and engineering aspects. "
        "Use google_search to find technical documentation and specs. "
        "Present findings as clear technical bullet points."
    ),
    tools=[google_search],
)


# Specialist 2: Market Research
market_researcher = Agent(
    name="market_researcher",
    model=_model,
    description="Researches market trends, adoption, and business impact",
    instruction=(
        "You are a market research specialist. When given a topic, focus on "
        "market trends, adoption rates, competitive landscape, and business impact. "
        "Use google_search to find market data and industry reports. "
        "Present findings as business-focused bullet points."
    ),
    tools=[google_search],
)


# Specialist 3: User Impact Research
user_researcher = Agent(
    name="user_researcher",
    model=_model,
    description="Researches user experience and practical applications",
    instruction=(
        "You are a user experience research specialist. When given a topic, focus on "
        "how real users are affected, practical applications, use cases, and user feedback. "
        "Use google_search to find user reviews and case studies. "
        "Present findings from the user perspective."
    ),
    tools=[google_search],
)


# Root agent: Parallel research
root_agent = ParallelAgent(
    name="comprehensive_research",
    description="Conducts parallel research from technical, market, and user perspectives",
    instruction=(
        "You coordinate a parallel research team that investigates topics from "
        "three angles simultaneously:\n"
        "1. Technical aspects (specs, engineering)\n"
        "2. Market perspective (trends, business impact)\n"
        "3. User impact (applications, feedback)\n\n"
        "All three researchers work at the same time, then their findings are gathered "
        "and presented together for a comprehensive view."
    ),
    sub_agents=[tech_researcher, market_researcher, user_researcher],
)
