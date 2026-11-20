# M10P2 - Gallons of paint for a room with functions
SQ_FT_PER_GALLON = 50


def calc_wall_area(length, width, height):
    return 2 * length * height + 2 * width * height


def calc_ceiling_area(length, width):
    return length * width


response = input("Do you want to enter a room? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    length = float(input("Enter the length of the room: "))
    width = float(input("Enter the width of the room: "))
    height = float(input("Enter the height of the room: "))

    wall_area = calc_wall_area(length, width, height)
    wall_gallons = wall_area / SQ_FT_PER_GALLON

    ceiling_area = calc_ceiling_area(length, width)
    ceiling_gallons = ceiling_area / SQ_FT_PER_GALLON

    print("Wall square feet:".ljust(26) + f"{wall_area:10,.2f}")
    print("Gallons for walls:".ljust(26) + f"{wall_gallons:10,.2f}")
    print("Ceiling square feet:".ljust(26) + f"{ceiling_area:10,.2f}")
    print("Gallons for ceiling:".ljust(26) + f"{ceiling_gallons:10,.2f}")
    print()

    response = input("Do you want to enter another room? (Yes or No): ")
