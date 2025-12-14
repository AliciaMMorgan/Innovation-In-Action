# Data Governance Audit

## Purpose
Identify taxonomy inconsistencies, ownership gaps, and privacy risks before they create compliance issues or fragile metrics.

## When to Use
- Before integrating data from multiple sources or partners
- When building dashboards that span organizational boundaries
- Preparing for external audits or certifications
- After discovering inconsistent reporting across teams

## Why This Matters
Siloed data with inconsistent labels looks manageable at small scale. But when you try to aggregate, compare across years, or report to external stakeholders, the lack of shared taxonomy creates hidden risk. This prompt surfaces those gaps early.

---

## Copy This Prompt Into Your AI Tool
```
You are a data governance specialist conducting a pre-implementation audit. Analyze our data ecosystem for taxonomy, ownership, and privacy risks that could block scaling or create compliance issues.

**Our Data Ecosystem:**

**Data Sources:**
[List each system, survey, platform, or tool that generates data]
- Source 1: [name, what it captures, who manages it]
- Source 2: [name, what it captures, who manages it]
- etc.

**Data Flows:**
[Describe how data moves between systems, teams, or organizations]

**Key Stakeholders:**
[Who creates, manages, analyzes, or consumes this data]

**Current State:**
- How are categories/labels defined? [consistent taxonomy or varies by source]
- Who decides what data to keep and for how long? [retention policies]
- Are there privacy regulations that apply? [FERPA, GDPR, HIPAA, industry standards]
- Do partners/vendors have access to data? [data sharing agreements]

**Audit Focus Areas:**

1. **Taxonomy Standardization**
   - Are the same concepts measured consistently across all sources?
   - Can you aggregate data without manual recoding or translation?
   - Do response scales, categories, or definitions vary by program/partner?
   - Example: If measuring "student interest," do all surveys use the same scale?

2. **Data Ownership Clarity**
   - Who legally owns each data asset?
   - Are responsibilities for accuracy, security, and retention documented?
   - What happens when staff turnover occurs?
   - Are ownership boundaries clear when data crosses organizational lines?

3. **Privacy & Compliance Controls**
   - What regulations apply to this data? (list them)
   - Are consent processes, access controls, and retention policies documented?
   - Can you demonstrate compliance to an auditor today?
   - Are there agreements with partners about data handling?

4. **Documentation Gaps**
   - Do data dictionaries exist for each source?
   - Are lineage and transformation rules documented?
   - Can a new team member understand the data without institutional knowledge?

**Output Format:**

For each governance gap identified:
- **Gap Description**: Specific issue found
- **Category**: Taxonomy / Ownership / Privacy / Documentation
- **Risk Level**: Critical / High / Medium / Low
- **Evidence**: What in the context reveals this gap
- **Impact on Scaling**: What breaks if you don't fix this
- **Remediation**: Concrete steps to address (not just "create a policy")
- **Quick Win**: Is there a fast partial fix while long-term solution develops?

Prioritize issues that will get exponentially worse as data volume or partner count increases.
```

---

## How to Use This Prompt

1. **Gather your data ecosystem map** before running the prompt
   - List all systems that generate or store data
   - Document current data flows (even informal ones like "exported to spreadsheets")
   - Identify all stakeholders who touch the data

2. **Be specific about your context**
   - Name your industry and applicable regulations
   - Include details about partner relationships
   - Mention any past compliance issues or near-misses

3. **Run the prompt** and review output critically
   - Does it identify gaps your team has discussed but not addressed?
   - Are there surprises? (Those are valuable)

4. **Use output to build governance roadmap**
   - Which gaps block immediate scaling?
   - Which can be mitigated with interim controls?
   - What requires long-term investment?

## Common Patterns This Prompt Surfaces

**Taxonomy Failures:**
- Survey questions that "look similar" but aren't comparable
- Categories that evolved over time without documentation
- Different definitions of success across programs

**Ownership Gaps:**
- "Shared" data with no clear accountability
- Vendor-managed systems with unclear ownership after contract ends
- Cross-functional data where no one has authority to make changes

**Privacy Risks:**
- Data retention longer than legally allowed
- Unclear consent for specific uses
- Partner access without formal agreements

---

## Related Prompts

- **[Initial Risk Assessment](01-initial-risk-assessment.md)** - Start here for high-level scan
- **[Pipeline Pattern Analysis](03-pipeline-pattern-analysis.md)** - Examine how data flows across boundaries
- **[Audit Readiness Check](04-audit-readiness-check.md)** - Prepare for external validation

---

## Real-World Example

In the STEM museum case study, this type of audit revealed:
- Surveys in silos with inconsistent labels
- No unified taxonomy across school partners
- Unclear ownership when museum staff and school district staff both touched data
- Limited ability to track longitudinal impact across the K-12 pipeline

Addressing these gaps enabled growth from 30K to 45K+ students with audit-ready reporting.

See **[Sample Assessment: STEM Museum Case](../examples/sample-assessment-stem-museum.md)** for detailed output.

---

*Part of the PM Risk Assessor prompt library*  
*Based on lessons from scaling mission-critical programs under governance constraints*
