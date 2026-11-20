# M10P5 - Assessed value of a home with a function
def calc_assessed_value(county, market_value):
    county = county.strip().lower()
    if county == "cook":
        assessed_percent = 0.90
    elif county == "dupage":
        assessed_percent = 0.80
    elif county == "mchenry":
        assessed_percent = 0.75
    elif county == "kane":
        assessed_percent = 0.60
    else:
        assessed_percent = 0.70
    return market_value * assessed_percent


total_market = 0.0
total_assessed = 0.0

response = input("Do you want to enter a home? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    county = input("Enter the county: ")
    market_value = float(input("Enter the market value: "))

    assessed_value = calc_assessed_value(county, market_value)

    total_market = total_market + market_value
    total_assessed = total_assessed + assessed_value

    print("County:".ljust(18) + county)
    print("Market value:".ljust(18) + f"${market_value:12,.2f}")
    print("Assessed value:".ljust(18) + f"${assessed_value:12,.2f}")
    print()

    response = input("Do you want to enter another home? (Yes or No): ")

print()
print("Total market value:".ljust(22) + f"${total_market:12,.2f}")
print("Total assessed value:".ljust(22) + f"${total_assessed:12,.2f}")
