import random

play = "yes"
while play == "yes":
    number = random.randint(1, 100)
    guesses = 0
    guess = -1

    while guess != number:
        guess = int(input("What is your guess? "))
        guesses = guesses + 1

        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
        else:
            print("You guessed it!")

    print(f"It took you {guesses} guesses to guess the magic number")
    play = input("Would you like to play again yes or no? ")

print("Goodbye")