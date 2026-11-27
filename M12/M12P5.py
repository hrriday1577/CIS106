# M12P5 - Search by last name and show "Name not found" when missing
def display_players(names, averages):
    print(f"{'Player':<12}{'Average':>8}")
    for i in range(0, len(names)):
        print(f"{names[i]:<12}{averages[i]:>8.3f}")


def search_player(names, averages, search_name):
    found = False
    for i in range(0, len(names)):
        if names[i] == search_name:
            print(f"{names[i]:<12}{averages[i]:>8.3f}")
            found = True
    if found == False:
        print("Name not found")


player_names = []
batting_averages = []

player_file = open("players.txt", "r")
name = player_file.readline().rstrip("\n")
while name != "":
    average = float(player_file.readline().rstrip("\n"))
    player_names.append(name)
    batting_averages.append(average)
    name = player_file.readline().rstrip("\n")
player_file.close()

display_players(player_names, batting_averages)
print()

search_name = input("Enter a last name to search for (or quit to stop): ").strip()
while search_name.lower() != "quit":
    search_player(player_names, batting_averages, search_name)
    print()
    search_name = input("Enter a last name to search for (or quit to stop): ").strip()
