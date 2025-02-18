while True:
    number = int(input("Please type a positive number: "))
    if number >= 0:
        print(f"The number is: {number}")
        break
    else:
        print("Sorry, that is a negative number. Please try again.")

answer = ""
while answer != "yes":
    answer = input("May I have a piece of candy? ")

print ("Thank you.")