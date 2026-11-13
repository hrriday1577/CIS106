# M7P4 - Payroll with overtime
total_gross = 0.0
count = 0

response = input("Do you want to enter employee data? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    last_name = input("Enter the employee's last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter rate of pay: "))

    if hours > 40:
        gross_pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        gross_pay = hours * rate

    total_gross = total_gross + gross_pay
    count = count + 1

    print("Last name:".ljust(14) + last_name)
    print("Gross pay:".ljust(14) + f"${gross_pay:10,.2f}")
    print()

    response = input("Do you want to enter another employee? (Yes or No): ")

print()
print("Total gross pay:".ljust(22) + f"${total_gross:10,.2f}")
print("Number of employees:".ljust(22) + f"{count:11d}")
if count > 0:
    average_pay = total_gross / count
    print("Average pay:".ljust(22) + f"${average_pay:10,.2f}")
