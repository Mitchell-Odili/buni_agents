from google.adk.agents.llm_agent import Agent
from .tools import process_refund, calculate_cleaning_price

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for Buni Agents.',
    instruction='You are a helpful assistant. Use your tools to process requests.',
    # Pass the functions directly
    tools=[process_refund, calculate_cleaning_price]
)