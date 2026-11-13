# M8P4 - Orders from a file
f = open("orders.txt", "r")

total_extended = 0.0
count = 0

print("Item".ljust(10) + "Quantity".rjust(10) + "Price".rjust(12) + "Extended".rjust(14))
print()

item = f.readline().rstrip("\n")

while item != "":
    quantity = float(f.readline())
    price = float(f.readline())

    extended_price = quantity * price
    total_extended = total_extended + extended_price
    count = count + 1

    print(item.ljust(10) + f"{quantity:10.0f}" + f"${price:,.2f}".rjust(12) + f"${extended_price:,.2f}".rjust(14))

    item = f.readline().rstrip("\n")

f.close()

print()
print("Total extended prices:".ljust(24) + f"${total_extended:,.2f}".rjust(12))
print("Number of orders:".ljust(24) + f"{count}".rjust(12))
if count > 0:
    average_order = total_extended / count
    print("Average order:".ljust(24) + f"${average_order:,.2f}".rjust(12))
