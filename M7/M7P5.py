# M7P5 - Order discounts
total_discount = 0.0

response = input("Do you want to enter an order? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    quantity = float(input("Enter the quantity: "))
    price = float(input("Enter the price of the item: "))

    extended_price = quantity * price

    if extended_price > 10000.00:
        discount_rate = 0.25
    else:
        discount_rate = 0.10

    discount_amount = extended_price * discount_rate
    total = extended_price - discount_amount
    total_discount = total_discount + discount_amount

    print("Extended price:".ljust(18) + f"${extended_price:11,.2f}")
    print("Discount amount:".ljust(18) + f"${discount_amount:11,.2f}")
    print("Total:".ljust(18) + f"${total:11,.2f}")
    print()

    response = input("Do you want to enter another order? (Yes or No): ")

print()
print("Total of all discounts:".ljust(25) + f"${total_discount:11,.2f}")
