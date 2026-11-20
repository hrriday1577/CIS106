# M9P5 - Tuition with a function
def calc_tuition(credit_hours, district_code):
    if district_code == "I":
        return credit_hours * 250.00
    else:
        return credit_hours * 550.00


total_tuition = 0.0

response = input("Do you want to enter a student? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    last_name = input("Enter the student's last name: ")
    credit_hours = int(input("Enter credit hours: "))
    district_code = input("Enter the district code (I or O): ").strip().upper()

    tuition = calc_tuition(credit_hours, district_code)
    total_tuition = total_tuition + tuition

    print("Last name:".ljust(16) + last_name)
    print("Tuition owed:".ljust(16) + f"${tuition:10,.2f}")
    print()

    response = input("Do you want to enter another student? (Yes or No): ")

print()
print("Total tuition owed:".ljust(21) + f"${total_tuition:10,.2f}")
