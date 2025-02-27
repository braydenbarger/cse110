import random
words = ["apple", "grape", "table", "chair", "brick", "sword", "panda", "horse", "mouse", "plant", "flame"]
word = random.choice(words)
guesses = 0
correct = False

print("Welcome to wordle")
print(f"Your hint is: {'_ ' * len(word)}")

while not correct:
    guess = input("What is your guess? ").lower()

    if len(guess) != len(word):
        print(f"Your guess must have the same number of letters as the secret word")
        continue

    guesses += 1

    if guess == word:
        correct = True
        print(f"You guessed it! It took you {guesses} guesses")
    else:
        hint = []
        for i in range(len(word)):
            if guess[i] == word[i]:
                hint.append(guess[i].upper())
            elif guess[i] in word:
                hint.append(guess[i].lower())
            else:
                hint.append('_')
        print(f"Your hint is: {' '.join(hint)}")
