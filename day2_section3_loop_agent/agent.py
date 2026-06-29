"""
Day 2 - Section 3: Loop Agent (Iterative Refinement)
Repeats a sub-agent until a condition is met: draft → critique → improve
"""
from google.adk.agents import Agent
from google.adk.agents.workflow_agents import LoopAgent, SequentialAgent

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


# Agent 1: Writer (creates drafts)
writer_agent = Agent(
    name="writer",
    model=_model,
    description="Writes content based on the given topic or improves existing drafts",
    instruction=(
        "You are a creative writer. When given a topic, write a short article (2-3 paragraphs). "
        "If you receive feedback, revise your draft to address the critique. "
        "Be open to improving clarity, structure, and engagement."
    ),
)


# Agent 2: Critic (evaluates drafts)
critic_agent = Agent(
    name="critic",
    model=_model,
    description="Evaluates writing and provides constructive feedback",
    instruction=(
        "You are a constructive editor and critic. Evaluate the draft and provide:\n"
        "1. What works well\n"
        "2. What needs improvement (clarity, structure, engagement)\n"
        "3. Specific suggestions for revision\n"
        "4. A score from 1-10 (quality rating)\n\n"
        "If the draft scores 8 or above, say 'APPROVED' at the end of your feedback. "
        "Otherwise, provide constructive critique to help improve it."
    ),
)


# Compose into a sequential refinement step (write → critique)
refinement_step = SequentialAgent(
    name="refinement_step",
    description="One iteration: write/revise then critique",
    sub_agents=[writer_agent, critic_agent],
)


# Loop the refinement until quality threshold is met
def should_continue_loop(output: str) -> bool:
    """
    Determines if the loop should continue based on the critic's output.
    Stops when the critic says "APPROVED".
    """
    return "APPROVED" not in output.upper()


root_agent = LoopAgent(
    name="iterative_writer",
    description="Iteratively refines writing through multiple draft-critique cycles",
    instruction=(
        "You coordinate an iterative writing process:\n"
        "1. The writer creates a draft (or revises based on feedback)\n"
        "2. The critic evaluates and provides feedback\n"
        "3. Loop continues until the critic approves (scores 8+)\n\n"
        "This demonstrates iterative improvement through multiple cycles."
    ),
    sub_agent=refinement_step,
    max_iterations=5,  # Safety limit: max 5 rounds of revision
)
