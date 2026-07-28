# GitHub Copilot Chat Assistant

This document organizes repository patterns into a concise GitHub-friendly matrix using the provided seven-pattern AI capability taxonomy.

## Canonical seven AI patterns

1. Recognition (perception, classification, extraction)
2. Conversational / Human Interaction (dialogue, assistants)
3. Predictive Analytics & Decision Support (forecasting, recommendations)
4. Generative Content (text, image, code generation)
5. Optimization & Automation (planning, orchestration, process automation)
6. Anomaly Detection & Security (threats, robustness)
7. Knowledge Retrieval & Reasoning (RAG, grounding, long-context reasoning)

## Repository pattern mapping

| Pattern | Why (evidence from this repo) | AI tools that can enhance or automate work | Mapped AI pattern(s) |
|---|---|---|---|
| Agent-based advisory / Domain-specific copilots | The PM Risk Assessor prototype and agent materials (`agents/pm-risk-assessor`, `ai-agent-q1-2026`) show an agent encoding PM rules, stage-aware guidance, and scenario tests. | Azure AI Foundry; Copilot Studio; ChatGPT Enterprise; RAG stacks such as Azure Cognitive Search, LlamaIndex, and LangChain; agent QA frameworks | Conversational / Human Interaction; Knowledge Retrieval & Reasoning; Generative Content |
| Stage-aware decision support (adoption lifecycle) | `README` and `ai-agent-q1-2026` emphasize stage confusion, evidence ladders, and stage-aware guidance for pilot-to-scale transitions. | Workflow automation such as Power Automate and Azure Logic Apps; decision-support agents; dashboards such as Power BI; policy engines | Predictive Analytics & Decision Support; Optimization & Automation; Knowledge Retrieval & Reasoning |
| Governance, compliance & risk mapping | `cyber-ai-profile`, NIST AI RMF references, and `responsible-ai-usage.md` stress control mappings, GRC integration, and NIST alignment. | Policy-as-code such as OPA; compliance scanners; Microsoft Responsible AI toolkits; SBOM tools; GitHub Actions gating | Anomaly Detection & Security; Knowledge Retrieval & Reasoning; Recognition (classification of controls and risks) |
| Human-in-the-loop review & accountability | The repository repeatedly stresses human responsibility, review, and acceptance tests; human checkpoints are built into agent validation. | Annotation UIs such as Label Studio; review queues in Teams or Jira; explainability tools such as InterpretML; HITL workflow automation | Conversational / Human Interaction; Knowledge Retrieval & Reasoning; Optimization & Automation |
| Knowledge-grounding & cross-ecosystem integration | References to SharePoint, OneDrive, prompt libraries, and structured artifacts imply reuse of knowledge-management assets to ground agents (`prompts/`, `frameworks/`). | Vector databases such as Pinecone; Azure Cognitive Search; connectors to SharePoint or Confluence; RAG pipelines using LangChain or LlamaIndex | Knowledge Retrieval & Reasoning; Recognition (entity extraction); Conversational / Human Interaction |
| Reporting, measurement & evidence translation | `README` suggests Power BI risk heatmaps, CSV exports, Evidence Ladder, and notebooks for benchmarking. | ETL tooling such as Azure Data Factory; Power BI dashboards; Jupyter notebooks; AutoML; anomaly detection | Predictive Analytics & Decision Support; Optimization & Automation; Recognition (metric classification and labeling) |
| Prompt engineering & reproducible enablement artifacts | The repository includes a prompt library, templates, examples, and suggested artifact workflows for reuse and governance. | PromptLayer; prompt versioning in Git; CI for prompts using GitHub Actions; prompt testing frameworks | Generative Content; Conversational / Human Interaction; Knowledge Retrieval & Reasoning |

## Notes

- This version keeps the provided canonical taxonomy unchanged.
- The table wording is tightened for readability in GitHub Markdown while preserving the original intent.
- File and folder references remain in inline code for easier scanning in repository documentation.

## Possible next edits

- Re-map the table to a different canonical seven-pattern taxonomy.
- Add explicit file and line references for each evidence statement.
- Split the matrix into "repository evidence" and "recommended tooling" sections for presentation use.
