# Day 2 - Section 2: Parallel Agent (Fan-out Research)

## What You'll Learn
- How to run multiple agents simultaneously
- When to use parallel vs sequential workflows
- How to gather and combine parallel results
- The performance benefits of parallelization

## The Pattern: ParallelAgent

Runs sub-agents **at the same time**, then gathers all results together. Perfect for fan-out research where you need different perspectives on the same topic.

```python
root_agent = ParallelAgent(
    name="parallel_research",
    sub_agents=[agent1, agent2, agent3],  # all run simultaneously
)
```

## This Example: Multi-angle Research

Three specialists research the same topic simultaneously:
1. **Tech researcher**: Technical specs and engineering
2. **Market researcher**: Business trends and adoption
3. **User researcher**: User experience and applications

All three run at once, dramatically faster than sequential!

## How to Run
```bash
adk web day2_section2_parallel_agent
```

## Try It
Ask: "Research electric vehicles"

Watch the trace to see:
- All three researchers starting simultaneously
- Each gathering different types of information
- Results being gathered and combined

## Parallel vs Sequential

### Use Sequential when:
- Order matters (research → fact-check → write)
- One step depends on the previous step
- You need a pipeline

### Use Parallel when:
- Tasks are independent
- You need multiple perspectives
- Speed matters (parallelization is faster!)
- Fan-out research

## Performance Benefits

```
Sequential: agent1 → agent2 → agent3  (takes 3x time)
Parallel:   agent1 ↓
            agent2 ↓  (all at once, takes 1x time)
            agent3 ↓
```

## Real-world Use Cases
- **Competitive analysis**: Research multiple competitors simultaneously
- **Multi-source verification**: Check multiple sources for fact-checking
- **Comprehensive research**: Technical + business + user perspectives
- **Portfolio analysis**: Evaluate multiple options in parallel

## Key Concept
The agents don't communicate with each other—they all work independently on the same input, then their outputs are gathered together.
