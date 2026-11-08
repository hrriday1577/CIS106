# M6P3 - CD interest rate
principle = float(input("Enter the principle amount: "))
years = int(input("Enter the years to maturity: "))

if principle > 100000.00 and years == 5:
    rate = 0.06
elif principle >= 50000.00 and years == 10:
    rate = 0.05
elif principle >= 50000.00 and years == 5:
    rate = 0.04
else:
    rate = 0.02

interest = principle * rate

print()
print("Principle:".ljust(22) + f"${principle:12,.2f}")
print("Interest rate:".ljust(22) + f"{rate * 100:12.2f}%")
print("First year interest:".ljust(22) + f"${interest:12,.2f}")