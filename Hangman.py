import random

words = ["python", "hangman", "developer", "programming", "internship", "keyboard", "function"]
word = random.choice(words)
guessed = []
tries = 6
display = ["_" for _ in word]

print("Welcome to Hangman!")
print("Guess the word:")

while tries > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Tries left:", tries)
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input.")
        continue

    if guess in guessed:
        print("Already guessed.")
        continue

    guessed.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct!")
    else:
        tries -= 1
        print("Wrong!")

if "_" not in display:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost. The word was:", word)
