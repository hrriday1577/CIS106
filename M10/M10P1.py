# M10P1 - Next month's sales forecast with a function
def calc_forecast(month, sales):
    month = month.strip().title()[:3]
    if month in ("Jan", "Feb", "Mar"):
        forecast_percent = 0.10
    elif month in ("Apr", "May", "Jun"):
        forecast_percent = 0.15
    elif month in ("Jul", "Aug", "Sep"):
        forecast_percent = 0.20
    else:
        forecast_percent = 0.25
    return sales * (1 + forecast_percent)


response = input("Do you want to enter a salesperson? (Yes or No): ")

while response.strip().lower() in ("yes", "y"):
    last_name = input("Enter the last name: ")
    month = input("Enter the month (Jan to Dec): ")
    sales = float(input("Enter the sales: "))

    next_month_sales = calc_forecast(month, sales)

    print("Last name:".ljust(22) + last_name)
    print("Sales:".ljust(22) + f"${sales:12,.2f}")
    print("Next month forecast:".ljust(22) + f"${next_month_sales:12,.2f}")
    print()

    response = input("Do you want to enter another salesperson? (Yes or No): ")
