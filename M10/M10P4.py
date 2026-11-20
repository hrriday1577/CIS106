# M10P4 - Train ticket price with a function
def calc_ticket_price(miles):
    if miles >= 30:
        return 12.00
    elif miles >= 20:
        return 10.00
    elif miles >= 10:
        return 8.00
    else:
        return 5.00


total_tickets = 0.0

response = input("Do you want to enter a rider? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    last_name = input("Enter the last name: ")
    miles = float(input("Enter the miles from downtown Chicago: "))

    ticket_price = calc_ticket_price(miles)
    total_tickets = total_tickets + ticket_price

    print("Last name:".ljust(16) + last_name)
    print("Ticket price:".ljust(16) + f"${ticket_price:8,.2f}")
    print()

    response = input("Do you want to enter another rider? (Yes or No): ")

print()
print("Total of all tickets:".ljust(24) + f"${total_tickets:8,.2f}")
