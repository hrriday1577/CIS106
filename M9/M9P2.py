# M9P2 - Batting average with a function
def calc_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0
    return hits / at_bats


count = 0

response = input("Do you want to enter a player? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    last_name = input("Enter the player's last name: ")
    hits = int(input("Enter the number of hits: "))
    at_bats = int(input("Enter the number of at bats: "))

    average = calc_batting_average(hits, at_bats)
    count = count + 1

    print("Last name:".ljust(18) + last_name)
    print("Batting average:".ljust(18) + f"{average:.3f}")
    print()

    response = input("Do you want to enter another player? (Yes or No): ")

print()
print("Number of players:", count)
