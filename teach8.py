word = "Commitment"
fav_letter = input("What is your favorite letter? ").lower()

for letter in word:
    if letter.lower() == fav_letter:
        print(letter.upper())
    else:
        print(letter.lower())

print("Printing on the same line:", end=" ")
for letter in word:
    if letter.lower() == fav_letter:
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

print("Hiding favorite letter:", end=" ")
for letter in word:
    if letter.lower() == fav_letter:
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()

quote = ("In coming days, it will not be possible to survive spiritually "
         "without the guiding, directing, comforting, and constant influence of the Holy Ghost.")

while True:
    n = int(input("Please enter a number: "))
    new_quote = "".join(
        letter.upper() if (i + 1) % n == 0 else letter for i, letter in enumerate(quote)
    )
    print(new_quote)
    
    another = input("Would you like to enter another number? (yes/no) ").strip().lower()
    if another != "yes":
        print("Goodbye")
        break
