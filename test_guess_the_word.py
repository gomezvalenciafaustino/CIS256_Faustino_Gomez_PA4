# Faustino Gomez
# CIS256 Fall 2026
# Programming Assignment 4 Test


from guess_the_word import validate_in_list


# Constants
RABBIT = 'rabbit'
DOLPHIN = 'dolphin'
DOG = 'dog'
CAT = 'cat'


def test_word_in_list():
    assert validate_in_list(RABBIT) == True
    assert validate_in_list(DOLPHIN) == True

def test_word_not_in_list():
    assert validate_in_list(DOG) == False
    assert validate_in_list(CAT) == False


# Main program
if __name__ == '__main__':
    pass
# End of program