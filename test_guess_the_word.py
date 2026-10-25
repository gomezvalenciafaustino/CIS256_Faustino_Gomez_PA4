# Faustino Gomez
# CIS256 Fall 2026
# Programming Assignment 4 Test


from guess_the_word import validate_in_list, is_letter_in_word


# Constants
# These words are in the list
RABBIT = 'rabbit'
DOLPHIN = 'dolphin'

# These words are not in the list
DOG = 'dog'
CAT = 'cat'


# Testing functions for validate_in_list
def test_word_in_list():
    assert validate_in_list(RABBIT) == True
    assert validate_in_list(DOLPHIN) == True

def test_word_not_in_list():
    assert validate_in_list(DOG) == False
    assert validate_in_list(CAT) == False

# Testing functions for is_letter_in_word
def test_letter_in_word():
    assert is_letter_in_word('r',RABBIT) == True
    assert is_letter_in_word('d',DOLPHIN) == True

def test_letter_not_in_word():
    assert is_letter_in_word('p',RABBIT) == False
    assert is_letter_in_word('c',DOLPHIN) == False


# Main program
if __name__ == '__main__':
    pass
# End of program