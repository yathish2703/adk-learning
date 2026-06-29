# Quick Start Guide

Get up and running with Google ADK in 5 minutes!

## 1. Install Python & ADK

```bash
# Check Python version (need 3.10+)
python --version

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install ADK
pip install google-adk

# Verify
adk --version
```

## 2. Get API Key

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Click "Get API key"
3. Copy your key

## 3. Set API Key

```bash
# Option A: Environment variable
export GOOGLE_API_KEY="your-key-here"

# Option B: .env file (in each agent folder)
echo "GOOGLE_API_KEY=your-key-here" > day1_section1_first_agent/.env
```

## 4. Run Your First Agent

```bash
# From the repo root:
adk web day1_section1_first_agent
```

This will:
- Start a local web server
- Open your browser automatically
- Show a chat interface

## 5. Try It!

In the chat, ask:
- "What is artificial intelligence?"
- "Explain quantum computing"
- "What's the weather?" (it won't know - no tools yet!)

**Click the "Trace" tab** to see how the agent reasoned!

## 6. Next Steps

### Learn the Basics (Day 1)
1. [First Agent](day1_section1_first_agent/) - You just did this! ✅
2. [Agent with Tools](day1_section2_agent_with_tools/) - Give it abilities
3. [Sessions & State](day1_section3_session_and_state/) - Add memory

### Advanced Patterns (Day 2)
4. [Sequential Agent](day2_section1_sequential_agent/) - Multi-step pipelines
5. [Parallel Agent](day2_section2_parallel_agent/) - Simultaneous work
6. [Loop Agent](day2_section3_loop_agent/) - Iterative refinement
7. [RAG Agent](day2_section4_rag_agent/) - Document-based answers

### Build Something Real (Capstone)
- [Docs Q&A](capstone_option1_docs_qa/) - Hybrid knowledge system
- [Research Report](capstone_option2_research_report/) - Full pipeline
- [Support Triage](capstone_option3_support_triage/) - Smart routing

## Common Commands

```bash
# Web UI (best for learning)
adk web <agent_folder>

# Terminal chat
adk run <agent_folder>

# Check version
adk --version

# Help
adk --help
```

## Troubleshooting

### "Agent not found"
Make sure you're in the **parent** directory:
```bash
# ❌ Wrong: inside the agent folder
cd day1_section1_first_agent
adk web .

# ✅ Right: from parent directory
cd adk-learning
adk web day1_section1_first_agent
```

### "API key not found"
```bash
# Check if set
echo $GOOGLE_API_KEY

# Set it
export GOOGLE_API_KEY="your-key"
```

### "Tool never called"
The tool's docstring is key - the model reads it to decide when to use the tool!

## Tips

1. **Always check the Trace view** - It shows what the agent is thinking
2. **Start simple** - Don't jump to complex multi-agent systems first
3. **Read the READMEs** - Each agent has detailed docs
4. **Experiment** - Try changing instructions and see what happens!

## Learning Path

```
Day 1: Basics (3-4 hours)
├── First Agent (30 min)
├── Tools (60 min)
└── Sessions (60 min)

Day 2: Advanced (3-4 hours)
├── Sequential/Parallel/Loop (90 min)
├── RAG (60 min)
└── Capstone project (90 min)
```

## Resources

- 📖 [Full README](README.md) - Complete documentation
- 👨‍🏫 [Workshop Guide](WORKSHOP_GUIDE.md) - For instructors
- 🏗️ [Basic Agent](basic_agent/) - Reference implementation
- 📊 [Workshop Slides](Google-ADK-2Day-Workshop.pptx) - Concepts

## Need Help?

1. Check the specific agent's README
2. Look at the workshop slides
3. Read [Google ADK docs](https://github.com/google/adk)

---

**You're ready!** 🚀

Start with `adk web day1_section1_first_agent` and work through each section.
