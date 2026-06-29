# Google ADK Workshop - Complete Learning Path

A comprehensive 2-day hands-on workshop for building AI agents with Google's Agent Development Kit (ADK).

## 🎯 Workshop Overview

This repository contains hands-on examples for learning Google ADK from basics to advanced multi-agent systems. All examples run **locally** without requiring Google Cloud dependencies (Day 1) or cloud services (simplified for local learning).

## 📚 Repository Structure

### Day 1: Foundations

#### [Section 1: Your First Agent](day1_section1_first_agent/)
- The simplest possible agent: name, model, description, instruction
- Understanding the reason → act → observe loop
- Running agents with `adk web` and `adk run`

#### [Section 2: Agent with Tools](day1_section2_agent_with_tools/)
- Writing tool functions with proper docstrings
- How the model decides when to call tools
- Using built-in tools like `google_search`
- Best practices for tool design

#### [Section 3: Sessions & State](day1_section3_session_and_state/)
- Understanding sessions (one conversation)
- Using state (short-term memory within a session)
- The Runner and SessionService
- Difference between state and long-term memory

### Day 2: Real Systems

#### [Section 1: Sequential Agent](day2_section1_sequential_agent/)
- Multi-agent pipelines: step 1 → step 2 → step 3
- Researcher → Writer example
- When to specialize agents
- Benefits of composed systems

#### [Section 2: Parallel Agent](day2_section2_parallel_agent/)
- Running agents simultaneously for speed
- Fan-out research from multiple perspectives
- Tech + Market + User research example
- When to use parallel vs sequential

#### [Section 3: Loop Agent](day2_section3_loop_agent/)
- Iterative refinement workflows
- Draft → Critique → Improve cycles
- Defining stopping conditions
- Safety with max_iterations

#### [Section 4: RAG Agent](day2_section4_rag_agent/)
- Retrieval-Augmented Generation (RAG)
- Local document search and retrieval
- Grounding answers in your documents
- The 6-step RAG pipeline

### Capstone Projects

#### [Option 1: Docs Q&A with Web Fallback](capstone_option1_docs_qa/)
- RAG over local documents
- Google search as fallback
- Hybrid knowledge strategy

#### [Option 2: Research → Report Pipeline](capstone_option2_research_report/)
- Three-stage: Research → Fact-Check → Write
- Quality control through specialization
- Professional report generation

#### [Option 3: Support Triage System](capstone_option3_support_triage/)
- Intelligent request routing
- Specialized support agents (Tech/Billing/General)
- Coordinator pattern

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or newer
- A Google AI Studio API key (free, for Gemini)
- Terminal and code editor

### Installation

```bash
# Clone this repo
cd adk-learning

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install ADK
pip install google-adk

# Verify installation
adk --version
```

### Set Up API Key

Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey), then:

```bash
# Set environment variable
export GOOGLE_API_KEY="your-api-key-here"

# Or create a .env file in each agent folder
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

### Running Examples

```bash
# Run any example with the web UI
adk web day1_section1_first_agent

# Or use terminal chat
adk run day1_section1_first_agent
```

## 📖 Learning Path

Follow this recommended sequence:

1. **Day 1, Section 1-3**: Learn the basics (agents, tools, state)
2. **Day 2, Section 1-3**: Master multi-agent patterns (sequential, parallel, loop)
3. **Day 2, Section 4**: Understand RAG for document-grounded responses
4. **Capstone**: Build a complete project combining the concepts

## 🎓 Key Concepts

### What is an AI Agent?
An agent is an LLM given a goal and tools, running in a loop until the task is done:
- **Reason**: Decide what to do next
- **Act**: Call a tool with inputs
- **Observe**: Feed result back, repeat

### Why ADK?
- **Code-first**: Define agents in Python, not config files
- **Model-agnostic**: Works with Gemini, Claude, and others
- **Batteries included**: Web UI, tools, memory, deployment
- **Scales up**: One agent → multi-agent systems

### Three Workflow Patterns
1. **SequentialAgent**: A → B → C (pipelines)
2. **ParallelAgent**: A + B + C (fan-out, simultaneous)
3. **LoopAgent**: Repeat A until condition (iterative)

## 🛠️ Tech Stack

- **Google ADK**: Agent framework
- **Gemini 2.0 Flash**: LLM (via free API key)
- **Local tools**: No cloud dependencies for learning
- **Python 3.10+**: Core language

## 📂 Project Structure

```
adk-learning/
├── day1_section1_first_agent/       # Simplest agent
├── day1_section2_agent_with_tools/  # Tools
├── day1_section3_session_and_state/ # Memory
├── day2_section1_sequential_agent/  # Pipelines
├── day2_section2_parallel_agent/    # Parallel
├── day2_section3_loop_agent/        # Loops
├── day2_section4_rag_agent/         # RAG
├── capstone_option1_docs_qa/        # Project 1
├── capstone_option2_research_report/# Project 2
├── capstone_option3_support_triage/ # Project 3
└── basic_agent/                     # Reference implementation
```

Each folder contains:
- `agent.py`: The agent definition
- `README.md`: Detailed documentation
- Additional files as needed

## 🎯 What You'll Build

By the end of this workshop, you'll have built:
- ✅ Single agents with tools
- ✅ Multi-agent pipelines
- ✅ Parallel research systems
- ✅ Iterative refinement loops
- ✅ RAG-powered Q&A agents
- ✅ A complete capstone project

## 🔍 Key Patterns Demonstrated

### Agent Composition
```python
# Sequential: research → write
SequentialAgent(sub_agents=[researcher, writer])

# Parallel: tech + market + user
ParallelAgent(sub_agents=[tech, market, user])

# Loop: draft → critique → improve
LoopAgent(sub_agent=refinement_step, max_iterations=5)
```

### Tool Definition
```python
def get_word_count(text: str) -> dict:
    """Counts words in text.

    Args:
        text: The text to count

    Returns:
        {"word_count": int}
    """
    return {"word_count": len(text.split())}
```

### RAG Pattern
```python
# 1. Retrieve relevant documents
docs = retrieve_documents(query)

# 2. Agent answers from retrieved content
agent = Agent(
    tools=[retrieve_documents],
    instruction="Answer ONLY from retrieved documents"
)
```

## 🚦 Common Pitfalls

1. **Agent not found**: Missing `root_agent` variable or wrong folder
2. **Tool never called**: Vague/missing docstring
3. **RAG returns nothing**: Empty document store or wrong path
4. **Hallucinated answers**: Instruction didn't enforce grounding

See individual README files for troubleshooting tips.

## 📈 Next Steps

After completing this workshop:

1. **Official Docs**: [Google ADK Documentation](https://github.com/google/adk)
2. **Sample Gallery**: Explore more examples
3. **Evaluation**: Learn to test agent reliability
4. **Deployment**: Deploy to Cloud Run or GKE
5. **Advanced**: Memory systems, callbacks, custom workflows

## 🤝 Contributing

This is a learning repository. Feel free to:
- Add your own examples
- Improve documentation
- Report issues
- Share your capstone projects

## 📝 License

Educational use - based on Google ADK 2.0 workshop materials.

## 🙋 Support

- Check individual agent README files
- Review the workshop slides (Google-ADK-2Day-Workshop.pptx)
- Consult [Google ADK docs](https://github.com/google/adk)

---

**Happy Building! 🚀**

Start with [day1_section1_first_agent](day1_section1_first_agent/) and work your way through!
