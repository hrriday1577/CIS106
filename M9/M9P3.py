# M9P3 - Miles per gallon with a function
def calc_mpg(miles, gallons):
    if gallons == 0:
        return 0.0
    return miles / gallons


count = 0

response = input("Do you want to enter a trip? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    city = input("Enter the destination city: ")
    miles = float(input("Enter the miles travelled: "))
    gallons = float(input("Enter the gallons used: "))

    mpg = calc_mpg(miles, gallons)
    count = count + 1

    print("Destination:".ljust(16) + city)
    print("Miles:".ljust(16) + f"{miles:10,.1f}")
    print("MPG:".ljust(16) + f"{mpg:10,.2f}")
    print()

    response = input("Do you want to enter another trip? (Yes or No): ")

print()
print("Number of trips:", count)
