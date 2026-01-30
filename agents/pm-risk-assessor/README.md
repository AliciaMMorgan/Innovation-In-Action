# PM Risk Assessor Agent

[![PM Risk Assessor](https://img.shields.io/badge/PM%20Risk%20Assessor-Prompts%20Live-blue?style=for-the-badge&logo=ai&logoColor=white)](prompts/)
[![NIST Aligned](https://img.shields.io/badge/NIST-AI%20RMF%20Governance-green?style=flat-square&logo=nist)](https://www.nist.gov/itl/ai-risk-management-framework)
[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey?style=flat&logo=creativecommons)](https://creativecommons.org/licenses/by/4.0/)

**Status:** Prompt Library Available (Dec 2025) | Agent workflow MVP (Playground validation – Jan 2026)  
**Purpose:** Identify data governance and execution risks before teams scale analytics, dashboards, or agentic AI systems.

---

## 🚀 Use It Now: Prompt Library

**The PM Risk Assessor is available today as a structured prompt library.**

No API costs. No infrastructure. Works with Claude, ChatGPT, Gemini, Copilot, or Perplexity.

**→ Go to Prompt Library**  
[prompts/](prompts/)

Five prompts covering:

1. Initial Risk Assessment  
2. Data Governance Audit  
3. Pipeline Pattern Analysis  
4. Audit Readiness Check  
5. Stakeholder Alignment Diagnostic  

**→ See real example: STEM Museum Assessment**  
https://github.com/AliciaMMorgan/Innovation-In-Action/blob/main/agents/pm-risk-assessor/case-vp-stem-data-foundation.md

---

## Overview

The PM Risk Assessor translates lessons from scaling mission-critical programs into structured questions and checks. It helps senior project, program, and portfolio leaders surface governance gaps, taxonomy failures, and audit readiness issues early — before they become scaling blockers.

This agent bridges the gap between strategic frameworks and practical execution. It does not automate delivery work. It operationalizes judgment — asking the right governance and execution questions at the right moment, based on recurring patterns observed across multiple industries and organizational environments.

---

## Why This Agent Exists

Organizations often move quickly to implement analytics platforms, dashboards, or AI-enabled tooling without resolving foundational execution and governance questions:

- Do we have shared taxonomies across teams, partners, and systems?
- Who owns this data and what are our retention, privacy, and usage obligations?
- How will audit readiness be demonstrated when external reviewers or funders request evidence?
- What happens when pipelines (student journeys, customer journeys, supply chains, or service pathways) cross organizational and system boundaries?

These are not theoretical concerns. They are execution risks that routinely appear only after scale begins — when remediation is slow, expensive, and politically complex.

The PM Risk Assessor was created to surface these risks early, while corrective action is still feasible.

---

## Current Capabilities  
*(Prompt Library – Dec 2025)*

### Risk prioritization

Evaluates risk across:

- taxonomy and definitions
- data ownership and stewardship
- pipeline and feeder pattern integrity
- audit readiness
- stakeholder alignment

The intent is to help teams focus attention on risks that actually block scale — not generic checklist items.

---

### Data governance readiness

Assesses:

- taxonomy standardization
- ownership clarity
- privacy and access controls
- documentation and evidence gaps

Surfaces governance weaknesses before they become compliance or funding barriers.

---

### Audit and validation checks

Identifies what evidence, documentation, or process artifacts cannot currently be produced — but will be requested during audits, certifications, or formal reviews.

---

### Stakeholder alignment diagnostics

Makes implicit assumptions explicit.

Highlights where leaders believe alignment exists but decision rights, priorities, or risk tolerances differ in practice.

---

### Pipeline and dependency analysis

Maps cross-boundary flows and dependencies.

Identifies where handoffs, system integrations, or organizational boundaries create fragility and blind spots.

---

## Planned Capabilities  
*(Original full agent concept)*

### Interactive assessment

- Agent asks follow-up questions based on responses
- Adapts to industry context and regulatory environment
- Produces context-aware governance and execution guidance

---

### Risk scoring

- Quantified risk levels
- Prioritization by likelihood, impact, and remediation complexity
- Trend tracking as improvements are implemented

---

### Documentation generation

- Audit-ready assessment summaries
- Governance and ownership documentation
- Structured evidence requests

---

### Framework integration

- Connects to the Cross-Industry PM Playbook
- Leverages real case examples and patterns

---

## Foundational Case Study

This work is grounded in real delivery and governance execution.

**Data Governance Foundation for a STEM Pipeline**  
https://github.com/AliciaMMorgan/Innovation-In-Action/blob/main/agents/pm-risk-assessor/case-vp-stem-data-foundation.md

### Key lessons embedded in the design

1. Growth without shared taxonomies creates hidden operational and audit risk  
2. Pipeline patterns must be designed before systems are scaled  
3. External validations reveal real governance maturity  
4. Quantifiable outcomes validate disciplined execution

---

## Implementation Roadmap

### ✅ Q4 2025 – Prompt Library (Complete)

- Five core assessment prompts
- Sample assessment from a real STEM governance case
- Documentation and usage guidance
- Tool-agnostic execution across conversational AI platforms

---

### 🔄 Q1 2026 – Agent workflow MVP (Playground validation)

- Workflow-based execution tested in Microsoft Foundry playground
- PM Risk Assessor logic invoked through an orchestration surface
- Cross-industry scenarios executed in preview mode
- Operational, governance, and execution behavior observed

*This phase is intentionally exploratory and not a production deployment.*

---

### ⏳ Future – Platform-agnostic agent execution (directional)

- Continued experimentation in multiple enterprise platforms
- Validation of governance, execution, and lifecycle behavior
- No platform commitment implied

---

## 🔄 Design Rationale & Learning Log  
*(Direction update – January 30, 2026)*

When this project began, the primary delivery strategy for the PM Risk Assessor was to publish high-quality prompts and allow practitioners to run them inside their preferred AI tools.

That approach intentionally emphasized:

- accessibility
- zero infrastructure cost
- and broad reach across ChatGPT, Gemini, Copilot, Claude, and Perplexity

This led to the PM Risk Assessor cross-tool demonstration, where identical scenarios were executed across five AI tools to compare how different models frame governance and execution risk.

---

### Original assumption

The initial assumption was that broad prompt distribution would be the best way to validate real-world usefulness.

In practice:

- practitioner feedback arrived slowly and inconsistently
- it was difficult to observe how governance and operational realities appear when the logic is embedded into real delivery environments

---

### What changed

Through:

- live presentations to project and program management professionals
- structured Q&A during those sessions
- and feedback from leaders responsible for delivery and governance

it became clear that the greater value lies in observing how this assessment logic behaves when placed inside enterprise execution and orchestration environments.

---

### Foundry playground MVP

On January 30, 2026, a deliberate decision was made to validate the PM Risk Assessor inside a workflow environment using Microsoft Foundry’s playground.

The goal was not to build a production agent.

The goal was to learn:

- how assessment logic behaves when orchestrated
- how user input and state management behave
- how execution errors surface
- how lifecycle and change controls become visible
- and how governance and accountability concerns emerge when an agent is no longer only a prompt

The workflow was intentionally minimal:


All scenarios were executed in preview mode.

---

### What the playground revealed

Running the PM Risk Assessor inside a workflow surfaced operational realities not visible in prompt-only testing:

- unhandled question and state errors
- input binding and conversation context issues
- model availability and regional deployment constraints
- execution and validation differences between chat and orchestration environments
- early visibility into logging, lifecycle, and governance concerns

This confirmed that the future value of this work is not limited to assessment logic, but also includes how that logic integrates into delivery and governance ecosystems.

---

### Relationship to the multi-model comparison work

The original cross-tool experiments remain foundational.

The PM Risk Assessor was intentionally executed across:

- ChatGPT
- Claude
- Gemini
- Copilot
- Perplexity

Those experiments revealed consistent differences in:

- executive framing
- research depth
- regulatory emphasis
- operational and technical detail
- stakeholder and change perspectives

This demonstrated that the assessment structure itself is portable and resilient across vendors.

The Foundry playground work builds on that foundation by validating execution context rather than model behavior.

---

### Why this direction is now preferred

Based on practitioner feedback and sandbox experimentation, this project now prioritizes:

- embedding assessment logic into delivery and governance workflows
- validating operational and organizational friction early
- learning how different enterprise platforms shape agent behavior

This approach strengthens the original prompt strategy rather than replacing it.

---

### Important clarification

The Foundry work represents a sandbox MVP only.

It does not represent:

- a platform commitment
- a production architecture
- or a finalized agent design

The final form of a deployable PM Risk Assessor agent will be informed by continued experimentation across multiple enterprise platforms.

---

### Forward view (high-level only)

The broader learning objective is to understand how assessment and agentic workflows behave across commonly adopted enterprise ecosystems, including:

- Microsoft Foundry
- AWS Bedrock
- Google Gemini / Workspace environments

These platforms were selected because they represent practical enterprise availability and hands-on access.

No future platform commitments are implied.

---

## How This Differs from Task Automation

Task automation executes known steps.

The PM Risk Assessor operates in ambiguity:

- determining which risks matter most when resources are constrained
- identifying governance and ownership gaps not visible in checklists
- exposing assumptions before scale
- adapting questioning based on industry and organizational maturity

It is designed to support judgment, not replace it.

---

## Get Started

### Option 1 – Use the prompt library

[prompts/](prompts/)

---

### Option 2 – Review a real assessment

https://github.com/AliciaMMorgan/Innovation-In-Action/blob/main/agents/pm-risk-assessor/prompts/01-initial-risk-assessment.md

---

### Option 3 – Build on this work

All content is licensed under CC BY 4.0.

---

## Related Resources

- Cross-Industry PM Playbook  
  https://github.com/AliciaMMorgan/cross-industry-pm-playbook-ai-transformation

- Innovation in Action repository  
  https://github.com/AliciaMMorgan/Innovation-In-Action

---

*Part of the Innovation in Action program exploring agentic workflows for cross-industry organizational transformation.*  
*© 2025–2026 Alicia M. Morgan – Licensed under CC BY 4.0*

