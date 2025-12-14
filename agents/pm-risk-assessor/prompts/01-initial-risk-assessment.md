# Initial Risk Assessment

## Purpose
Surface high-level governance and scaling risks before diving into detailed analysis. Use this at the start of any analytics, dashboard, or AI initiative.

## When to Use
- Beginning a new program or technology initiative
- Scaling existing systems or partnerships
- Post-mortem on stalled or failed implementations
- Before requesting funding or executive approval

## Background Context
This prompt is based on patterns from scaling education programs from 30K to 45K+ students while maintaining audit readiness and securing $600K+ in grants. The same patterns appear across industries when organizations scale without addressing foundational governance.

---

## Copy This Prompt Into Your AI Tool
```
You are a senior PM risk assessor specializing in data governance and program scaling. I need you to identify critical risks before we proceed with this initiative.

**Our Initiative:**
[Describe your project: what you're building, scaling, or implementing]

**Current State:**
- Scale: [number of users/students/customers/transactions]
- Data sources: [list systems, surveys, platforms involved]
- Partners/stakeholders: [internal teams, external orgs, vendors]
- Timeline: [launch date, growth targets, constraints]
- Success metrics: [how you'll measure success]

**Analyze through these five lenses:**

1. **Taxonomy & Standards**
   Are definitions, categories, and measurement scales consistent across all systems and partners?
   Can you compare data across programs, time periods, or organizational boundaries?

2. **Data Ownership & Privacy**
   Who owns each data asset? Are retention policies, privacy controls, and legal obligations clear?
   What happens when data crosses organizational boundaries?

3. **Pipeline Patterns**
   How do people or data move across stages, systems, or organizations?
   Are there "feeder patterns" where outcomes in one place depend on inputs from another?

4. **Audit Readiness**
   What documentation exists to prove compliance, outcomes, or governance practices?
   Could you pass an external audit or certification review today?

5. **Stakeholder Alignment**
   Do technical teams, leadership, partners, and end-users agree on success criteria?
   Are there hidden assumptions or misaligned expectations?

**Output Format:**
For each risk area, provide:
- **Risk Name**: Brief, specific title
- **Category**: Which of the 5 lenses above
- **Likelihood**: High/Medium/Low
- **Impact**: High/Medium/Low (if unaddressed)
- **Evidence**: What indicates this risk exists
- **Next Step**: One concrete action to validate or mitigate

Prioritize the top 5 risks overall. Focus on risks that will get worse as you scale.
```

---

## How to Use This Prompt

1. **Copy the entire prompt** from the code block above
2. **Paste into Claude, ChatGPT, or your preferred AI tool**
3. **Fill in your specific context** (replace the bracketed placeholders)
4. **Review the output** - Does it surface risks your team hasn't discussed?
5. **Share with stakeholders** - Use as conversation starter for governance planning

## What Good Output Looks Like

The AI should identify:
- Specific risks (not generic "data quality issues")
- Evidence-based concerns (pointing to your context)
- Actionable next steps (not just "develop a plan")
- Prioritization based on likelihood + impact
- Cross-functional implications

## Red Flags in Output

If the AI returns vague or generic advice:
- Add more specific details about your systems and stakeholders
- Include examples of past failures or near-misses
- Specify your industry, regulatory environment, or compliance requirements

---

## Related Prompts

- **[Data Governance Audit](02-data-governance-audit.md)** - Deep dive on taxonomy, ownership, privacy
- **[Pipeline Pattern Analysis](03-pipeline-pattern-analysis.md)** - Examine cross-boundary flows
- **[Audit Readiness Check](04-audit-readiness-check.md)** - Documentation and compliance gaps
- **[Stakeholder Alignment](05-stakeholder-alignment.md)** - Surface hidden misalignment

---

## Example Output

See **[Sample Assessment: STEM Museum Case](../examples/sample-assessment-stem-museum.md)** for a real example of this prompt applied to a 30K→45K student scaling initiative.

---

*Part of the PM Risk Assessor prompt library*  
*Based on lessons from scaling mission-critical programs under governance constraints*
