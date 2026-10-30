# M3P1 - Amount invested in a stock
ticker = input("Enter the stock ticker symbol: ")
shares = float(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))

amount_invested = shares * cost_per_share

print(f"Amount invested in {ticker}: ${amount_invested:.2f}")