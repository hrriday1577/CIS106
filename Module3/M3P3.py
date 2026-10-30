# M3P3 - Split job payment three ways
amount_received = float(input("Enter the amount received for the job: "))

each_share = amount_received / 3

print(f"Each person will receive: ${each_share:.2f}")