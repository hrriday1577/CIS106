# M3P4 - Auto discount
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
msrp = float(input("Enter the MSRP: "))
discount_percent = float(input("Enter the discount percent as a decimal (example 0.10): "))

amount_off = msrp * discount_percent
discounted_price = msrp - amount_off

print(f"Make: {make}")
print(f"Model: {model}")
print(f"MSRP: ${msrp:.2f}")
print(f"Discount percent: {discount_percent:.1%}")
print(f"Amount off: ${amount_off:.2f}")
print(f"Discounted price: ${discounted_price:.2f}")