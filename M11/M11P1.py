# M11P1 - Discount amount and discounted price (function returns 2 values)
def calc_discount(quantity, price, discount_rate):
    discount_amount = quantity * price * discount_rate
    discounted_price = quantity * price - discount_amount
    return discount_amount, discounted_price


quantity = float(input("Enter the quantity: "))
price = float(input("Enter the price: "))
discount_rate = float(input("Enter the discount rate (example 0.10 for 10%): "))

discount_amount, discounted_price = calc_discount(quantity, price, discount_rate)

print()
print("Quantity:".ljust(20) + f"{quantity:12,.0f}")
print("Price:".ljust(20) + f"${price:11,.2f}")
print("Discount amount:".ljust(20) + f"${discount_amount:11,.2f}")
print("Discounted price:".ljust(20) + f"${discounted_price:11,.2f}")
