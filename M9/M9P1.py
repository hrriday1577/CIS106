# M9P1 - Extended price with a function
def calc_extended_price(quantity, price):
    total = quantity * price
    if total > 10000.00:
        total = total * 0.90
    return total


total_ext_price = 0.0

response = input("Do you want to enter an item? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    quantity = float(input("Enter the quantity: "))
    price = float(input("Enter the price: "))

    ext_price = calc_extended_price(quantity, price)
    total_ext_price = total_ext_price + ext_price

    print("Quantity:".ljust(18) + f"{quantity:12,.0f}")
    print("Price:".ljust(18) + f"${price:11,.2f}")
    print("Extended price:".ljust(18) + f"${ext_price:11,.2f}")
    print()

    response = input("Do you want to enter another item? (Yes or No): ")

print()
print("Total extended price:".ljust(23) + f"${total_ext_price:11,.2f}")
