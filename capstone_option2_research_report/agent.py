"""
Capstone Option 2: Research → Report Pipeline
A SequentialAgent: researcher → fact-checker → writer
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


# Agent 1: Researcher
researcher = Agent(
    name="researcher",
    model=_model,
    description="Conducts thorough research on topics",
    instruction=(
        "You are a research specialist. When given a topic:\n"
        "1. Use google_search to gather comprehensive information\n"
        "2. Look for facts, statistics, expert opinions, and recent developments\n"
        "3. Organize findings into clear categories with bullet points\n"
        "4. Note your sources and key facts\n"
        "5. Be thorough but focused on quality information\n\n"
        "Your output will be used by a fact-checker, so be accurate!"
    ),
    tools=[google_search],
)


# Agent 2: Fact-Checker
fact_checker = Agent(
    name="fact_checker",
    model=_model,
    description="Verifies research findings and flags inconsistencies",
    instruction=(
        "You are a fact-checking specialist. Review the research provided and:\n"
        "1. Verify key claims using google_search when needed\n"
        "2. Flag any unsupported or questionable statements\n"
        "3. Note any contradictions or inconsistencies\n"
        "4. Confirm important statistics and dates\n"
        "5. Mark verified facts as [VERIFIED] and concerns as [NEEDS REVIEW]\n\n"
        "Your output guides the writer on what's reliable."
    ),
    tools=[google_search],
)


# Agent 3: Writer
writer = Agent(
    name="writer",
    model=_model,
    description="Creates polished reports from verified research",
    instruction=(
        "You are a professional writer. Create a polished report from the fact-checked research:\n\n"
        "STRUCTURE:\n"
        "1. Executive Summary (2-3 sentences)\n"
        "2. Introduction\n"
        "3. Main Findings (organized sections)\n"
        "4. Analysis and Insights\n"
        "5. Conclusion\n\n"
        "STYLE:\n"
        "- Clear, professional prose\n"
        "- Use only [VERIFIED] facts from the fact-checker\n"
        "- Note any [NEEDS REVIEW] items in a separate section\n"
        "- Cite sources when mentioned\n"
        "- Make it engaging but accurate\n\n"
        "Do not add information beyond what the researchers provided."
    ),
)


# Root: Sequential Pipeline
root_agent = SequentialAgent(
    name="research_report_pipeline",
    description="Full pipeline: research → verify → write professional reports",
    instruction=(
        "You coordinate a three-stage research-to-report pipeline:\n\n"
        "Stage 1: RESEARCH - Gather comprehensive information\n"
        "Stage 2: FACT-CHECK - Verify accuracy and flag concerns\n"
        "Stage 3: WRITE - Create a polished, professional report\n\n"
        "Each stage builds on the previous, ensuring quality and accuracy."
    ),
    sub_agents=[researcher, fact_checker, writer],
)
