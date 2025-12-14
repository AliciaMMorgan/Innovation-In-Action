# Stakeholder Alignment Diagnostic

## Purpose
Surface hidden misalignment between technical teams, leadership, partners, and end-users before it derails execution. Identify where stakeholders think they agree but actually don't.

## When to Use
- Beginning cross-functional or multi-partner initiatives
- When projects stall for "unclear" reasons
- Before major milestones or funding decisions
- After discovering conflicting assumptions late in execution

## Why This Matters
Most programs fail not from technical issues, but from stakeholder misalignment that wasn't visible early. Teams use the same words to mean different things. Success criteria that "everyone agreed to" turn out to mean different outcomes to different groups. This prompt makes implicit assumptions explicit.

---

## Copy This Prompt Into Your AI Tool
```
You are an organizational alignment specialist. Analyze our stakeholder ecosystem for hidden misalignment, conflicting assumptions, and communication gaps that could derail this initiative.

**Initiative Overview:**
[What you're building/scaling/implementing]

**Stakeholder Map:**

**Decision-Makers:**
[Who has authority to approve, fund, or stop the initiative]
- Name/role: [their priorities, constraints]

**Key Influencers:**
[Who doesn't have formal authority but shapes opinions]
- Name/role: [their concerns, interests]

**Implementation Teams:**
[Who does the actual work]
- Team/role: [their capabilities, workload]

**End-Users:**
[Who experiences the outcome]
- Group: [their needs, current pain points]

**Partners/Vendors:**
[External organizations involved]
- Organization: [their incentives, obligations]

**Current State:**
- What "success" has been defined? [stated goals]
- How was success defined? [who was in the room, who wasn't]
- What metrics exist? [how you'll measure progress]
- What's the communication cadence? [how often stakeholders sync]

**Alignment Analysis Framework:**

1. **Definition Alignment**
   - Do all stakeholders use the same definitions for key terms?
   - Example: Does "completion" mean the same thing to all parties?
   - Are success criteria measurable and unambiguous?
   - Where are terms used without clear definitions?

2. **Incentive Alignment**
   - What does each stakeholder gain if this succeeds?
   - What do they lose if it fails?
   - Are incentives aligned or competing?
   - Who has reasons to slow or stop progress?

3. **Timeline Alignment**
   - When does each stakeholder need results?
   - Are timelines realistic given dependencies?
   - Who has conflicting deadlines or priorities?
   - Where is urgency mismatched?

4. **Authority Clarity**
   - Who can make which decisions?
   - Where is authority ambiguous or overlapping?
   - What needs consensus vs. unilateral approval?
   - Who can veto, and under what conditions?

5. **Communication Patterns**
   - Who talks to whom regularly?
   - Where are communication gaps?
   - Are there "shadow" decision-making channels?
   - How is disagreement surfaced and resolved?

**Output Format:**

For each misalignment identified:
- **Misalignment Description**: Specific disconnect between stakeholders
- **Stakeholders Involved**: Who has conflicting views/incentives
- **Type**: Definition / Incentive / Timeline / Authority / Communication
- **Severity**: Critical (blocks progress) / High (slows progress) / Medium (creates friction)
- **Evidence**: What reveals this misalignment
- **Likely Impact**: What happens if not addressed
- **Resolution Path**: How to bring stakeholders into alignment
- **Owner**: Who should lead the alignment conversation

Also provide:
- **Overall Alignment Score**: 1-10 (where 10 is fully aligned)
- **Highest Risk Misalignments**: Top 3 issues most likely to derail the initiative
- **Communication Recommendations**: How to improve stakeholder sync
- **Quick Wins**: Clarifications you can make this week
```

---

## How to Use This Prompt

1. **Map all stakeholders honestly**
   - Include informal influencers, not just org chart roles
   - Note who wasn't consulted but should have been
   - Identify silent stakeholders (those affected but not engaged)

2. **Gather real quotes and behaviors**
   - How do different groups describe the initiative?
   - What language do they use for "success"?
   - Where have miscommunications already occurred?

3. **Run the prompt with specifics**
   - Use actual stakeholder names/roles
   - Include timeline pressures and competing priorities
   - Describe past projects where alignment failed

4. **Use output to design alignment rituals**
   - Which stakeholders need regular sync?
   - Where do definitions need explicit documentation?
   - What decision-making authority needs clarification?

## Common Patterns This Prompt Surfaces

**Definition Drift:**
- "Improved outcomes" means different metrics to different teams
- "Launch" means pilot to tech, full rollout to leadership
- "Data-driven" means dashboards to some, predictive models to others

**Incentive Conflicts:**
- IT wants stability, business wants fast iteration
- Partners prioritize their own metrics over shared goals
- Individual performance incentives misaligned with team success

**Authority Ambiguity:**
- No one knows who can approve changes
- Multiple stakeholders think they have veto power
- Decision-making process not documented

**Communication Gaps:**
- Leadership and implementation teams don't sync regularly
- Partners hear different messages from different contacts
- Bad news doesn't flow upward

---

## Related Prompts

- **[Initial Risk Assessment](01-initial-risk-assessment.md)** - Stakeholder alignment is one of the five risk lenses
- **[Pipeline Pattern Analysis](03-pipeline-pattern-analysis.md)** - Cross-boundary flows require stakeholder alignment
- **[Audit Readiness Check](04-audit-readiness-check.md)** - Partners must understand audit requirements

---

## Real-World Example

In the STEM museum case study, stakeholder alignment challenges included:
- School districts, museum staff, and external evaluators using different definitions of "STEM interest"
- Partners interpreting data ownership and privacy responsibilities differently
- Funders expecting certain metrics while programs tracked different indicators
- Leadership and program managers having different timelines for demonstrating impact

Building explicit alignment on taxonomies, success criteria, and governance responsibilities enabled sustained growth and external validation.

See **[Sample Assessment: STEM Museum Case](../examples/sample-assessment-stem-museum.md)** for detailed output.

---

*Part of the PM Risk Assessor prompt library*  
*Based on lessons from scaling mission-critical programs under governance constraints*
