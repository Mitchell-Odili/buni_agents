import os
from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types
from .tools import calculate_cleaning_price
from .....callback_logging import log_query_to_model, log_model_response

RETRY_OPTIONS = types.HttpRetryOptions(initial_delay=1, max_delay=3, attempts=30)

coverage_calculator_agent = Agent(
    name="coverage_calculator_agent",
    model=Gemini(model=os.getenv("MODEL"), retry_options=RETRY_OPTIONS),
    instruction="""
    You are the Pricing Specialist for Connor's Cleaning.
    Use the 'calculate_cleaning_price' tool to determine the cost based on the data provided.
    Present the final price clearly to the user.
    """,
    before_model_callback=log_query_to_model,
    after_model_callback=log_model_response,
    tools=[calculate_cleaning_price],
)