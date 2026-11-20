# M9P4 - Gross pay with a pay rate function
def get_pay_rate(job_code):
    if job_code == "L":
        return 25.00
    elif job_code == "A":
        return 30.00
    elif job_code == "J":
        return 50.00
    else:
        return 0.00


total_gross = 0.0

response = input("Do you want to enter an employee? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    last_name = input("Enter the employee's last name: ")
    job_code = input("Enter the job code (L, A or J): ").strip().upper()
    hours = float(input("Enter hours worked: "))

    rate = get_pay_rate(job_code)

    if hours > 40:
        gross_pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        gross_pay = hours * rate

    total_gross = total_gross + gross_pay

    print("Last name:".ljust(14) + last_name)
    print("Gross pay:".ljust(14) + f"${gross_pay:10,.2f}")
    print()

    response = input("Do you want to enter another employee? (Yes or No): ")

print()
print("Total gross pay:".ljust(18) + f"${total_gross:10,.2f}")
