# M12P3 - Load names and scores from a file, show highest and lowest
def display_high_low(names, scores):
    high_var = 0
    high_index = 0
    low_var = 999
    low_index = 0
    for i in range(0, len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
    print("Highest score:".ljust(16) + f"{names[high_index]:<12}{high_var:>6.1f}")
    print("Lowest score:".ljust(16) + f"{names[low_index]:<12}{low_var:>6.1f}")


last_names = []
exam_scores = []

score_file = open("scores.txt", "r")
last_name = score_file.readline().rstrip("\n")
while last_name != "":
    score = float(score_file.readline().rstrip("\n"))
    last_names.append(last_name)
    exam_scores.append(score)
    last_name = score_file.readline().rstrip("\n")
score_file.close()

print(f"{'Last Name':<12}{'Score':>6}")
for i in range(0, len(last_names)):
    print(f"{last_names[i]:<12}{exam_scores[i]:>6.1f}")

print()
display_high_low(last_names, exam_scores)
