# Audit Readiness Check

## Purpose
Identify documentation gaps and compliance risks that would surface during an external audit, certification, or funder review. Surface issues before they become blockers.

## When to Use
- Preparing for external audits or certifications
- Before applying for grants or major funding
- When partners request compliance evidence
- After discovering documentation gaps during routine reviews

## Why This Matters
Many organizations operate with informal practices that "work fine" until someone asks "prove it." External validations—audits, certifications, funder reviews—test whether governance exists on paper, not just in practice. This prompt reveals gaps before they become crisis moments.

---

## Copy This Prompt Into Your AI Tool
```
You are an external auditor preparing to review our program for compliance, outcomes validation, or certification. Identify documentation gaps and evidence risks that could fail an audit.

**Program Context:**
[Describe what you do: services provided, populations served, scale]

**Audit Trigger:**
[Why are you being audited: grant requirement, certification, regulatory compliance, partner request]

**Applicable Standards/Regulations:**
[List what you need to comply with: FERPA, GDPR, CPE requirements, industry certifications, funder terms]

**Current Documentation:**
[What exists today]
- Policies: [list documented policies]
- Procedures: [standard operating procedures]
- Evidence: [data, records, logs you maintain]
- Agreements: [contracts, MOUs, data sharing agreements]

**Audit Requirements:**

1. **Compliance Documentation**
   - What regulations apply to this program?
   - Are policies documented and dated?
   - Can you prove policies were followed?
   - Are staff trained on compliance requirements?

2. **Outcomes Evidence**
   - What outcomes do you claim to achieve?
   - How do you measure them?
   - Can you produce raw data if requested?
   - Are evaluation methods documented and valid?

3. **Data Management Practices**
   - Are retention schedules documented and followed?
   - Can you demonstrate privacy controls?
   - Are data access logs maintained?
   - How is data backed up and secured?

4. **Operational Records**
   - Can you prove service delivery occurred?
   - Are attendance, participation, or completion records maintained?
   - How long are records kept?
   - Are records stored securely and retrievably?

5. **Partnership Accountability**
   - Are partner responsibilities documented?
   - Do data sharing agreements exist?
   - How are partner deliverables verified?
   - What happens if partners don't meet obligations?

**Output Format:**

For each audit risk:
- **Risk Description**: What an auditor would flag
- **Category**: Compliance / Outcomes / Data Management / Operations / Partnerships
- **Severity**: Critical (fails audit) / High (major finding) / Medium (observation)
- **Missing Evidence**: Specifically what you can't produce today
- **Why It Matters**: Impact if flagged in audit
- **Remediation Timeline**: How long to fix (immediate / weeks / months)
- **Interim Control**: What you can do quickly while long-term fix develops

Also provide:
- **Audit Readiness Score**: Overall assessment (1-10, where 10 is fully ready)
- **Show-Stoppers**: Issues that would fail the audit immediately
- **Quick Wins**: Documentation you can create this week
- **Long-Term Investments**: Systems or practices that need months to implement
```

---

## How to Use This Prompt

1. **Identify your audit scenario**
   - Is this a real upcoming audit or preventive review?
   - What standards apply? (be specific)
   - What has triggered past audit findings? (if any)

2. **Inventory current documentation honestly**
   - Don't overstate what exists
   - Include informal practices that aren't documented
   - Note where you rely on individual knowledge vs. systems

3. **Run the prompt with full context**
   - Name specific regulations or certification requirements
   - Describe your scale (more scale = higher audit scrutiny)
   - Include partner/vendor relationships

4. **Prioritize remediation**
   - Which gaps block immediate audits?
   - Which can be addressed with simple documentation?
   - Which require system changes or policy updates?

## Common Patterns This Prompt Surfaces

**Compliance Gaps:**
- Policies exist but aren't dated or version-controlled
- Staff don't know policies exist
- No evidence policies were actually followed

**Outcomes Validation Issues:**
- Claims of impact without supporting data
- Evaluation methods not documented or validated
- Raw data lost or inaccessible

**Data Management Risks:**
- Retention schedules not followed (keeping too long or too short)
- No audit trails for data access
- Privacy controls assumed but not documented

**Operational Blind Spots:**
- Participation tracked informally (spreadsheets, memory)
- Records not maintained for required retention periods
- No system for producing historical evidence

---

## Related Prompts

- **[Initial Risk Assessment](01-initial-risk-assessment.md)** - Broader risk scan
- **[Data Governance Audit](02-data-governance-audit.md)** - Deep dive on data practices
- **[Stakeholder Alignment](05-stakeholder-alignment.md)** - Ensure partners understand audit requirements

---

## Real-World Example

In the STEM museum case study, audit readiness preparation enabled:
- **State CPE provider approval**: Demonstrated educator trainings met state rules, used qualified facilitators, collected evaluations, and maintained audit-ready documentation for attendance and hours
- **Outcomes certification**: Regional nonprofit validated methodology for collecting, analyzing, and reporting outcomes with proper data governance

These weren't just badges—they were practical tests that proved the governance system could withstand external scrutiny.

See **[Sample Assessment: STEM Museum Case](../examples/sample-assessment-stem-museum.md)** for detailed output.

---

*Part of the PM Risk Assessor prompt library*  
*Based on lessons from scaling mission-critical programs under governance constraints*
