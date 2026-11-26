# M11P3 - Sales report (function returns commission and next year's target)
def calc_commission_target(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05
    next_year_target = sales * 1.05   # 5% more than this year's sales
    return commission, next_year_target


last_name = input("Enter the salesperson's last name: ")
sales = float(input("Enter the sales: "))

commission, next_year_target = calc_commission_target(sales)

print()
print("Salesperson:".ljust(20) + last_name)
print("Commission:".ljust(20) + f"${commission:12,.2f}")
print("Next year's target:".ljust(20) + f"${next_year_target:12,.2f}")
