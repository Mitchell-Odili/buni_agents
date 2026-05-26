# Buni Agents

A stateful, multi-agent concierge platform for PetMates and Conor's Cleaning.

## Quick Start
1. **Clone the repo**: `git clone <your-repo-url>`
2. **Install dependencies**: `uv sync`
3. **Run the agent**: `uv run python agent.py`

## Architecture
- **Root Orchestrator**: `agent.py` handles routing and state.
- **Capabilities**: Located in `tools/`.
- **Documentation**: See `docs/SPEC.md` for technical specifications.

## Development
- Managed by `uv`.
- Built with Google ADK.