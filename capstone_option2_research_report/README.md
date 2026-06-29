# Capstone Option 2: Research → Report Pipeline

## Overview
A three-stage SequentialAgent pipeline that produces high-quality, fact-checked reports.

## The Pipeline

```
Research → Fact-Check → Write
   ↓           ↓          ↓
 Gather     Verify    Polish
```

### Stage 1: Researcher
- Gathers comprehensive information
- Uses google_search for current data
- Organizes findings systematically

### Stage 2: Fact-Checker
- Verifies key claims
- Flags inconsistencies
- Confirms statistics and sources
- Marks facts as [VERIFIED] or [NEEDS REVIEW]

### Stage 3: Writer
- Creates professional report
- Uses only verified information
- Follows structured format
- Cites sources appropriately

## How to Run
```bash
adk web capstone_option2_research_report
```

## Try It
Ask: "Research and write a report on renewable energy trends"

Watch in the trace:
1. Researcher gathering information
2. Fact-checker verifying claims
3. Writer producing final report

## Why This Pattern?

**Quality Control**: Each agent has one job
- Researcher focuses on gathering
- Fact-checker focuses on accuracy
- Writer focuses on presentation

**Testable**: Test each stage independently

**Reusable**: Use the same researcher for other pipelines

## Report Structure
The final output includes:
- Executive Summary
- Introduction
- Main Findings
- Analysis
- Conclusion
- Any items needing review

## Real-world Applications
- Business intelligence reports
- Market research
- Competitive analysis
- Due diligence
- Academic research summaries

## Customization Ideas
- Add a fourth stage: reviewer/editor
- Include a citation formatter
- Add a data visualization agent
- Create specialized researchers for different domains
