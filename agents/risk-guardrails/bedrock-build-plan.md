# Bedrock Build Plan

This document maps the Risk Guardrails Agent from workflow definition into staged AWS Bedrock implementation.

## Purpose

The purpose of this build plan is to define how the Risk Guardrails Agent will be implemented in stages using AWS Bedrock and related workflow logic.  
The goal is to preserve governance, source control, accessibility, escalation handling, and final human-in-the-loop approval from the beginning of the build.

## Build principles

- Start with governance and retrieval boundaries before optimization.
- Keep human judgment in the loop for ambiguity, accessibility, narrative fidelity, and release approval.
- Use platform guardrails where possible, but do not treat platform controls as a replacement for human review.
- Build for reusable enterprise workflows rather than one-off demos.
- Preserve clear escalation paths for blockers, stalled work, and unresolved review issues.

## Foundational policy alignment

This implementation assumes the Day 1 operating policy has already been defined.  
That policy establishes approved sources, GRC expectations, accessibility requirements, reviewer roles, escalation logic, and required HITL approval.  
The Bedrock build must align to those controls rather than redefine them.

## Stage 1: Intake and scope

**Goal:** Capture the request before generation begins.

### Inputs
- User or stakeholder request
- Intended audience
- Business purpose
- Requested output type
- Known constraints or deadlines

### Outputs
- Intake summary
- Scope classification
- Initial routing recommendation

### Questions
- What is being requested?
- Who is the audience?
- Is the request informational, operational, public-facing, or decision-support related?
- Does the request involve sensitive content, organizational narrative, or accessibility implications?

## Stage 2: Source boundaries

**Goal:** Confirm that the workflow only uses approved sources.

### Checks
- Approved organizational source list exists
- Retrieval boundaries are defined
- External retrieval is blocked unless explicitly allowed
- Source attribution expectations are documented

### Decision
- Proceed if approved source configuration is complete
- Pause for review if source scope is unclear or incomplete

## Stage 3: Risk classification

**Goal:** Classify the level of governance and review needed.

### Risk dimensions
- Source sensitivity
- Compliance exposure
- Accessibility impact
- Narrative fidelity risk
- Delivery or timeline risk
- Stakeholder visibility

### Risk levels
- Low
- Moderate
- High
- Contain or stop

### Result
The workflow assigns a risk level that determines reviewer routing and escalation requirements.

## Stage 4: Reviewer routing

**Goal:** Send work to the correct reviewers based on risk and content type.

### Reviewer groups
- Governance, Risk, and Compliance
- Accessibility review
- Domain or content owner
- Project or product lead
- Final human-in-the-loop approver

### Routing logic
- Low-risk outputs may proceed to domain review and HITL approval
- Moderate-risk outputs require domain review plus additional checks
- High-risk outputs require governance review, accessibility review if applicable, and explicit HITL approval
- Unclear or conflicting cases move to escalation

## Stage 5: Escalation handling

**Goal:** Define what happens when work stalls or unresolved issues remain.

### Escalation triggers
- Missing approved sources
- Unresolved ambiguity
- Accessibility concerns not addressed
- Reviewer disagreement
- Delivery blocker affecting timeline
- Narrative drift from approved organizational context

### Escalation path
1. Clarify blocker
2. Route to project or product lead
3. Route to accountable leadership if unresolved
4. Move to contingency path if delivery risk remains

## Stage 6: Final HITL approval

**Goal:** Require human approval before release or decision use.

### Human approval checks
- Output aligns with approved sources
- Output reflects organizational narrative accurately
- Accessibility concerns were reviewed
- Required reviewers signed off
- Escalation issues are resolved or contained

### Final states
- Approved for build
- Approved for release
- Revise
- Escalate
- Contain or stop

## Bedrock mapping areas

This section identifies the implementation areas that will be mapped in AWS Bedrock.

### Platform-managed controls
- Guardrails configuration
- Topic restrictions
- Content filtering
- Sensitive information controls
- Context grounding configuration
- Invocation boundaries

### Human-managed controls
- Narrative fidelity review
- Accessibility judgment
- Organizational context verification
- Approval for external release
- Escalation decisions for unclear cases

## Initial implementation sequence

### Week 1
- Confirm use cases
- Define required inputs
- Finalize source boundaries
- Draft risk classification logic
- Finalize reviewer routing rules

### Week 2
- Configure Bedrock-aligned guardrail categories
- Map escalation triggers to workflow logic
- Draft test prompts and negative cases
- Validate human review checkpoints
- Prepare v1 implementation notes

## Test scenarios

The first Bedrock-aligned tests should include:

1. Request with approved internal sources only
2. Request missing required organizational context
3. Request with accessibility implications
4. Request that creates reviewer disagreement
5. Request that risks narrative drift
6. Request that must be escalated because of timeline or governance blockers

## Open questions

- Which controls should be enforced directly in Bedrock versus external workflow logic?
- What evidence is required for reviewer sign-off?
- How should accessibility review be documented in the release path?
- What triggers a hard stop versus a revise state?
- What minimum artifacts are 
