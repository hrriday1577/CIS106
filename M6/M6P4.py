# M6P4 - Concert ticket pricing
tickets = int(input("Enter the number of tickets: "))

if tickets >= 25:
    price_per_ticket = 50.00
elif tickets >= 10:
    price_per_ticket = 60.00
elif tickets >= 5:
    price_per_ticket = 70.00
else:
    price_per_ticket = 75.00

total_cost = tickets * price_per_ticket

print()
print("Number of tickets:".ljust(20) + f"{tickets:10d}")
print("Price per ticket:".ljust(20) + f"${price_per_ticket:9,.2f}")
print("Total cost:".ljust(20) + f"${total_cost:9,.2f}")