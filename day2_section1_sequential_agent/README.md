# Day 2 - Section 1: Sequential Agent (Multi-agent Pipeline)

## What You'll Learn
- How to compose multiple specialized agents
- Sequential workflow: step 1 → step 2 → step 3
- Why specialized agents are better than one agent doing everything
- How data flows between agents in a pipeline

## The Pattern: SequentialAgent

Runs sub-agents **one after another** in order. Perfect for pipelines where each step builds on the previous one.

```python
root_agent = SequentialAgent(
    name="pipeline",
    sub_agents=[agent1, agent2, agent3],  # runs in order
)
```

## This Example: Research → Write

1. **Researcher agent**: Gathers information using google_search
2. **Writer agent**: Takes research findings and creates a polished summary

Each agent is specialized and easier to:
- Instruct
- Test
- Debug
- Reuse

## How to Run
```bash
adk web day2_section1_sequential_agent
```

## Try It
Ask: "Research and write a summary about quantum computing"

Watch the trace to see:
1. The researcher gathering information
2. The writer receiving that information
3. The final polished output

## Why Specialize?

❌ **Bad**: One agent doing everything
- Complex, conflicting instructions
- Hard to debug which part failed
- Can't reuse components

✅ **Good**: Specialized agents in a pipeline
- Clear, focused instructions
- Easy to test each step
- Reusable components

## When to Use Sequential
- Pipelines where order matters (research → fact-check → write)
- Multi-step workflows (analyze → transform → summarize)
- Any task that's naturally "do A, then B, then C"

## ADK 2.0 Note
Under the hood, this runs as a graph in the Workflow Runtime. Each agent is a node, and the edges define the sequence.
