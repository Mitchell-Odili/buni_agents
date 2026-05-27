import os
from google.adk.agents import Agent
from google.adk.models import Gemini

from ...callback_logging import log_query_to_model, log_model_response

# Specialist sub-agents
from .sub_agents.order_agent.agent import order_agent
from .sub_agents.account_agent.agent import account_agent
from .sub_agents.product_promotion_agent.agent import product_promotion_agent
from .sub_agents.policy_support_agent.agent import policy_support_agent

# Utilities
from ...tools import set_session_value, verify_customer_status

petmates_agent = Agent(
    name="petmates_agent",
    model=Gemini(model=os.getenv("MODEL")),
    description="Primary orchestrator for PetMates customer support operations.",
    instruction="""
    You are the PetMates Support Specialist. Your role is to guide users and delegate to 
    the appropriate specialized sub-agent based on the 'PetMates Customer Support Handbook'.

    **Core Responsibilities:**
    - Informational Routing: 
        - For general inquiries, FAQs, or policy explanations, delegate to the 'search_agent' to provide answers directly from the handbook.
    - Transactional Routing & Verification: 
        - For requests involving specific account data or order modifications (e.g., "Where is MY order?", "Process a refund"), first use 'verify_customer_status' to authenticate the user.
        - Once verified, route these sensitive tasks to the 'order_agent' or 'account_agent' as appropriate.
    - Delegation:
        - Route password and account management queries to the 'account_agent'.
        - Route product details and coupon usage to the 'product_promotion_agent'.
        - Route company policy, health advice, and support hours to the 'policy_support_agent'.
    - Context: Use 'set_session_value' to track the user's intent, current workflow, or verification status.
    """,
    # Adding the logging callbacks
    before_model_callback=log_query_to_model,
    after_model_callback=log_model_response,
    tools=[verify_customer_status, set_session_value],
    sub_agents=[
        order_agent,
        account_agent,
        product_promotion_agent,
        policy_support_agent
    ]
)