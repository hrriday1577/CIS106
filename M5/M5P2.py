# M5P2 - Unit price by item
item = input("Enter the item (A or B): ")
quantity = int(input("Enter the quantity: "))

if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

extended_price = quantity * unit_price

print(f"Item: {item}")
print(f"Unit price: ${unit_price:.2f}")
print(f"Extended price: ${extended_price:.2f}")