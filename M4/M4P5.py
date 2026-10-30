# M4P5 - Break-even point
fixed_costs = float(input("Enter the fixed costs: "))
price_per_unit = float(input("Enter the price per unit: "))
cost_per_unit = float(input("Enter the cost per unit: "))

break_even = fixed_costs / (price_per_unit - cost_per_unit)

print(f"Break-even point: {break_even:.2f} units")