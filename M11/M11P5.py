# M11P5 - Total and tax using global variables
TAX_RATE = 0.07

total = 0.0
tax = 0.0


def calc_total_tax(quantity, unit_price):
    global total
    global tax
    total = quantity * unit_price
    tax = total * TAX_RATE


quantity = float(input("Enter the quantity: "))
unit_price = float(input("Enter the unit price: "))

calc_total_tax(quantity, unit_price)

print()
print("Total:".ljust(10) + f"${total:11,.2f}")
print("Tax:".ljust(10) + f"${tax:11,.2f}")
