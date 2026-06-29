# Capstone Option 3: Support Triage Agent

## Overview
A coordinator agent that triages support requests and routes them to appropriate specialist agents.

## The Pattern: Intelligent Routing

```
User Request
     ↓
 Coordinator (classifies)
     ↓
   ┌─┴─┬─────────┬────────┐
   ↓   ↓         ↓        ↓
Tech  Billing  General  ...
```

## Specialist Agents

### Technical Support
Handles:
- Bug reports
- Error messages
- Troubleshooting
- Performance issues

### Billing Support
Handles:
- Invoice questions
- Payment issues
- Refund requests
- Subscription changes

### General Support
Handles:
- How-to questions
- Feature explanations
- Product information
- Best practices

## How to Run
```bash
adk web capstone_option3_support_triage
```

## Try It
Ask different types of questions:
- "My app is crashing when I click submit" (→ Technical)
- "Why was I charged twice this month?" (→ Billing)
- "How do I export my data?" (→ General)

Watch how the coordinator:
1. Understands the request
2. Classifies the issue type
3. Routes to the right specialist
4. Summarizes the response

## Why This Pattern?

**Specialization Benefits:**
- Each agent has focused expertise
- Clearer instructions
- Better quality responses
- Easier to test and improve

**Scalability:**
- Add new specialists easily
- No need to retrain the coordinator
- Each specialist can have its own tools

**Better User Experience:**
- Faster routing to the right help
- Consistent responses by category
- Clear escalation paths

## Real-world Applications
- Customer support systems
- IT helpdesk
- Healthcare triage
- Legal consultation routing
- Educational tutoring systems

## Implementation Notes

This example shows the conceptual pattern. To make it fully functional with actual sub-agent delegation, you would:

1. Use the coordinator to classify the request
2. Have the coordinator explicitly call the appropriate sub-agent as a tool
3. Return the specialist's response

Alternatively, use a more sophisticated routing mechanism where the coordinator has the sub-agents as actual delegatable agents (not just tools).

## Extension Ideas
- Add priority classification (urgent/normal/low)
- Track which specialists are busiest
- Route based on specialist availability
- Add escalation paths (tier 1 → tier 2 → engineering)
- Include sentiment analysis for upset customers
- Multi-language support routing
