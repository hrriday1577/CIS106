# M3P2 - Total exam points
last_name = input("Enter your last name: ")
midterm = float(input("Enter your midterm score (0-100): "))
final_exam = float(input("Enter your final exam score (0-100): "))

total_points = midterm * 0.40 + final_exam * 0.60

print(f"{last_name}, your total exam points: {total_points:.2f}")