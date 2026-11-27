# M12P1 - Display 10 last names in order and in reverse order
def display_names(names):
    for i in range(0, len(names)):
        print(f"{i + 1:>2}. {names[i]}")


def display_names_reverse(names):
    for i in range(len(names) - 1, -1, -1):
        print(f"{i + 1:>2}. {names[i]}")


last_names = ["Baker", "Jones", "Smith", "Davis", "Michaels",
              "Patel", "Garcia", "Nguyen", "Wilson", "Lopez"]

print("Names in order:")
display_names(last_names)

print()
print("Names in reverse order:")
display_names_reverse(last_names)
