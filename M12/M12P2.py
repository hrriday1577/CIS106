# M12P2 - Parallel arrays of last names and exam scores
def display_names_scores(names, scores):
    for i in range(0, len(names)):
        print(f"{names[i]:<12}{scores[i]:>6.1f}")


def display_names_scores_reverse(names, scores):
    for i in range(len(names) - 1, -1, -1):
        print(f"{names[i]:<12}{scores[i]:>6.1f}")


last_names = ["Baker", "Jones", "Smith", "Davis", "Michaels",
              "Patel", "Garcia", "Nguyen", "Wilson", "Lopez"]
exam_scores = [89.5, 79.7, 92.4, 85.6, 95.5,
               88.0, 73.2, 91.8, 67.5, 84.3]

print("Names and scores in order:")
print(f"{'Last Name':<12}{'Score':>6}")
display_names_scores(last_names, exam_scores)

print()
print("Names and scores in reverse order:")
print(f"{'Last Name':<12}{'Score':>6}")
display_names_scores_reverse(last_names, exam_scores)
