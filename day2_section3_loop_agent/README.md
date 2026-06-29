# Day 2 - Section 3: Loop Agent (Iterative Refinement)

## What You'll Learn
- How to create iterative workflows with loops
- When to use loops vs sequential/parallel
- How to define stopping conditions
- The power of self-critique and refinement

## The Pattern: LoopAgent

Repeats a sub-agent **until a condition is met**. Perfect for iterative improvement workflows like draft → critique → improve → repeat.

```python
root_agent = LoopAgent(
    name="iterative_process",
    sub_agent=refinement_step,
    max_iterations=5,  # safety limit
)
```

## This Example: Iterative Writing

A two-step refinement cycle that repeats:
1. **Writer**: Creates a draft or revises based on feedback
2. **Critic**: Evaluates and provides constructive feedback

The loop continues until the critic approves (score 8+) or hits max iterations (5).

```
Draft 1 → Critique → Draft 2 → Critique → Draft 3 → APPROVED!
```

## How to Run
```bash
adk web day2_section3_loop_agent
```

## Try It
Ask: "Write an article about the benefits of morning exercise"

Watch the trace to see:
- Initial draft creation
- Critic's feedback
- Revised draft addressing feedback
- Multiple iterations until approval
- The final polished version

## The Stopping Condition

```python
def should_continue_loop(output: str) -> bool:
    return "APPROVED" not in output.upper()
```

The loop continues **until**:
- The critic says "APPROVED" (quality threshold met), OR
- Max iterations reached (safety limit)

## When to Use Loops

✅ **Good for:**
- Iterative refinement (draft → critique → improve)
- Quality improvement cycles
- Self-correction workflows
- Repeated attempts until success

❌ **Not good for:**
- Tasks that don't improve with iteration
- When you need different agents for different steps
- Simple pipelines (use Sequential instead)

## Real-world Use Cases
- **Code review loops**: Write code → review → fix → repeat
- **Content refinement**: Draft → edit → improve → publish
- **Problem solving**: Attempt → verify → retry until correct
- **Design iterations**: Propose → critique → refine → approve

## Safety: Max Iterations

Always set `max_iterations` to prevent infinite loops! If the stopping condition is never met, the loop will exit after max iterations.

## Combining Patterns

Notice how this uses **LoopAgent + SequentialAgent**:
- Sequential: (writer → critic) is one iteration
- Loop: Repeat that iteration until approved

You can nest any workflow agents inside each other!
