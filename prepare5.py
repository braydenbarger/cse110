first = input("What is the first number?: ")
second = input("What is the second number?: ")

if first > second:
    print("The first number is greater than the second")
else:
    print("The first number is not greater than the second")

if first == second:
    print("The first number is equal to the second")
else:
    print("The first number is not equal to the second")

if first < second:
    print("The first number is less than the second")
else:
    print("The first number is not less than the second")

animal = input("What is your favorite animal?: ")

if animal.lower() == "panda":
    print("That's my favorite animal too")
else:
    print("That's not my favorite animal")