import os
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools import VertexAiSearchTool
from google.genai import types

load_dotenv()

# Load configuration
RETRY_OPTIONS = types.HttpRetryOptions(initial_delay=1, max_delay=3, attempts=30)

PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT')
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')
MODEL_NAME = os.getenv("MODEL") 

# Construct the resource path
SEARCH_ENGINE_PATH = f"projects/{PROJECT_ID}/locations/global/collections/default_collection/engines/{SEARCH_ENGINE_ID}"

# Initialize the tool
faq_search_tool = VertexAiSearchTool(search_engine_id=SEARCH_ENGINE_PATH)

# Define the Agent with explicit guardrails
search_agent = Agent(
    name="search_agent",
    model=Gemini(model=MODEL_NAME, retry_options=RETRY_OPTIONS),
    instruction="""
    You are a professional concierge assistant for Buni services. 
    Use the provided search_tool to look up information regarding our services, FAQs, and policies.
    
    Guidelines:
    1. Only answer based on the information retrieved by the search_tool.
    2. If the user's query cannot be answered by the tool, politely inform the user that you don't have that information.
    3. Maintain a professional, helpful, and concise tone at all times.
    4. Do not hallucinate or provide information outside of the provided FAQ data.
    """,
    tools=[faq_search_tool],
)