import os
import google.cloud.logging

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools import AgentTool
from google.genai import types

from .callback_logging import log_query_to_model, log_model_response

# Import your sub-agents
from .sub_agents.search_agent.agent import search_agent
from .sub_agents.connors_agent.agent import cleaning_agent
from .sub_agents.petmates_agent.agent import petmates_agent


# Import your existing tools
from .tools import set_session_value

load_dotenv()

# Resilience configuration
RETRY_OPTIONS = types.HttpRetryOptions(initial_delay=1, max_delay=3, attempts=30)

# Configure logging to the Cloud
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

root_agent = Agent(
    name='root_agent',
    model=Gemini(model=os.getenv("MODEL", "gemini-1.5-flash"), retry_options=RETRY_OPTIONS),
    description='A helpful concierge assistant for Buni services.',
    instruction="""
    ""
    You are the primary orchestrator for Buni services.
    - Route cleaning-related inquiries to the 'cleaning_agent'.
    - Route general information, FAQs, and policy questions to the 'search_agent'.
    - You do not handle refunds or quotes directly; delegate these to `petmates_agent`.
    - If a user request falls outside these domains, politely inform them you cannot assist.
    """,
    before_model_callback=log_query_to_model,
    after_model_callback=log_model_response,
    sub_agents=[cleaning_agent, petmates_agent],
    # Integrating search_agent as a tool makes it callable by the root_agent
    tools=[
        set_session_value,
        AgentTool(search_agent, skip_summarization=False)
    ]
)

if __name__ == "__main__":
    # You can now test the root agent directly
    print("Root agent initialized and ready.")