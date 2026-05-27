import os
from google.adk.agents import Agent
from google.adk.models import Gemini
# Updated path: Look inside the 'search_agent' sibling or 
# wherever 'coverage_calculator' is located relative to this file
from .sub_agents.coverage_calculator.agent import coverage_calculator_agent

cleaning_agent = Agent(
    name="connors_cleaning_agent",
    model=Gemini(model=os.getenv("MODEL", "gemini-1.5-flash")),
    description="Specialist for Connor's Cleaning quotes. Delegates math to the coverage_calculator_agent.",
    instruction="""
    You are the specialist for Connor's Cleaning services. Your goal is to collect property details.
    
    Workflow:
    1. Ask if the property is a 'House' or 'Apartment'.
    2. Ask for square footage.
    3. Ask for the service tier ('Regular', 'Deep', 'Move-In', 'Post-Renovation').
    4. Once you have all data, transfer the conversation to 'coverage_calculator_agent' 
       to perform the final price calculation.
    5. Present the final price provided by the calculator to the user in a professional manner.
    """,
    sub_agents=[coverage_calculator_agent] 
)