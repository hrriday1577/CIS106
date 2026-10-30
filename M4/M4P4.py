# M4P4 - Calories burned from steps
CALORIES_PER_STEP = 0.25

first_name = input("Enter your first name: ")
steps = int(input("Enter the number of steps walked today: "))

calories_burned = steps * CALORIES_PER_STEP

print(f"{first_name}, you burned {calories_burned:.2f} calories.")