def calculate_future_value(present_value, annual_growth_rate, years):
    """
    Calculate the future value of an investment in a multibagger stock.

    Parameters:
    present_value (float): The present value (initial investment).
    annual_growth_rate (float): The annual growth rate (as a percentage).
    years (int): The number of years.

    Returns:
    float: The future value.
    """
    if present_value <= 0 or annual_growth_rate <= 0 or years <= 0:
        raise ValueError("All input values must be positive and greater than zero.")

    annual_growth_rate = annual_growth_rate / 100  # Convert percentage to decimal
    future_value = present_value * ((1 + annual_growth_rate) ** years)
    return future_value


# Example usage
present_value = 3000000  # Initial investment
annual_growth_rate = 18  # Annual growth rate in percentage
years = 2  # Number of years

future_value = calculate_future_value(present_value, annual_growth_rate, years)
print(f"The future value of the investment is {future_value:.2f}")
