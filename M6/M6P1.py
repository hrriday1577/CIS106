# M6P1 - Widget pricing with tax
TAX_RATE = 0.07

quantity = int(input("Enter the quantity of widgets: "))

if quantity > 10000:
    price = 10.00
elif quantity >= 5000:
    price = 20.00
else:
    price = 30.00

extended_price = quantity * price
tax = extended_price * TAX_RATE
total = extended_price + tax

print()
print("Extended price:".ljust(18) + f"${extended_price:12,.2f}")
print("Tax:".ljust(18) + f"${tax:12,.2f}")
print("Total:".ljust(18) + f"${total:12,.2f}")