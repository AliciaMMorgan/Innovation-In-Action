# Model-Based Reflex Agent

## What is a Model-Based Reflex Agent?
A model-based reflex agent is a system that uses an internal model of the environment to make decisions. Unlike simple reflex agents, which only react to current conditions, model-based reflex agents maintain a memory of the past states, actions, and their effects. This enables them to infer the current state of the environment and respond based on both immediate input and stored knowledge.

## Connection to Project Execution Gaps and Knowledge–Implementation–Trust
This project applies the concept of a model-based reflex agent to address execution gaps in project management. Execution gaps arise when there are mismatches or shortcomings in one or more of these areas:
- **Knowledge (K):** Gaps in understanding or information.
- **Implementation (I):** Challenges in executing tasks or plans.
- **Trust (T):** Issues related to trust among team members or stakeholders.

The agent interprets project inputs such as risks, blockers, and trust issues and provides targeted recommendations to close these gaps. Each recommendation is explicitly labeled by its focus area (K/I/T), helping teams take corrective actions efficiently.

## How to Run the Agent Example

### Prerequisites
Before running the example, make sure you have Python installed on your system.

### Steps
1. Clone the repository and switch to the `model-based-agent` branch:
   ```bash
   git clone https://github.com/AliciaMMorgan/Innovation-In-Action.git
   cd Innovation-In-Action
   git checkout model-based-agent
   ```

2. Review the sample input JSON file (`sample_input.json`) to understand the format of project data:
   ```json
   {
       "risks": ["Incomplete requirements", "Lack of expertise"],
       "blockers": ["Tooling delays", "Resource availability"],
       "trust_issues": ["Low team morale"]
   }
   ```

3. Run the Python script (make sure the input file `sample_input.json` is in the same directory):
   ```bash
   python project_execution_gap_agent.py
   ```

4. Review the output JSON file (`sample_output.json`) for recommendations. Example output:
   ```json
   {
       "recommendations": [
           {
               "classification": "K",
               "label": "Knowledge",
               "recommendation": "Address Incomplete requirements to improve Knowledge"
           },
           ...
       ]
   }
   ```

This demonstrates how the agent takes project data, processes it, and suggests actionable recommendations for closing execution gaps.