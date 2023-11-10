num = input("Enter the number: "); n = len(num); total = 0

for digit in num:
    total += int(digit) ** n

print("Armstrong" if total == int(num) else "Not Armstrong")
