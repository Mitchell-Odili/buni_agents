# Buni Agents

A stateful, multi-agent concierge platform designed to handle customer inquiries across two domains: **PetMates** (support) and **Connor’s Cleaning** (service/pricing).

## Architecture
This project uses a hierarchical delegation model:

* **Root Orchestrator**: Manages high-level routing and intent classification.
* **Specialist Agents**: Encapsulated sub-agents (e.g., `petmates_agent`, `connors_agent`) that manage domain-specific workflows and data collection.
* **Utility Layer**: Dedicated tools (e.g., `coverage_calculator`) that handle specialized math and logic, invoked by specialists as needed.
* **Documentation**: See `docs/SPEC.md` for technical specifications.

## Quick Start
1. **Clone the repo**: `git clone <your-repo-url>`
2. **Install dependencies**: `uv sync`
3. **Run the agent**: `uv run python agent.py`

## Development
- Managed by `uv`.
- Built with Google ADK.