# Faustino Gomez
# CIS256 Fall 2026
# Programming Assignment 4


import random


# Constants
ENGLISH_WORDS = (
    'rabbit',
    'butterfly',
    'ladybug',
    'sky',
    'cloud',
    'ocean',
    'dolphin',
    'moon',
    'field',
    'pizza',
    )

WORDS_LIST_ERROR = "There is an issue with the list; the word is not in the list."
SHOW_CURRENT_STATUS = "Current word progress: "
PROMPT_LETTER = "please enter one letter: "
PROMPT_EXIT = "Do you want to end the game? "

TRY_AGAIN = "Please, try again."
WARNING_EMPTY_INPUT = f"You need to enter a letter, {TRY_AGAIN}"
WARNING_ONE_LETTER = f"More than one letter, {TRY_AGAIN}"
WARNING_INVALID_LETTER = f"That is not a valid letter, {TRY_AGAIN}"
WARNING_LETTER_TRIED = f"was already tried, {TRY_AGAIN}"
WARNING_NOT_IN_WORD = "is not part of the word, you have lost one chance"
WARNING_INVALID_OPTION = f"You entered an invalid option, {TRY_AGAIN}"

YES = ('yes', 'y',)
NO = ('no', 'n',)

GAME_ENDED = "Thanks for playing, see you next time!"


def validate_in_list(word_to_guess: str) -> bool:
    ''' Validate if the word is in the list.

        Parameters:
            word_to_guess (str): Word to be guessed.
        Returns:
            bool: True if found, otherwise False.
    '''
    return word_to_guess in ENGLISH_WORDS

def get_random_word() -> str:
    ''' Get random word.

        Parameters:
            None:
        Returns:
            str: Random word from list.
    '''
    return random.choice(ENGLISH_WORDS).lower()

def reveal_letters(word_to_guess: str, remaining_letters_to_guess: list[str]) -> None:
    ''' Shows the guessed letters in the word, if any.

        Parameters:
            word_to_guess (str): The word to be guessed.
            remaining_letters_to_guess (list[str]): List of all letters still pending to be guessed.
        Returns:
            None:
    '''
    partial_guess = [letter if letter not in remaining_letters_to_guess else '*' for letter in word_to_guess]
    print(f"{SHOW_CURRENT_STATUS} {' '.join(partial_guess)}")

def get_letter(letter_tried: list[str]) -> str:
    ''' Get input letter.

        Parameters:
            letter_tried (list[str]): List of all letters already tried.
        Returns:
            str: Letter entered.
    '''
    print()
    while True:
        letter = input(PROMPT_LETTER).strip().lower()
        if not letter:
            print(WARNING_EMPTY_INPUT)
            continue

        if len(letter) > 1:
            print(WARNING_ONE_LETTER)
            continue

        if not letter.isalpha():
            print(WARNING_INVALID_LETTER)
            continue

        if letter in letter_tried:
            print(f"'{letter}' {WARNING_LETTER_TRIED}")
            continue
        return letter

def is_letter_in_word(letter: str, word_to_guess: str) -> bool:
    ''' Validate if the letter is in the word.

        Parameters:
            letter (str): Letter to look for.
            word_to_guess (str): Word to be guessed.
        Returns:
            bool: True if found, otherwise False.
    '''
    return letter in word_to_guess

def confirm_exit() -> bool:
    ''' Confirm exit from game.

        Parameters:
            None:
        Returns:
            bool: True if exit confirmed, False otherwise.
    '''
    while True:
        raw = input(PROMPT_EXIT).strip().lower()
        if raw in YES:
            return True
        if raw in NO:
            return False
        print(WARNING_INVALID_OPTION)


# Main program
if __name__ == '__main__':
    while True:
        word_to_guess = get_random_word()
        if not validate_in_list(word_to_guess):
            print(WORDS_LIST_ERROR)
            break

        remaining_letters_to_guess = list(word_to_guess)
        letter_tried = []
        max_tries = len(word_to_guess)
        tries = max_tries
        while tries:
            reveal_letters(word_to_guess, remaining_letters_to_guess)
            print(f"You have {tries} opportunities left to guess.")

            letter = get_letter(letter_tried)
            letter_tried.append(letter)

            if not is_letter_in_word(letter, word_to_guess):
                print(f"{letter} {WARNING_NOT_IN_WORD}", end="")
                tries -= 1
                if tries:
                    print(f", {TRY_AGAIN}")
                else:
                    print()
                continue

            # Rebuilt letters still pending to guess
            remaining_letters_to_guess = [_ for _ in remaining_letters_to_guess if _ != letter]
            if remaining_letters_to_guess:
                continue

            print(f"\nYou won! You guessed the word {word_to_guess.upper()} " 
                f"with only {max_tries - tries} unsuccessful attempts.")
            break
        else:
            print(f"\nYou didn't win, the word was: {word_to_guess.upper()} " 
                f"and you ran out of opportunities.")
        
        if confirm_exit():
            break
        print()
    print(GAME_ENDED)
# End of program