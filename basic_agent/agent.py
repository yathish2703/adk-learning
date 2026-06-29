from google.adk.agents import LlmAgent
from basic_agent.root_instruction import root_instruction
try:
    from lilly_tools.llm_config import create_llm_model_with_auth
    LLM_AUTHENTICATED = True
except ImportError as e:
    print(f"Warning: {e}")
    print("lilly_tools not available, using unauthenticated model string")
    LLM_AUTHENTICATED = False
print(f"LLM_AUTHENTICATED: {LLM_AUTHENTICATED}")
# Create agent
if LLM_AUTHENTICATED:
    try:
        _model = create_llm_model_with_auth(model_name="anthropic/claude-sonnet-4.6")
    except Exception:
        _model = "anthropic/claude-sonnet-4.6"
else:
    _model = "gemini-2.0-flash"

root_agent = LlmAgent(
    name="hello_world",
    model=_model,
    description="Collects clinical trial data from ClinicalTrials.gov with incremental storage",
    instruction=root_instruction
)

