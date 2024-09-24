def calculate_discounted_value(future_value, discount_rate, periods):
    """
    Calculate the discounted value (present value) of a future amount of money.

    Parameters:
    future_value (float): The future value of the investment.
    discount_rate (float): The discount rate (as a percentage).
    periods (int): The number of periods.

    Returns:
    float: The present value.
    """
    if future_value <= 0 or discount_rate <= 0 or periods <= 0:
        raise ValueError("All input values must be positive and greater than zero.")

    discount_rate = discount_rate / 100  # Convert percentage to decimal
    present_value = future_value / ((1 + discount_rate) ** periods)
    return present_value


# Example usage
future_value = 1000  # Future amount of money
discount_rate = 5  # Discount rate in percentage
periods = 3  # Number of periods

present_value = calculate_discounted_value(future_value, discount_rate, periods)
print(f"The present value is {present_value:.2f}")
