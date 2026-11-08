# M6P2 - Part cost
part_number = input("Enter the part number: ")
quantity = int(input("Enter the quantity: "))

if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00

total_cost = quantity * unit_cost

print()
print("Part number:".ljust(16) + part_number.rjust(10))
print("Cost per unit:".ljust(16) + f"${unit_cost:9,.2f}")
print("Total cost:".ljust(16) + f"${total_cost:9,.2f}")