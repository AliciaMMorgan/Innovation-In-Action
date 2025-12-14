# Pipeline Pattern Analysis

## Purpose
Identify where people, data, or resources flow across organizational boundaries, systems, or life stages. Surface dependencies and handoff risks before they block scaling.

## When to Use
- Designing programs that span multiple organizations or life stages
- Building analytics across customer/student/patient journeys
- Scaling initiatives that depend on cross-functional coordination
- When outcomes in one place depend on inputs from another

## Why This Matters
"Feeder patterns" or "pipelines" create hidden dependencies. Students move from elementary to high school. Customers progress from trial to paid. Patients transition from primary care to specialists. When these transitions cross organizational boundaries, governance gaps emerge. This prompt makes those dependencies visible.

---

## Copy This Prompt Into Your AI Tool
```
You are a systems analyst specializing in pipeline patterns and cross-boundary flows. Map the critical dependencies and handoff risks in our initiative.

**Our Pipeline/Pattern:**
[Describe the flow: Where do people/data/resources start? Where do they end? What stages exist between?]

Example formats:
- Student pipeline: Elementary → Middle → High School → College → Workforce
- Customer journey: Awareness → Trial → Paid → Renewal → Advocacy
- Patient pathway: Screening → Diagnosis → Treatment → Follow-up
- Supply chain: Supplier → Manufacturing → Distribution → Customer

**Organizational Boundaries:**
[Which stages are owned by different teams, partners, or organizations?]

**Current State:**
- How many people/items move through this pipeline annually? [volume]
- What data follows them across stages? [what gets tracked]
- Where do handoffs occur? [transitions between owners]
- What breaks most often? [known failure points]

**Analysis Framework:**

1. **Dependency Mapping**
   - Which stages depend on data or actions from prior stages?
   - What happens if upstream stages change their processes?
   - Are there circular dependencies?

2. **Boundary Risks**
   - Where does the pipeline cross organizational lines?
   - How is accountability managed at handoff points?
   - What governance mechanisms exist for shared decisions?

3. **Data Continuity**
   - Can you track individuals across all stages?
   - Are identifiers, categories, or measures consistent?
   - Where does data get lost or transformed?

4. **Bottleneck Analysis**
   - Which stage has the lowest capacity?
   - Where do delays or drop-offs occur most frequently?
   - What would break if volume doubled?

5. **Outcome Validation**
   - Can you measure end-to-end success?
   - How long before you know if early stages worked?
   - Are there feedback loops to improve upstream stages?

**Output Format:**

For each critical dependency or risk:
- **Stage/Handoff**: Where in the pipeline
- **Dependency Description**: What relies on what
- **Boundary Type**: Internal / Partner / External org
- **Risk Level**: Critical / High / Medium / Low
- **Failure Mode**: What breaks if this dependency fails
- **Current Controls**: What exists to manage this risk (if anything)
- **Gap**: What's missing
- **Recommendation**: Specific governance mechanism needed

Also provide:
- **End-to-End Flow Diagram**: Text-based visualization of the pipeline
- **Top 3 Bottlenecks**: Where capacity limits scaling
- **Quick Wins**: Fast improvements to strengthen handoffs
```

---

## How to Use This Prompt

1. **Map your pipeline first**
   - List all stages from start to finish
   - Identify which organizations own each stage
   - Note where handoffs occur

2. **Gather failure stories**
   - What went wrong in past scaling attempts?
   - Where do you lose people/data/tracking?
   - When have partners/teams blamed each other?

3. **Run the prompt with specific details**
   - Include actual volume numbers
   - Name the organizations involved
   - Describe existing coordination mechanisms (or lack thereof)

4. **Use output to design governance**
   - Which dependencies need formal agreements?
   - Where do you need shared taxonomies?
   - What metrics should be tracked end-to-end?

## Common Patterns This Prompt Surfaces

**Cross-Organizational Gaps:**
- No shared definitions of "success" across pipeline stages
- Data handoffs via email or spreadsheets (not systems)
- Unclear accountability when outcomes fail

**Tracking Failures:**
- Can't connect early-stage participants to later outcomes
- Identifiers change at organizational boundaries
- No longitudinal view of pipeline effectiveness

**Bottlenecks:**
- One stage operates at much smaller capacity than others
- Manual processes that don't scale with volume
- Approval gates that slow the entire pipeline

---

## Related Prompts

- **[Initial Risk Assessment](01-initial-risk-assessment.md)** - High-level scan before deep dive
- **[Data Governance Audit](02-data-governance-audit.md)** - Examine taxonomy across pipeline stages
- **[Stakeholder Alignment](05-stakeholder-alignment.md)** - Surface misalignment between pipeline owners

---

## Real-World Example

In the STEM museum case study, the pipeline analysis revealed:
- Students moved through elementary → middle → high school → college/workforce
- Each stage involved different school districts and organizations
- No consistent tracking of student outcomes across the full pipeline
- Limited visibility into whether early STEM exposure influenced later career choices

Building shared taxonomies and governed data flows enabled longitudinal tracking and demonstrated impact across the entire pipeline.

See **[Sample Assessment: STEM Museum Case](../examples/sample-assessment-stem-museum.md)** for detailed output.

---

*Part of the PM Risk Assessor prompt library*  
*Based on lessons from scaling mission-critical programs under governance constraints*
