# SPEC: Buni Agents (Omni-Concierge Platform)

## 1. Project Overview
**Buni Agents** is a stateful, multi-agent concierge platform designed to handle customer inquiries across two domains: **PetMates** (support) and **Conor’s Cleaning** (service/pricing). The architecture leverages a "Hub & Spoke" model, utilizing a lean root orchestrator to manage state and route tasks to domain-specific tools.

## 2. Architecture: "Hub & Spoke"
* **Root Orchestrator (`agent.py`)**: The primary interface. It performs intent classification and tool selection without the need for a separate orchestration file.
* **Tools Layer (`tools.py`)**: Contains pure functions for capabilities:
    * `calculate_cleaning_price`: Pricing engine for service tiers.
    * `process_refund`: Secure transaction logic with internal verification.
    * `verify_customer_status`: Private helper function used as the "Muscle" for access control.
* **Verification Layer**: A "Verify-Before-Act" pattern where `process_refund` invokes `verify_customer_status` to ensure authorization before execution.

## 3. Core Functional Requirements
* **Stateful Memory**: Managed via ADK; maintains context during transitions between PetMates and Conor’s Cleaning inquiries.
* **Grounding**: All responses must be derived from:
    * *PetMates Customer Support Handbook*[cite: 1]
    * *Conor's Cleaning - Knowledge Base Document (1).docx*[cite: 2]
* **Security & Guardrails**: The agent must strictly gate sensitive tools (refunds) behind a customer status verification check.
* **Domain Isolation**: The root orchestrator is instructed to reject queries unrelated to the two supported business domains.

## 4. Technical Stack
* **Framework**: Google Agent Development Kit (ADK).
* **Runtime/LLM**: Vertex AI Agent Engine with `gemini-2.5-flash`.
* **Dependency Management**: `uv` and `pyproject.toml` for fast, reproducible environment builds.
* **Version Control**: GitHub (managed via Git, with `uv.lock` and `.python-version` committed for consistency).

## 5. Evaluation Plan (`evalset.json`)
The `evalset.json` file will maintain test cases to prevent knowledge contamination and ensure routing accuracy.

| Test Case | Expected Path |
| :--- | :--- |
| "I need a refund for my pet food order." | `root_agent` -> `process_refund` (with `verify_customer_status` check). |
| "Quote for a 1000sqft deep cleaning." | `root_agent` -> `calculate_cleaning_price(service_tier="Deep", area_sqft=1000)`. |
| "Can I use my PetMates coupon at Conor's?" | `root_agent` (Reject/Clarify). |

## 6. Development Workflow
1. **Project Init**: `adk create buni-agents`.
2. **Env Setup**: `uv init` followed by `uv add google-adk`.
3. **Doc Setup**: `mkdir docs` and `touch docs/SPEC.md`.
4. **Deployment**: Push via `git push`, excluding `.venv/`, `.adk/`, and `.env` while including `uv.lock` and `.python-version`.