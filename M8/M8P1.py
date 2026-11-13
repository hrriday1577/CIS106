# M8P1 - Five year interest table
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))

total_interest = 0.0

print()
print("Year".ljust(8) + "Beginning".rjust(14) + "Ending".rjust(17))
print("".ljust(8) + "Balance".rjust(14) + "Balance".rjust(17))
print()

for year in range(1, 6):
    interest = principal * rate
    ending_balance = principal + interest
    total_interest = total_interest + interest

    print(f"{year:5d}" + f"${principal:,.2f}".rjust(17) + f"${ending_balance:,.2f}".rjust(17))

    principal = ending_balance

print()
print(f"Total interest earned: ${total_interest:,.2f}")
