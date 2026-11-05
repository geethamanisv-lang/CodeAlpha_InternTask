
import random

# Words for each level
easy_words = ["apple", "mango", "grape", "house"]
medium_words = ["python", "coding", "java", "laptop"]
hard_words = ["developer", "programmer", "database", "computer"]

print("Welcome to Hangman Game!")

# Choose difficulty level
print("\nChoose your level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

level = input("Enter your choice (1/2/3): ")

# Set words and attempts based on level
if level == "1":
    words = easy_words
    max_attempts = 6
    print("You selected Easy Level!")

elif level == "2":
    words = medium_words
    max_attempts = 5
    print("You selected Medium Level!")

elif level == "3":
    words = hard_words
    max_attempts = 4
    print("You selected Hard Level!")

else:
    print("Invalid choice!")
    exit()

# Select random word
secret_word = random.choice(words)

guessed_letters = []
wrong_attempts = 0

# Main game loop
while wrong_attempts < max_attempts:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")

    print("Attempts remaining:", max_attempts - wrong_attempts)

# Check loss
if wrong_attempts == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", secret_word)
