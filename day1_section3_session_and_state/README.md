# Day 1 - Section 3: Sessions & State (Short-term Memory)

## What You'll Learn
- What a Session is (one ongoing conversation)
- What State is (key-value scratchpad within a session)
- What a Runner does (executes agent, manages session)
- The difference between session state and long-term memory

## Key Concepts

### Session
One ongoing conversation that holds events (messages and tool calls history).

### State
A key-value scratchpad on the session that remembers things within ONE chat. This is short-term memory that disappears when the session ends.

### Runner
Executes the agent and manages the session via a SessionService.

```python
runner = Runner(
    agent=root_agent,
    app_name="my_app",
    session_service=InMemorySessionService()
)
```

### Don't Confuse These!
- **State**: Lives inside one conversation (short-term)
- **Memory**: Persists across separate conversations (long-term) - that's Day 2!

## How to Run
```bash
# Run with web UI
adk web day1_section3_session_and_state

# Or see the runner code
python day1_section3_session_and_state/runner_example.py
```

## Try It
1. "Remember my favorite color is blue"
2. "What's my favorite color?" (it should remember!)
3. "Add 'buy milk' to my shopping list"
4. "Add 'buy eggs' to my shopping list"
5. "What's on my shopping list?"

Now close the session and start a new one - the state is gone!

## Session Services Available
- **InMemorySessionService**: Default, stores in RAM (gone when app stops)
- **DatabaseSessionService**: Persists to a database
- **VertexAiSessionService**: Uses Google Cloud (not in this local example)

## Key Takeaways
- State is temporary and lives only within the current session
- The agent doesn't "remember" across different conversations by default
- For long-term memory, you need Memory tools (Day 2)
- The Runner manages the lifecycle: session creation, event storage, state management
