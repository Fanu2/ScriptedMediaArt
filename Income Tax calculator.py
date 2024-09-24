def calculate_tax(income):
    income -= 75000  # Apply the standard deduction

    if income <= 300000:
        return 0
    elif income <= 700000:
        tax = (income - 300000) * 0.05
        return tax if income > 500000 else 0  # Tax rebate u/s 87A for income <= 7 lakh
    elif income <= 1000000:
        return (income - 700000) * 0.10 + 20000
    elif income <= 1200000:
        return (income - 1000000) * 0.15 + 50000
    elif income <= 1500000:
        return (income - 1200000) * 0.20 + 80000
    else:
        return (income - 1500000) * 0.30 + 140000

def add_cess(tax):
    return tax * 0.04

def calculate_total_tax(income):
    tax = calculate_tax(income)
    cess = add_cess(tax)
    total_tax = tax + cess
    return tax, cess, total_tax

def main():
    income = float(input("Enter your annual income: ₹ "))
    tax, cess, total_tax = calculate_total_tax(income)
    print(f"Income Tax: ₹ {tax:.2f}")
    print(f"Cess: ₹ {cess:.2f}")
    print(f"Total Income Tax: ₹ {total_tax:.2f}")

if __name__ == "__main__":
    main()
