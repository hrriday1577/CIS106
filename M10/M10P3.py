# M10P3 - Out the door price of a car with a function
SALES_TAX_RATE = 0.07


def calc_out_the_door(msrp, make, model, electric_code):
    make = make.strip().lower()
    model = model.strip().lower()
    if make == "honda" and model == "accord":
        percent_off = 0.10
    elif make == "toyota" and model == "rav4":
        percent_off = 0.15
    elif electric_code == "Y":
        percent_off = 0.30
    else:
        percent_off = 0.05
    new_msrp = msrp - msrp * percent_off
    return new_msrp + new_msrp * SALES_TAX_RATE


total_msrp = 0.0
total_sales_price = 0.0

response = input("Do you want to enter a car? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    electric_code = input("Is it an electric vehicle? (Y or N): ").strip().upper()
    msrp = float(input("Enter the MSRP: "))

    out_the_door = calc_out_the_door(msrp, make, model, electric_code)

    total_msrp = total_msrp + msrp
    total_sales_price = total_sales_price + out_the_door

    print("Car:".ljust(18) + make + " " + model)
    print("MSRP:".ljust(18) + f"${msrp:12,.2f}")
    print("Out the door:".ljust(18) + f"${out_the_door:12,.2f}")
    print()

    response = input("Do you want to enter another car? (Yes or No): ")

print()
print("Total MSRP:".ljust(20) + f"${total_msrp:12,.2f}")
print("Total sales price:".ljust(20) + f"${total_sales_price:12,.2f}")
