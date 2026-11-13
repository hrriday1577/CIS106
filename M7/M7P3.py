# M7P3 - Student exam averages
count = 0

response = input("Do you want to enter student data? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    last_name = input("Enter the student's last name: ")
    exam1 = float(input("Enter exam score 1: "))
    exam2 = float(input("Enter exam score 2: "))

    average = (exam1 + exam2) / 2
    count = count + 1

    print("Last name:".ljust(16) + last_name)
    print("Average:".ljust(16) + f"{average:.2f}")
    print()

    response = input("Do you want to enter another student? (Yes or No): ")

print()
print("Number of students:", count)
