# Workshop Instructor Guide

## Workshop Timeline (2 Days)

### Day 1: Foundations (6 hours)

#### Session 1: Introduction (45 min)
- What is an AI agent? (reason → act → observe)
- What is ADK and why use it?
- Setup verification

**Hands-on**: [day1_section1_first_agent/](day1_section1_first_agent/)
- Build the simplest agent
- Run with `adk web`
- Explore the trace view

#### Session 2: Tools (90 min)
- Tools are just Python functions
- Writing good docstrings
- How models decide when to call tools

**Hands-on**: [day1_section2_agent_with_tools/](day1_section2_agent_with_tools/)
- Create custom tools (word_count, calculate_sum, text_stats)
- Use built-in google_search
- Watch tool calls in the trace

**Break**: 15 min

#### Session 3: Sessions & State (90 min)
- Session = one conversation
- State = short-term memory
- Runner and SessionService

**Hands-on**: [day1_section3_session_and_state/](day1_section3_session_and_state/)
- Build stateful agent
- Save and recall preferences
- Understand session lifecycle

**Lunch**: 60 min

#### Session 4: Practice & Review (90 min)
- Students experiment with their own ideas
- Q&A and troubleshooting
- Common pitfalls discussion

---

### Day 2: Real Systems (6 hours)

#### Session 1: Multi-Agent Orchestration (90 min)
- Why specialize agents?
- Three workflow patterns: Sequential, Parallel, Loop
- When to use each

**Hands-on Part 1**: [day2_section1_sequential_agent/](day2_section1_sequential_agent/)
- Research → Writer pipeline
- Watch data flow between agents

**Hands-on Part 2**: [day2_section2_parallel_agent/](day2_section2_parallel_agent/)
- Three researchers (Tech, Market, User)
- See parallelization performance

**Break**: 15 min

#### Session 2: Loops & RAG (120 min)
- Iterative refinement with loops
- What is RAG really?
- The 6-step RAG pipeline

**Hands-on Part 1**: [day2_section3_loop_agent/](day2_section3_loop_agent/)
- Draft → Critique → Improve loop
- Stopping conditions
- Max iterations safety

**Hands-on Part 2**: [day2_section4_rag_agent/](day2_section4_rag_agent/)
- Local document retrieval
- Grounding responses in documents
- Understanding chunking and retrieval

**Lunch**: 60 min

#### Session 3: Capstone Projects (120 min)
Students choose one project:

1. **[Docs Q&A](capstone_option1_docs_qa/)**: RAG + web fallback
2. **[Research Report](capstone_option2_research_report/)**: Research → fact-check → write
3. **[Support Triage](capstone_option3_support_triage/)**: Intelligent routing system

Each person/pair builds and demos their project.

#### Session 4: Demos & Wrap-up (60 min)
- Student demos (5 min each)
- Walk through interesting traces
- Discussion: lessons learned
- Next steps & resources

---

## Teaching Tips

### Day 1

**Section 1 - First Agent**
- Spend real time in the trace view - this builds intuition
- Show the reason → act → observe loop visually
- Let students ask simple questions first
- Common mistake: running `adk web` from wrong directory

**Section 2 - Tools**
- Emphasize docstrings - the model reads them!
- Show a tool with bad docstring, watch it fail
- Return structured data (dict), not plain strings
- Let students create their own tool

**Section 3 - Sessions**
- Don't conflate state, memory, and RAG - be explicit
- State = temporary, this conversation only
- Demo: save preference, end session, show it's gone
- Explain Runner and SessionService architecture

### Day 2

**Section 1 - Multi-Agent**
- Start with WHY specialize (not HOW)
- Draw the patterns on a whiteboard:
  - Sequential: →→→
  - Parallel: |||
  - Loop: ⟲
- Show performance benefit of parallel in the trace
- Students often try to nest incorrectly - watch for this

**Section 2 - Loops & RAG**
- Loop: emphasize max_iterations safety
- RAG: explain it's NOT learning, it's retrieving + reading fresh
- Show what happens when you ask about something NOT in docs
- Common mistake: not instructing agent to ground in retrieved text

**Section 3 - Capstone**
- Let students choose their project
- Encourage pair programming
- Walk around and help debug
- Focus on getting something working, not perfect

**Section 4 - Demos**
- Every student demos (even if incomplete)
- Use the trace view during demos - most interesting part!
- Ask: "What would you do next?"
- Celebrate learning, not perfection

---

## Common Issues & Solutions

### "Agent not found"
**Problem**: `adk web` can't find root_agent
**Solution**:
- Check you're in parent directory, not agent directory
- Verify `root_agent` variable exists in agent.py
- Check `__init__.py` imports agent

### "Tool never called"
**Problem**: Agent doesn't use the tool
**Solution**:
- Check docstring - is it clear when to use it?
- Is the tool in the tools list?
- Try asking more explicitly

### "RAG returns nothing"
**Problem**: retrieve_documents returns empty
**Solution**:
- Check documents loaded (print DOCUMENT_STORE)
- Verify file paths
- Try simpler query with obvious keywords

### "Agent hallucinates instead of using documents"
**Problem**: Answers questions not in docs
**Solution**:
- Strengthen instruction: "Answer ONLY from retrieved text"
- Add: "If not found, say 'I don't have that information'"
- Show this in the RAG section explicitly

---

## Customization for Your Audience

### For Beginners
- Slow down on Day 1
- More time on each hands-on
- Simpler capstone projects
- More guided exercises

### For Experienced Developers
- Quick through Day 1
- More time on multi-agent patterns
- More ambitious capstone projects
- Discuss production considerations

### For Researchers
- Emphasize evaluation and reliability
- Discuss limitations and failure modes
- Add academic use cases
- Cover experimental features

---

## Materials Checklist

Before the workshop:
- [ ] All students have Python 3.10+ installed
- [ ] Google AI Studio API keys obtained
- [ ] ADK installed and verified (`adk --version`)
- [ ] Repository cloned locally
- [ ] Environment variables set (GOOGLE_API_KEY)
- [ ] Test: run `adk web day1_section1_first_agent`

During the workshop:
- [ ] Slides ready (Google-ADK-2Day-Workshop.pptx)
- [ ] Whiteboard/digital board for diagrams
- [ ] Backup internet connection
- [ ] Help channel (Slack/Discord) for async questions

---

## Key Messages to Reinforce

1. **Agents loop** - They're not one Q&A, they reason-act-observe repeatedly
2. **Tools are functions** - Clear docstrings = better tool use
3. **Specialize agents** - Multiple simple agents > one complex agent
4. **Three workflows** - Sequential, Parallel, Loop (and you can nest them!)
5. **RAG retrieves fresh** - It doesn't "learn" documents, it reads them each time
6. **Code-first** - Everything is Python, testable and version-controlled

---

## Post-Workshop Follow-up

Send students:
- Link to official ADK docs
- Sample agent gallery
- Evaluation framework resources
- Deployment guides (Cloud Run, GKE)
- Community channels

Encourage them to:
- Build their own project
- Share capstone work
- Contribute to community
- Join ADK community discussions

---

## Feedback Collection

After Day 1:
- What was clearest?
- What needs more explanation?
- Pacing okay?
- Technical issues?

After Day 2:
- Most valuable section?
- Ready to build your own?
- What would you change?
- Would you recommend to a colleague?

Use feedback to improve next workshop!
