# Agent Examples Summary

Quick reference for all agents in this workshop.

## Day 1: Foundations

| Section | Agent | Concepts | Run Command |
|---------|-------|----------|-------------|
| 1 | [First Agent](day1_section1_first_agent/) | Basic agent structure, name/model/instruction | `adk web day1_section1_first_agent` |
| 2 | [Agent with Tools](day1_section2_agent_with_tools/) | Tool functions, docstrings, google_search | `adk web day1_section2_agent_with_tools` |
| 3 | [Sessions & State](day1_section3_session_and_state/) | Runner, SessionService, short-term memory | `adk web day1_section3_session_and_state` |

## Day 2: Advanced Patterns

| Section | Agent | Concepts | Run Command |
|---------|-------|----------|-------------|
| 1 | [Sequential Agent](day2_section1_sequential_agent/) | Multi-agent pipeline, research→write | `adk web day2_section1_sequential_agent` |
| 2 | [Parallel Agent](day2_section2_parallel_agent/) | Simultaneous execution, fan-out research | `adk web day2_section2_parallel_agent` |
| 3 | [Loop Agent](day2_section3_loop_agent/) | Iterative refinement, draft→critique→improve | `adk web day2_section3_loop_agent` |
| 4 | [RAG Agent](day2_section4_rag_agent/) | Document retrieval, grounded answers | `adk web day2_section4_rag_agent` |

## Capstone Projects

| Project | Description | Key Features | Run Command |
|---------|-------------|--------------|-------------|
| [Docs Q&A](capstone_option1_docs_qa/) | Hybrid knowledge system | RAG + web search fallback | `adk web capstone_option1_docs_qa` |
| [Research Report](capstone_option2_research_report/) | Full research pipeline | Research→fact-check→write | `adk web capstone_option2_research_report` |
| [Support Triage](capstone_option3_support_triage/) | Intelligent routing | Coordinator + specialists | `adk web capstone_option3_support_triage` |

## Key Patterns

### Agent Composition
```python
# Sequential: A → B → C
SequentialAgent(sub_agents=[agent_a, agent_b, agent_c])

# Parallel: A + B + C simultaneously
ParallelAgent(sub_agents=[agent_a, agent_b, agent_c])

# Loop: repeat until condition
LoopAgent(sub_agent=refinement_step, max_iterations=5)
```

### Tool Definition
```python
def tool_name(param: type) -> dict:
    """Clear description for the model.
    
    Args:
        param: What this parameter is
    
    Returns:
        {"key": "structured data"}
    """
    return {"result": "value"}
```

### RAG Pattern
```python
# 1. Create retrieval tool
def retrieve_documents(query: str) -> dict:
    # Search document store
    return {"documents": [...]}

# 2. Agent with retrieval
agent = Agent(
    tools=[retrieve_documents],
    instruction="Answer ONLY from retrieved documents"
)
```

## Workflow Patterns Comparison

| Pattern | Use When | Example | Performance |
|---------|----------|---------|-------------|
| **Sequential** | Steps depend on each other | Research → Write | Slower (serial) |
| **Parallel** | Independent tasks | 3 researchers | Faster (parallel) |
| **Loop** | Need iteration/refinement | Draft → Critique | Depends on iterations |

## Common Configurations

### Basic Agent
```python
Agent(
    name="agent_name",
    model="gemini-2.0-flash",
    description="What this agent does",
    instruction="Detailed behavior instructions",
    tools=[tool1, tool2]
)
```

### Sequential Pipeline
```python
SequentialAgent(
    name="pipeline",
    description="Multi-step workflow",
    sub_agents=[step1, step2, step3]
)
```

### Parallel Execution
```python
ParallelAgent(
    name="parallel_team",
    description="Simultaneous tasks",
    sub_agents=[worker1, worker2, worker3]
)
```

### Iterative Loop
```python
LoopAgent(
    name="refinement",
    sub_agent=refinement_step,
    max_iterations=5  # Safety limit
)
```

## File Structure Pattern

Every agent follows this structure:
```
agent_name/
├── __init__.py          # from . import agent
├── agent.py             # root_agent definition
├── README.md            # Documentation
└── [additional files]   # Optional: tools, data, etc.
```

## Quick Reference: What to Use When

| You Want To... | Use This Pattern | Example |
|---------------|------------------|---------|
| Simple Q&A | Basic Agent | day1_section1 |
| Give abilities | Tools | day1_section2 |
| Remember in chat | Session State | day1_section3 |
| Multi-step workflow | SequentialAgent | day2_section1 |
| Faster parallel work | ParallelAgent | day2_section2 |
| Iterative improvement | LoopAgent | day2_section3 |
| Answer from docs | RAG + retrieval | day2_section4 |
| Complex system | Capstone projects | Combined patterns |

## Testing Your Agents

```bash
# Web UI - best for development
adk web <agent_folder>

# Terminal - quick tests
adk run <agent_folder>

# Check what the agent is thinking
# → Click "Trace" tab in web UI
```

## Dependencies

All agents use:
- **google-adk**: Core framework
- **gemini-2.0-flash**: LLM model (free API)
- **Local execution**: No cloud needed

Some agents additionally use:
- **google_search**: Built-in tool (requires API key)
- **python-pptx**: For reading PowerPoint (installed)
- **lxml, pillow**: For document processing (installed)

## Performance Notes

| Pattern | Speed | Resource Use | Best For |
|---------|-------|--------------|----------|
| Basic Agent | Fast | Low | Simple tasks |
| + Tools | Fast | Low | Single actions |
| Sequential | Slow (serial) | Medium | Ordered workflows |
| Parallel | Fast | High | Independent tasks |
| Loop | Varies | Medium-High | Refinement |
| RAG | Medium | Medium | Document Q&A |

## Next Steps

1. Work through Day 1 agents (basics)
2. Learn Day 2 patterns (composition)
3. Build a capstone project (integration)
4. Deploy your own agent (production)

See [README.md](README.md) for full documentation.
