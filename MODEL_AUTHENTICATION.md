# Model Authentication Pattern

All agents in this workshop now support **automatic model fallback**: they try to use authenticated LLM models (like Claude) first, then fall back to Gemini if authentication is not available.

## How It Works

```python
# Try to import authentication tools
try:
    from lilly_tools.llm_config import create_llm_model_with_auth
    LLM_AUTHENTICATED = True
except ImportError:
    LLM_AUTHENTICATED = False

# Choose model based on authentication
if LLM_AUTHENTICATED:
    try:
        _model = create_llm_model_with_auth(model_name="anthropic/claude-sonnet-4.6")
    except Exception:
        _model = "anthropic/claude-sonnet-4.6"
else:
    _model = "gemini-2.0-flash"

# Use the selected model
root_agent = Agent(
    name="agent_name",
    model=_model,  # Either authenticated Claude or Gemini
    # ... rest of config
)
```

## Three Fallback Levels

1. **Best**: Authenticated LLM (Claude Sonnet 4.6) via lilly_tools
2. **Good**: Unauthenticated Claude model string
3. **Default**: Gemini 2.0 Flash (free with Google AI API key)

## When Each Model Is Used

| Scenario | Model Used | Requirements |
|----------|------------|--------------|
| `lilly_tools` available + working | Claude Sonnet 4.6 (authenticated) | lilly_tools installed and configured |
| `lilly_tools` available but fails | Claude Sonnet 4.6 (unauthenticated) | ADK with Anthropic support |
| `lilly_tools` not available | Gemini 2.0 Flash | Google AI Studio API key |

## Benefits

✅ **Works everywhere**: Falls back to free Gemini if authentication fails
✅ **Uses best model when available**: Automatically uses Claude when authenticated
✅ **No manual switching**: Detects environment automatically
✅ **Safe**: Multiple fallback layers prevent failures

## For Workshop Participants

### Using Gemini (Default - No Setup Needed)
If you don't have `lilly_tools`, agents automatically use Gemini:
```bash
export GOOGLE_API_KEY="your-gemini-api-key"
adk web day1_section1_first_agent
```

### Using Authenticated Claude (Advanced)
If you have `lilly_tools` configured:
```bash
# lilly_tools will handle authentication
adk web day1_section1_first_agent
```

The agent automatically detects and uses the authenticated model!

## Verifying Which Model Is Used

Check the agent's startup output:
```python
# basic_agent prints this on startup:
print(f"LLM_AUTHENTICATED: {LLM_AUTHENTICATED}")
```

Or check the ADK logs when running the agent.

## All Updated Agents

Every agent now has this pattern:
- ✅ Day 1: All 3 agents
- ✅ Day 2: All 4 agents
- ✅ Capstone: All 3 projects

## Customizing the Model

To use a different model, edit the fallback values in any agent's `agent.py`:

```python
if LLM_AUTHENTICATED:
    try:
        _model = create_llm_model_with_auth(model_name="anthropic/claude-opus-4")
    except Exception:
        _model = "anthropic/claude-opus-4"
else:
    _model = "gemini-2.0-flash"  # or "gemini-1.5-pro", etc.
```

## Troubleshooting

### "Model not found" error
The authenticated model string failed and ADK doesn't support that model. Solution:
- Ensure ADK is up to date: `pip install -U google-adk`
- Or change the fallback to a supported model

### Always using Gemini
`lilly_tools` is not installed or not importable. This is expected and fine!
- Workshop participants should use Gemini (free)
- Internal users should ensure `lilly_tools` is in the Python path

### Want to force a specific model?
Replace the conditional logic with a direct model string:
```python
# Force Gemini
_model = "gemini-2.0-flash"

# Or force Claude (requires authentication)
_model = create_llm_model_with_auth(model_name="anthropic/claude-sonnet-4.6")
```

## Why This Pattern?

This pattern came from [basic_agent/agent.py](basic_agent/agent.py) which demonstrates best practices:
- Works in both internal (authenticated) and external (public workshop) environments
- No code changes needed when moving between environments
- Safe fallbacks prevent runtime errors
- Automatic detection reduces configuration burden

---

**All agents are now flexible and work in any environment!** 🎉
