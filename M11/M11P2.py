# M11P2 - Exam total and average (function returns 2 values)
def calc_exam_results(exam1, exam2, exam3):
    total_points = exam1 + exam2 + exam3
    average = total_points / 3
    return total_points, average


last_name = input("Enter the student's last name: ")
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
exam3 = float(input("Enter exam 3 score: "))

total_points, average = calc_exam_results(exam1, exam2, exam3)

print()
print("Last name:".ljust(16) + last_name)
print("Total points:".ljust(16) + f"{total_points:8.1f}")
print("Average:".ljust(16) + f"{average:8.1f}")
