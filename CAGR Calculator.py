def calculate_cagr(start_value, end_value, periods):
    """
    Calculate the Compound Annual Growth Rate (CAGR).

    Parameters:
    start_value (float): The starting value of the investment.
    end_value (float): The ending value of the investment.
    periods (int): The number of periods (years).

    Returns:
    float: The CAGR as a percentage.
    """
    if start_value <= 0 or end_value <= 0 or periods <= 0:
        raise ValueError("All input values must be positive and greater than zero.")

    cagr = (end_value / start_value) ** (1 / periods) - 1
    return cagr * 100


# Example usage
start_value = 1000000  # Initial investment amount
end_value = 25000000  # Final investment amount
periods = 31  # Investment period in years

cagr = calculate_cagr(start_value, end_value, periods)
print(f"The Compound Annual Growth Rate (CAGR) is {cagr:.2f}%")
