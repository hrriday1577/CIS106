# M5P4 - Appliance warranty
appliance_name = input("Enter the name of the appliance: ")
appliance_cost = float(input("Enter the cost of the appliance: "))

if appliance_cost > 1000.00:
    warranty_rate = 0.10
else:
    warranty_rate = 0.05

warranty_cost = appliance_cost * warranty_rate
total = appliance_cost + warranty_cost

print(f"Appliance: {appliance_name}")
print(f"Cost of appliance: ${appliance_cost:.2f}")
print(f"Warranty cost: ${warranty_cost:.2f}")
print(f"Total: ${total:.2f}")