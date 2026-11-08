# M6P5 - Employee bonus
last_name = input("Enter the employee last name: ")
salary = float(input("Enter the salary: "))
job_level = int(input("Enter the job level: "))

if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

bonus = salary * bonus_rate

print()
print("Employee:".ljust(12) + last_name.rjust(12))
print("Bonus:".ljust(12) + f"${bonus:11,.2f}")