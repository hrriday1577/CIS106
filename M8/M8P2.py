# M8P2 - First 20 Fibonacci numbers
first = 1
second = 1

for count in range(1, 21):
    print(f"{count:2d}: {first}")
    next_number = first + second
    first = second
    second = next_number
