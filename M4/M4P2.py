# M4P2 - Stock gain or loss
purchase_price = float(input("Enter the purchase price per share: "))
current_price = float(input("Enter the current stock price: "))
quantity = float(input("Enter the quantity of stock: "))

value_change = (current_price - purchase_price) * quantity

print(f"Change in value: ${value_change:.2f}")