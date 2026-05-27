# buni_agents/sub_agents/connors_agent/sub_agents/coverage_calculator/tools.py

async def calculate_cleaning_price(
    property_type: str, 
    area_sqft: int, 
    service_tier: str
):
    """Calculates cleaning price based on property type, size, and tier."""
    # Define rates
    rates = {"Regular": 0.5, "Deep": 0.8, "Move-In": 1.2, "Post-Renovation": 1.5}
    multiplier = 1.15 if property_type == "House" else 1.0
    
    price = area_sqft * rates.get(service_tier, 0.5) * multiplier
    
    return {"total_price": price, "currency": "USD"}