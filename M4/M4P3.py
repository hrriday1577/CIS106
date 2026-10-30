# M4P3 - Tip calculator
meal_total = float(input("Enter the total for the meal: "))

tip_15 = meal_total * 0.15
tip_18 = meal_total * 0.18
tip_20 = meal_total * 0.20

print()
print("With 15% Tip:")
print()
print("Total:".ljust(15) + f"{meal_total:5.2f}")
print("Tip:".ljust(15) + f"{tip_15:5.2f}")
print("Total with Tip".ljust(15) + f"{meal_total + tip_15:5.2f}")
print()
print()
print("With 18% Tip:")
print()
print("Total:".ljust(15) + f"{meal_total:5.2f}")
print("Tip:".ljust(15) + f"{tip_18:5.2f}")
print("Total with Tip".ljust(15) + f"{meal_total + tip_18:5.2f}")
print()
print()
print("With 20% Tip:")
print()
print("Total:".ljust(15) + f"{meal_total:5.2f}")
print("Tip:".ljust(15) + f"{tip_20:5.2f}")
print("Total with Tip".ljust(15) + f"{meal_total + tip_20:5.2f}")