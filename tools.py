
def verify_customer_status(user_id: str) -> bool:
    print(f"DEBUG: Checking database for user: {user_id}")
    return True

def process_refund(user_id: str, amount: float) -> str:
    """
    Processes a refund for a customer.
    Args:
        user_id: The ID of the customer.
        amount: Refund amount in USD.
    """
    if verify_customer_status(user_id):
        return f"SUCCESS: Refund of ${amount} processed for user {user_id}."
    return "FAILURE: Access Denied."

def calculate_cleaning_price(service_tier: str, area_sqft: int) -> float:
    """
        Pricing Engine: Calculates service cost based on tier and area.
        Tiers: 'Regular', 'Deep', 'Move-In', 'Post-Renovation'.
        """
    # Define multipliers per tier
    rates = {
        "Regular": 0.5,
        "Deep": 0.8,
        "Move-In": 1.2,
        "Post-Renovation": 1.5
    }
    
    # Calculate base price (e.g., $1.00 per sqft as base)
    rate = rates.get(service_tier, 0.5)
    total_price = area_sqft * rate
    
    return float(total_price)