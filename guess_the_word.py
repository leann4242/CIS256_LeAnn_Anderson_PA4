# LeAnn Anderson
# CIS256 Fall 2026
# Programming Assignment 4

import random

# List of words
words = ["basketball", "volleyball", "birthday", "weekend", "Halloween", "Disneyland"]

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

