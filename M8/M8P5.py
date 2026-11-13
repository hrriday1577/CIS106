# M8P5 - Tuition from a file
IN_DISTRICT_RATE = 250.00
OUT_DISTRICT_RATE = 500.00

f = open("students.txt", "r")

total_tuition = 0.0
count = 0

print("Last Name".ljust(12) + "Credits".rjust(9) + "Tuition".rjust(14))
print()

last_name = f.readline().rstrip("\n")

while last_name != "":
    district = f.readline().rstrip("\n").strip().upper()
    credits = int(f.readline())

    if district == "I":
        cost_per_credit = IN_DISTRICT_RATE
    else:
        cost_per_credit = OUT_DISTRICT_RATE

    tuition = credits * cost_per_credit
    total_tuition = total_tuition + tuition
    count = count + 1

    print(last_name.ljust(12) + f"{credits:9d}" + f"${tuition:,.2f}".rjust(14))

    last_name = f.readline().rstrip("\n")

f.close()

print()
print("Total tuition owed:".ljust(21) + f"${total_tuition:,.2f}".rjust(14))
print("Number of students:".ljust(21) + f"{count}".rjust(14))
