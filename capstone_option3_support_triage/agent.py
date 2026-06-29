"""
Capstone Option 3: Support Triage Agent
A coordinator that delegates to specialist sub-agents based on request type.
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


# Specialist 1: Technical Support
technical_support = Agent(
    name="technical_support",
    model=_model,
    description="Handles technical issues, bugs, and troubleshooting",
    instruction=(
        "You are a technical support specialist. When handling technical requests:\n"
        "1. Gather diagnostic information\n"
        "2. Identify the likely root cause\n"
        "3. Provide clear step-by-step solutions\n"
        "4. Use google_search if you need to look up error codes or known issues\n"
        "5. Escalate to engineering if it's a bug requiring code changes\n\n"
        "Be systematic, patient, and thorough."
    ),
    tools=[google_search],
)


# Specialist 2: Billing Support
billing_support = Agent(
    name="billing_support",
    model=_model,
    description="Handles billing questions, invoices, and payment issues",
    instruction=(
        "You are a billing support specialist. When handling billing requests:\n"
        "1. Confirm account details\n"
        "2. Explain charges clearly\n"
        "3. Guide through payment processes\n"
        "4. Handle refund requests according to policy\n"
        "5. Use google_search to check current pricing or policies if needed\n\n"
        "Be friendly, clear about policies, and helpful with solutions."
    ),
    tools=[google_search],
)


# Specialist 3: General Inquiries
general_support = Agent(
    name="general_support",
    model=_model,
    description="Handles product questions, how-to guides, and general information",
    instruction=(
        "You are a general support specialist. When handling general inquiries:\n"
        "1. Answer product questions clearly\n"
        "2. Provide how-to guidance step by step\n"
        "3. Point to relevant documentation\n"
        "4. Use google_search to find official guides or FAQs\n"
        "5. Be friendly and educational\n\n"
        "Help users understand features and get the most value."
    ),
    tools=[google_search],
)


# Coordinator: Triage Agent
root_agent = Agent(
    name="support_coordinator",
    model=_model,
    description="Triages support requests and delegates to appropriate specialists",
    instruction=(
        "You are a support triage coordinator. Your job is to:\n\n"
        "1. UNDERSTAND the user's request\n"
        "2. CLASSIFY it into one of these categories:\n"
        "   - Technical (bugs, errors, troubleshooting)\n"
        "   - Billing (payments, invoices, charges)\n"
        "   - General (how-to, features, product info)\n"
        "3. DELEGATE to the appropriate specialist agent\n"
        "4. SUMMARIZE the specialist's response to the user\n\n"
        "Use these sub-agents:\n"
        "- technical_support: For technical issues\n"
        "- billing_support: For billing questions\n"
        "- general_support: For general inquiries\n\n"
        "If a request spans multiple categories, prioritize the most urgent aspect.\n"
        "Always be clear about who's helping and why."
    ),
    # Note: In a real implementation, you'd use sub-agents here
    # For this demo, we'll explain the pattern
    tools=[google_search],
)
