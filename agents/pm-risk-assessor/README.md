# PM Risk Assessor Agent

**Status:** Design Phase (Q4 2025)  
**Purpose:** Identify data governance and execution risks before teams scale analytics, dashboards, or agentic AI systems.

---

## Overview

The PM Risk Assessor translates lessons from scaling mission-critical programs into structured questions and checks. It helps senior PMs and program leaders surface governance gaps, taxonomy failures, and audit readiness issues early—before they become scaling blockers.

This agent bridges the gap between strategic frameworks and practical implementation. It doesn't just automate checklists. It asks the right questions at the right time, informed by patterns from real-world program execution.

---

## Why This Agent Exists

Most organizations rush to implement AI tools or scale analytics without addressing foundational questions:

- Do we have shared taxonomies across partners and systems?
- Who owns this data, and what are our retention obligations?
- How will we demonstrate audit readiness to funders or regulators?
- What happens when feeder patterns (student pipelines, customer journeys, supply chains) cross organizational boundaries?

These aren't theoretical concerns. They're execution gaps that create fragile metrics, compliance risk, and failed scaling attempts. The PM Risk Assessor makes these gaps visible before deployment.

---

## Agent Capabilities (Planned)

### **Risk Prioritization**
- Evaluates risks across competing priorities using structured frameworks
- Identifies which governance gaps pose immediate threats vs. future concerns
- Surfaces hidden dependencies between systems, partners, and data flows

### **Data Governance Readiness**
- Assesses taxonomy standardization across programs and partners
- Validates ownership, privacy controls, and retention policies
- Checks alignment with regulatory requirements (FERPA, GDPR, industry standards)

### **Audit and Validation Checks**
- Determines external validation readiness (certifications, third-party reviews)
- Identifies documentation gaps that would block audits or compliance reviews
- Maps required evidence to actual availability

### **Stakeholder Alignment**
- Surfaces misalignment between technical teams, leadership, and partners
- Validates that success criteria are measurable and agreed upon
- Identifies communication gaps that could derail execution

---

## Foundational Case Study

This agent is informed by real-world experience scaling education programs under strict governance constraints:

**[Read the full case study: Data Governance Foundation for a STEM Pipeline →](case-vp-stem-data-foundation.md)**

### Key Lessons Embedded in Agent Design:

1. **Growth without shared taxonomies creates hidden risk**  
   Surveys in silos, inconsistent labels, partner misalignment—these patterns recur across industries.

2. **Pipeline patterns must be designed up front**  
   Feeder patterns (K-12 to workforce, customer acquisition to retention) can't be retrofitted after systems ship.

3. **External validations test real maturity**  
   State approvals, outcomes certifications, and audit readiness aren't badges—they're practical tests of governance strength.

4. **Quantifiable outcomes prove the framework works**  
   30K→45K students, $600K+ grants, third-party certifications—measurable results from governed data flows.

---

## Implementation Roadmap

### **Q4 2025: Foundation & Design**
- ✅ Case study documentation complete
- 🔄 Agent requirements gathering
- 🔄 Framework design: risk matrices, governance checklists, validation prompts
- ⏳ Initial agentic workflow prototyping

### **Q1 2026: Prototype Development**
- Agent implementation using Claude API
- Integration with playbook frameworks from [Cross-Industry PM Playbook](https://github.com/AliciaMMorgan/cross-industry-pm-playbook-ai-transformation)
- Testing with sample scenarios from case studies

### **Q2 2026: Pilot Testing**
- Real-world validation with organizations scaling analytics/AI
- Refinement based on user feedback
- Documentation of common risk patterns surfaced

---

## How This Agent Differs from Task Automation

**Task automation** handles known processes: generating compliance reports, scheduling reviews, routing approvals.

**The PM Risk Assessor** handles ambiguity:
- Evaluating which risks matter most when resources are constrained
- Identifying governance gaps that aren't obvious from checklists
- Asking questions teams don't know to ask until problems emerge
- Adapting prompts based on industry context, regulatory environment, and organizational maturity

It's the difference between executing a workflow and exercising judgment informed by cross-industry patterns.

---

## Related Resources

- **[Cross-Industry PM Playbook](https://github.com/AliciaMMorgan/cross-industry-pm-playbook-ai-transformation)** - Foundational frameworks this agent operationalizes
- **[Innovation in Action Repository](https://github.com/AliciaMMorgan/Innovation-In-Action)** - Additional case studies and future agents
- **[Case Study: STEM Data Governance](case-vp-stem-data-foundation.md)** - Real execution experience informing agent design

---

## Contributing & Feedback

This is an active development project. If you're a PM, program leader, or technologist working on similar challenges, I'd welcome your input:

- What governance gaps do you encounter most frequently?
- What questions would help surface risks earlier?
- What patterns from your industry should inform the agent's logic?

Open an issue or reach out via [GitHub](https://github.com/AliciaMMorgan).

---

*Part of the Innovation in Action repository demonstrating agentic workflows for traditional organization transformation.*  
*© 2025 Alicia M. Morgan | Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*


---

