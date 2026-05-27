from dotenv import load_dotenv
import os
from google.adk.tools import ToolContext

load_dotenv()


async def set_session_value(tool_context: ToolContext, key: str, value: str):
    """Sets a value in the tool_context's state dictionary."""
    tool_context.state[key] = value
    return {"status": f"stored '{value}' in '{key}'"}

async def verify_customer_status(tool_context: ToolContext, customer_id: str):
    """
    Verifies if a customer ID is valid and active in the system.
    Checks the session state to ensure the user is authorized.
    """
    # Simulate a database or system check
    # In a production environment, this would call your user management API/DB
    if not customer_id:
        return {"status": "error", "message": "Customer ID is required."}
    
    # Example logic: Check if the ID exists in the current session context
    # or perform a mock validation
    is_valid = True  # Replace with actual validation logic
    
    if is_valid:
        tool_context.state['authorized_customer_id'] = customer_id
        return {"status": "success", "message": f"Customer {customer_id} verified successfully."}
    else:
        return {"status": "error", "message": "Customer verification failed. Unauthorized."}