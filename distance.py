distance = int(input("Enter the distance (in Km): "))


if distance <= 50:
    fare = distance * 8
    print("The fare for the given distance is: Rs.",fare)
elif 51 <= distance <= 100:
    fare = distance * 10
    print("The fare for the given distance is: Rs.",fare)
else:
    fare = distance * 12
    print("The fare for the given distance is: Rs.",fare)
