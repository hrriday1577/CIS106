# M11P4 - Bowling average with handicap (function returns 2 values)
def calc_bowling_average(game1, game2, game3, handicap):
    average = (game1 + game2 + game3) / 3
    average_with_handicap = average + handicap
    return average, average_with_handicap


last_name = input("Enter the bowler's last name: ")
game1 = float(input("Enter game 1 score: "))
game2 = float(input("Enter game 2 score: "))
game3 = float(input("Enter game 3 score: "))
handicap = float(input("Enter the handicap: "))

average, average_with_handicap = calc_bowling_average(game1, game2, game3, handicap)

print()
print("Last name:".ljust(28) + last_name)
print("Average score:".ljust(28) + f"{average:8.1f}")
print("Average score with handicap:".ljust(28) + f"{average_with_handicap:8.1f}")
