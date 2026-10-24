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
PROMPT_EXIT = "Do you want to end the game [Yes/No]? "

TRY_AGAIN = "Please, try again."
WARNING_EMPTY_INPUT = f"You need to enter a letter. {TRY_AGAIN}"
WARNING_ONE_LETTER = f"More than one letter. {TRY_AGAIN}"
WARNING_INVALID_LETTER = f"That is not a valid letter. {TRY_AGAIN}"
WARNING_LETTER_TRIED = f"was already tried. {TRY_AGAIN}"
WARNING_NOT_IN_WORD = "is not part of the word. You have lost one chance"
WARNING_LAST_ONE = "and it was the last one."
WARNING_INVALID_OPTION = f"You entered an invalid option. {TRY_AGAIN}"

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

def reveal_letters(word_to_guess: str, unguessed_letters: set) -> None:
    ''' Shows the guessed letters in the word, if any.

        Parameters:
            word_to_guess (str): The word to be guessed.
            unguessed_letters (set): Set of all letters still pending to be guessed.
        Returns:
            None:
    '''
    partial_guess = [letter if letter not in unguessed_letters else '*' for letter in word_to_guess]
    print(f"{SHOW_CURRENT_STATUS} {' '.join(partial_guess)}")

def get_letter(letters_tried: list[str]) -> str:
    ''' Get input letter.

        Parameters:
            letters_tried (list[str]): List of all letters already tried.
        Returns:
            str: A valid, non-keyed letter.
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

        if letter in letters_tried:
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

        unguessed_letters = set(word_to_guess)  # Remove repeated letters in word to guess.
        max_tries = len(unguessed_letters)  # More opportunities if the word is longer, but account for duplicates.
        tries = max_tries
        letters_tried = []

        while tries:
            reveal_letters(word_to_guess, unguessed_letters)  # Show progress.
            print(f"You have {tries} opportunities left to guess.")

            letter = get_letter(letters_tried)
            letters_tried.append(letter)  # Update queue.

            if not is_letter_in_word(letter, word_to_guess):
                print(f"{letter} {WARNING_NOT_IN_WORD}", end="")
                tries -= 1  # One opportunity lost.
                if tries:
                    print(f". {TRY_AGAIN}")
                else:
                    print(f", {WARNING_LAST_ONE}")  # Ran out of opportunities.
                continue

            # Remove found letter from set
            unguessed_letters.remove(letter)
            if not unguessed_letters:
                print(f"\nYou won! You guessed the word {word_to_guess.upper()} " 
                    f"with only {max_tries - tries} unsuccessful attempts.")
                break
        else:
            print(f"\nYou didn't win, the word was: {word_to_guess.upper()} " 
                f"and you ran out of opportunities.")
        
        if confirm_exit():
            break
        print()  # Insert a new line into the console for the new game.
    print(f"\n{GAME_ENDED}")
# End of program