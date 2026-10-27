# LeAnn Anderson
# CIS256 Fall 2026
# Programming Assignment 4 - Word Guessing Game

import random

# List of words
words = ["BASKETBALL", "VOLLEYBALL", "BIRTHDAY", "WEEKEND", "HALLOWEEN", "DISNEYLAND"]

# Select random word
def select_word():
    return random.choice(words)

# Check guessed letters
def check_guess(word, letter):
    return letter in word

# Show word with correct letter guesses
def show_word(word, letters_guessed):
    result = ""

    for letter in word:
        if letter in letters_guessed:
            result += letter + " "
        else:
            result += "- "
    return result.strip()

# Run game
def main():

    # Select word
    word = select_word()

    # List for guessed letters
    letters_guessed = []

    # Number of guesses allowed
    guesses_left = 6

    print("\n***** Guessing Game *****")
    print("\nWord: ", show_word(word, letters_guessed))

    while guesses_left > 0:
        print("Letters Guessed: ", letters_guessed)
        print("Guesses left: ", guesses_left)

        # Guess input
        guess = input("\nGuess one letter: ").strip().upper()

        # Check guess
        if len(guess) != 1 or not guess.isalpha():
            print("\nPlease enter only one letter.")
            continue

        if guess in letters_guessed:
            print("\nYou already guessed that letter.")
            continue

        letters_guessed.append(guess)

        if check_guess(word, guess):
            print("\nCorrect letter!")
        else:
            guesses_left -= 1
            print("\nWrong letter!")

        print("Word: ", show_word(word, letters_guessed))

        if "-" not in show_word(word, letters_guessed):
            print("\nCongrats, you guessed the word: ", word,"\n")
            break

    else:
        print("\nBetter luck next time!  The word was: ", word,"\n")

# Run the program
if __name__ == "__main__":
    main()



