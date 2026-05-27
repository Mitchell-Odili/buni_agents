# SPEC: Buni Agents (Omni-Concierge Platform)

## 1. Project Overview
**Buni Agents** is a stateful, multi-agent concierge platform designed to handle customer inquiries across two domains: **PetMates** (support) and **Conor’s Cleaning** (service/pricing). The architecture has evolved into a **hierarchical delegation model**, utilizing a root orchestrator that delegates tasks to domain-specific sub-agents, which in turn utilize specialized tools for calculation and state management.

## 2. Architecture: "Hub & Spoke"
* **Root Orchestrator (`agent.py`)**: The central entry point. Performs high-level intent classification and routes traffic to the appropriate specialist agent.
* **Specialist Agents (`sub_agents/`)**: Domain-specific modules (e.g., `connors_agent`, `petmates_agent`) that manage conversational flow and data collection for their specific business unit.
* **Utility Layer (`tools.py`)**: Embedded within specialist sub-agents, providing functional primitives (e.g., `calculate_cleaning_price`) that are invoked as needed.
* **Delegation Flow**: Root $\rightarrow$ Specialist $\rightarrow$ Utility Tool.

## 3. Core Functional Requirements
* **Hierarchical State**: State is shared across the hierarchy via the ADK `tool_context`. Data collected by the `connors_agent` (e.g., `SELECTED_PROPERTY`) is persisted for the `coverage_calculator` sub-agent to access during pricing operations.
* **Grounding**: All responses must be derived from:
    * *PetMates Customer Support Handbook*[cite: 1]
    * *Conor's Cleaning - Knowledge Base Document (1).docx*[cite: 2]
* **Security & Guardrails**: The agent must strictly gate sensitive tools (refunds) behind a customer status verification check.
* **Domain Isolation**: Specialist agents are encapsulated, ensuring the **Connor’s Cleaning** logic is decoupled from **PetMates** logic, enabling independent scaling and testing..

## 4. Technical Stack
* **Framework**: Google Agent Development Kit (ADK).
* **Runtime/LLM**: Vertex AI Agent Engine with `gemini-2.5-flash`.
* **Modularity**: Nested directory structure (`sub_agents/`) requiring strict relative import path management.
* **Dependency Management**: `uv` and `pyproject.toml` for fast, reproducible environment builds.
* **Version Control**: GitHub (managed via Git, with `uv.lock` and `.python-version` committed for consistency).

## 5. Evaluation Plan (`evalset.json`)
The `evalset.json` file will maintain test cases to prevent knowledge contamination and ensure routing accuracy.

| Test Case | Expected Path |
| :--- | :--- |
| "I need a refund for my pet food order." | `root_agent` -> `petmates_agent`-> `process_refund` |
| "Quote for a 1000sqft deep cleaning." | `root_agent` -> `connors_agent` -> `calculate_cleaning_price` |
| "Can I use my PetMates coupon at Conor's?" | `root_agent` (Cross-domain routing/Reject). |

## 6. Development Workflow
1. **Project Init**: `adk create buni-agents`.
2. **Env Setup**: `uv init` followed by `uv add google-adk`.
3. **Doc Setup**: `mkdir docs` and `touch docs/SPEC.md`.
4. **Deployment**: Push via `git push`, excluding `.venv/`, `.adk/`, and `.env` while including `uv.lock` and `.python-version`.