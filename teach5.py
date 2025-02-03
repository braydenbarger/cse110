grade = int(input("What is your grade?: "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
elif grade < 60:
    letter = "F"

last = grade % 10

if last >= 7:
    sign = "+"
elif last < 3:
    sign = "-"
else:
    sign = ""

if grade >= 93:
    sign = ""

print(f"Your letter grade is {letter}{sign}")

if grade >= 70:
    print("Congratulations you passed the class")
else:
    print("Better luck next time")