# M8P3 - Employee bonuses from a file
f = open("employees.txt", "r")

total_bonus = 0.0

print("Last Name".ljust(12) + "Salary".rjust(14) + "Bonus".rjust(13))
print()

last_name = f.readline().rstrip("\n")

while last_name != "":
    salary = float(f.readline())

    if salary >= 100000.00:
        bonus_rate = 0.20
    elif salary >= 50000.00:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.10

    bonus = salary * bonus_rate
    total_bonus = total_bonus + bonus

    print(last_name.ljust(12) + f"${salary:,.2f}".rjust(14) + f"${bonus:,.2f}".rjust(13))

    last_name = f.readline().rstrip("\n")

f.close()

print()
print(f"Total bonuses paid: ${total_bonus:,.2f}")
