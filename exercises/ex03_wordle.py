"""Exercise 03 - Making a structured Wordle!"""

__author__ = "730574200"


def input_guess(secret_word_len: int) -> str:
    """Asks player for word and checks if it matches secret word length"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while (
        len(guess) != secret_word_len
    ):  # have to set it up to be not equal so that it can get to being equal and end
        guess = input(
            f"That wasn't {secret_word_len} chars! Try again: "
        )  # need to update variable so no infinite loop
    return guess  # returning string makes easier to use in main


def contains_char(secret: str, char: str) -> bool:
    """Checks whether character is in the hidden word at any location"""
    assert len(char) == 1  # makes sure everything will work
    index: int = 0
    while index < len(secret):  # moves through whole secret word
        if (
            secret[index] == char
        ):  # if that character in the word matches the input character
            index = len(secret)
            return True  # exits function if character found
        else:
            index += 1  # keeps going until character found
    return False  # need to return False if index reaches length without finding char


def emojified(guess: str, secret: str) -> str:
    """outputs emojis showing if characters in guess are in secret word/placed right"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"  # unicode emojies
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    wordle_output: str = ""  # need to make this a variable since it's returned
    while index < len(secret):
        if (
            guess[index] == secret[index]
        ):  # if character at that spot in word matches secret word
            wordle_output += GREEN_BOX
            index += 1  # moves to next character in guess/secret
        elif contains_char(
            secret, guess[index]
        ):  # uses contains_char to see if character is elsewhere in word
            wordle_output += YELLOW_BOX
            index += 1
        else:  # if character at this spot in guess is NOT in secret word
            wordle_output += WHITE_BOX  # if not in word at all
            index += 1  # always have to increase index to get to false in loop
    return wordle_output


def main(secret: str) -> None:
    """Where you enter program/main game loop to put it all together"""
    index: int = 0  # index representing turns and moving through the secret_word
    while index < len(secret):
        print(
            f"=== Turn {index + 1}/{len(secret)} ==="
        )  # have to add 1 so it's not 0/6 to 5/6
        guess: str = input_guess(
            secret_word_len=len(secret)
        )  # define variable guess to use in next function
        print(emojified(guess, secret))
        if guess == secret:  # what we do if person wins/needs another turn
            print(f"You won in {index + 1}/{len(secret)} turns!")
            return None  # needed to exit program here if the person wins
        else:
            index += 1
    print(
        f"X/{len(secret)} - Sorry, try again tomorrow!"
    )  # only print this if they do NOT win (why we exit if they do win)


if __name__ == "__main__":  # allows to be imported
    main(secret="codes")
