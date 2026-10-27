# LeAnn Anderson
# CIS256 Fall 2026
# Programming Assignment 4

# Import from game
from guess_the_word import words, select_word, check_guess, show_word

# Test selected word
def test_select_word():
    assert select_word() in words

# Test correct letter guess
def test_correct_guess():
    assert check_guess("BASKETBALL", "B") == True

# Test incorrect letter guess
def test_incorrect_guess():
    assert check_guess("BASKETBALL", "F") == False